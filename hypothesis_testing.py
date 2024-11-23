import streamlit as st
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache
def load_data(file):
    return pd.read_csv(file)

# Load the dataframes
df_1 = load_data('CLEAN_House1.csv')
df_2 = load_data('CLEAN_House2.csv')
df_3 = load_data('CLEAN_House3.csv')
df_4 = load_data('CLEAN_House4.csv')
df_5 = load_data('CLEAN_House5.csv')
df_6 = load_data('CLEAN_House11.csv')

st.title("Comprehensive A/B Testing App")

# Select dataframe
df_option = st.selectbox("Select the dataframe", ["House1", "House2", "House3", "House4", "House5", "House11"])
df_dict = {"House1": df_1, "House2": df_2, "House3": df_3, "House4": df_4, "House5": df_5, "House11": df_6}
df = df_dict[df_option]

st.write("Data Preview:")
st.write(df.head())

# Select columns for A/B testing
group_col = st.selectbox("Select the column for groups", df.columns)
value_col = st.selectbox("Select the column for values", df.columns)

# Check normality
group_a = df[df[group_col] == 'A'][value_col]
group_b = df[df[group_col] == 'B'][value_col]
normal_a = stats.shapiro(group_a)[1] > 0.05
normal_b = stats.shapiro(group_b)[1] > 0.05

st.write(f"Group A normality: {'Normal' if normal_a else 'Non-normal'}")
st.write(f"Group B normality: {'Normal' if normal_b else 'Non-normal'}")

# Select statistical test based on normality
if normal_a and normal_b:
    test_type = st.selectbox("Select the parametric test", ["t-test", "ANOVA"])
else:
    test_type = st.selectbox("Select the non-parametric test", ["Mann-Whitney U", "Kruskal-Wallis"])

if st.button("Perform Test"):
    if test_type == "t-test":
        t_stat, p_value = stats.ttest_ind(group_a, group_b)
        st.write(f"t-statistic: {t_stat:.2f}")
        st.write(f"p-value: {p_value:.2e}")
    elif test_type == "ANOVA":
        f_stat, p_value = stats.f_oneway(group_a, group_b)
        st.write(f"F-statistic: {f_stat:.2f}")
        st.write(f"p-value: {p_value:.2e}")
    elif test_type == "Mann-Whitney U":
        u_stat, p_value = stats.mannwhitneyu(group_a, group_b)
        st.write(f"U-statistic: {u_stat:.2f}")
        st.write(f"p-value: {p_value:.2e}")
    elif test_type == "Kruskal-Wallis":
        h_stat, p_value = stats.kruskal(group_a, group_b)
        st.write(f"H-statistic: {h_stat:.2f}")
        st.write(f"p-value: {p_value:.2e}")

    if p_value < 0.05:
        st.write("There is a significant difference between the groups.")
    else:
        st.write("There is no significant difference between the groups.")

# Visualization
st.write("Data Visualization:")
sns.boxplot(x=group_col, y=value_col, data=df)
st.pyplot(plt)