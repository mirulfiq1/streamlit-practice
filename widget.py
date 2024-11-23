import streamlit as st
import pandas as pd

# Load the DataFrame
df = pd.read_csv("my.csv")

# Title of the app
st.title("Streamlit Widgets Demo with DataFrame")

# Display the DataFrame
st.write("Here's the DataFrame loaded from my.csv:")
st.dataframe(df)

# Button widgets
if st.button('Primary Button'):
    st.write('Primary Button clicked!')

if st.button('Secondary Button', key='secondary'):
    st.write('Secondary Button clicked!')

# Checkbox widget
checkbox = st.checkbox('Check me out')
if checkbox:
    st.write('Checkbox is checked!')

# Radio button widget
radio = st.radio('Choose an option:', ('Option 1', 'Option 2', 'Option 3'))
st.write(f'You selected: {radio}')

# Radio button widget
radio = st.radio('Select columns:', options=df.columns[1:], index=1, horizontal = True)
st.write(f'You selected: {radio}')

st.divider()

# Selectbox widget
selectbox = st.selectbox('Select an option:', ['Option A', 'Option B', 'Option C'])
st.write(f'You selected: {selectbox}')

st.divider()

# Multiselect widget
multiselect = st.multiselect('Select multiple options:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {multiselect}')

multiselect = st.multiselect('Select columns:', options=df.columns[1:], default=[df.columns[1]], max_selections=2)
st.write(f'You selected: {multiselect}')

# Slider widget with step
slider = st.slider('Select a range of values:', 0.0, 100.0, (25.0, 75.0), step=0.1)
st.write(f'Slider range: {slider}')

# Advanced function: Conditional display
if st.button('Show Advanced Features'):
    st.write('Advanced features are now visible!')
    st.text_area('Enter some text:')
    st.date_input('Pick a date:')
    st.file_uploader('Upload a file:')

# Text input widget
text_input = st.text_input('Enter some text:')
st.write(f'You entered: {text_input}')

# Number input widget
number_input = st.number_input('Enter a number:', min_value=0, max_value=100, value=50)
st.write(f'You entered: {number_input}')

# Text area widget
text_area = st.text_area('Enter a long text:', height=200, placeholder="write your story")
st.write(f'You entered: {text_area}')
