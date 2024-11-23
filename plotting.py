import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Dashboard App')

# Upload dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = load_data(uploaded_file)
    
    # Display the dataframe
    st.write("### Dataset:")
    st.write(df)
    
    # Dashboard with multiple plots
    st.write("### Dashboard:")
    
    # Plot 1: Scatter plot
    st.write("#### Scatter Plot:")
    columns = df.columns.tolist()
    x_axis = st.selectbox('X-axis for Scatter', columns, key='scatter_x')
    y_axis = st.selectbox('Y-axis for Scatter', columns, key='scatter_y')
    if st.button('Generate Scatter Plot', key='scatter_button'):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=x_axis, y=y_axis)
        st.pyplot(plt)
    
    # Plot 2: Histogram
    st.write("#### Histogram:")
    hist_column = st.selectbox('Column for Histogram', columns, key='hist')
    if st.button('Generate Histogram', key='hist_button'):
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=hist_column)
        st.pyplot(plt)
    
    # Plot 3: Box plot
    st.write("#### Box Plot:")
    box_column = st.selectbox('Column for Box Plot', columns, key='box')
    if st.button('Generate Box Plot', key='box_button'):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=box_column)
        st.pyplot(plt)