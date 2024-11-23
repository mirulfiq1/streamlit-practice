import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Homepage",
    page_icon="",
    layout="centered",
    initial_sidebar_state="auto"
)

df = pd.DataFrame({"col1":[1,2,3],
                   "col2": [4, 3, 6]})

if "df" not in st.session_state:
    st.session_state["df"] = df

if __name__ == "__main__":
    st.title("homepage")

st.write(st.session_state)