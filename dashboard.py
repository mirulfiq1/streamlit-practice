import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Malaysia Cities Dashboard')

# Upload dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

@st.cache_data
def filter_data(df, min_pop, max_pop):
    return df[(df['population'] >= min_pop) & (df['population'] <= max_pop)]

def generate_scatter_plot(df, x_axis, y_axis):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_axis, y=y_axis, hue='admin_name')
    plt.title(f'{y_axis} vs. {x_axis}')
    st.pyplot(plt)

def generate_histogram(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column, bins=30)
    plt.title(f'{column} Distribution')
    st.pyplot(plt)

def generate_box_plot(df, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='admin_name', y=column)
    plt.xticks(rotation=90)
    plt.title(f'{column} by State')
    st.pyplot(plt)

def generate_bar_plot(df, column):
    top_cities = df.nlargest(10, column)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_cities, x='city', y=column)
    plt.xticks(rotation=90)
    plt.title(f'Top 10 Cities by {column}')
    st.pyplot(plt)

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = load_data(uploaded_file)
    
    # Display the dataframe
    st.write("### Dataset:")
    st.write(df)
    
    # Sidebar for filtering data
    st.sidebar.header("Filter Data")
    min_population = st.sidebar.slider('Minimum Population', min_value=int(df['population'].min()), max_value=int(df['population'].max()), value=int(df['population'].min()))
    max_population = st.sidebar.slider('Maximum Population', min_value=int(df['population'].min()), max_value=int(df['population'].max()), value=int(df['population'].max()))
    
    filtered_df = filter_data(df, min_population, max_population)
    
    st.write(f"Filtered Dataset (Population between {min_population} and {max_population}):")
    st.write(filtered_df)
    
    # Form for user input
    with st.form(key='my_form'):
        st.header("User Input Form")
        
        # Text input for user name
        user_name = st.text_input('Enter your name:')
        
        # Multiple choice for favorite city
        favorite_city = st.selectbox('Select your favorite city:', df['city'].unique())
        
        # Number input for age
        age = st.number_input('Enter your age:', min_value=0, max_value=100, value=25)
        
        # Submit button
        submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        st.write(f"Hello {user_name}, you selected {favorite_city} as your favorite city and your age is {age}.")
    
    # Metrics display
    total_cities = len(df['city'].unique())
    total_population = df['population'].sum()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Total Cities", value=total_cities)
    
    with col2:
        st.metric(label="Total Population", value=total_population)
    
    # Dashboard with multiple plots
    st.write("### Dashboard:")
    
    # Plot 1: Scatter plot of population vs. latitude
    st.write("#### Scatter Plot: Population vs. Latitude")
    if st.button('Generate Scatter Plot'):
        generate_scatter_plot(filtered_df, 'lat', 'population')
    
    # Plot 2: Histogram of population
    st.write("#### Histogram: Population")
    if st.button('Generate Histogram'):
        generate_histogram(filtered_df, 'population')
    
    # Plot 3: Box plot of population by state
    st.write("#### Box Plot: Population by State")
    if st.button('Generate Box Plot'):
        generate_box_plot(filtered_df, 'population')
    
    # Plot 4: Bar plot of top 10 cities by population
    st.write("#### Bar Plot: Top 10 Cities by Population")
    if st.button('Generate Bar Plot'):
        generate_bar_plot(filtered_df, 'population')
    
    # Advanced feature: Tabs for different plots
    tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Histogram", "Box Plot", "Bar Plot"])
    
    with tab1:
        st.header("Scatter Plot")
        generate_scatter_plot(filtered_df, 'lat', 'population')
    
    with tab2:
        st.header("Histogram")
        generate_histogram(filtered_df, 'population')
    
    with tab3:
        st.header("Box Plot")
        generate_box_plot(filtered_df, 'population')
    
    with tab4:
        st.header("Bar Plot")
        generate_bar_plot(filtered_df, 'population')

#st.cache_data = serializable object(str, int, float, dataframe, array, list.etc)
#st.cache_resource = ML models and Database connections

#cache literally making copy of the object before sending to the browser
#copying prevent mutation and concurrency

#cache.resource dont make a copy like cache_data/ the object not mutated/ just keep in cache no copy

#cache duration = @st.cache_data(ttl=3600) ---- this is 1 hour duration
#cache size = @st.cache_data(max_entries=1000) ---- will discard old values if too many than max entries

#exclude input parameters = a cache function must have hashable input parameters
# not all parameter can be hash.. so can put underscore to the variable model for example

# can customize the spinner

#cache resource dont make copy so it can run large dataset smoothly

#streamlit run top to bottom, no varibles shared between runs
