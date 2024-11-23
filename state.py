import streamlit as st

# Title of the app
st.title('Stateful App Example')

# Initialize state using key-value syntax
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

# Initialize state using attribute syntax
if 'name' not in st.session_state:
    st.session_state.name = "Streamlit User"

# Function to read state
def read_state():
    st.write(f"Counter: {st.session_state['counter']}")
    st.write(f"Name: {st.session_state.name}")

# Function to update state
def update_state():
    st.session_state['counter'] += 1
    st.session_state.name = st.text_input("Enter new name:", value=st.session_state.name)

# Function to delete state
def delete_state():
    if 'counter' in st.session_state:
        del st.session_state['counter']
    if 'name' in st.session_state:
        del st.session_state.name

# Display current state
st.header("Current State")
read_state()

# Update state
st.header("Update State")
if st.button('Increment Counter'):
    update_state()
    read_state()

# Delete state
st.header("Delete State")
if st.button('Delete State'):
    delete_state()
    st.write("State deleted.")
    read_state()

#session state for widget

#callback is run first before run anything else
# on change = for other than button, on click = for button
