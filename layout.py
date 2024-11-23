#streamlit layout
#1. can do sidebar
#2. can create column to arrange object
#3. can create tabs to change between plots
#4. can create expander
#5. can create container

import streamlit as st

# Title of the app
st.title("Streamlit Layout Demo")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar.")

# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.header("Tab 1")
    st.write("Content for tab 1")

with tab2:
    st.header("Tab 2")
    st.write("Content for tab 2")

# Expander
with st.expander("Expander"):
    st.write("This is an expander. You can put long content here.")

# Container
with st.container():
    st.header("Container")
    st.write("This is a container. You can group multiple elements here.")

# Display the layout
st.write("This is the main area of the app.")