import streamlit as st
import pandas as pd

st.title("Your Title")

st.header("Main Header")
st.subheader("Sub Header")

st.markdown("This is Markdown **bold**")
st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("## Header 3")

st.caption("This is caption")

st.code("import pandas as pd")

st.text("text")

st.latex("x =2^2")

st.divider()

st.write("Can display dataframe and many more thing")

df = pd.read_excel("combined_warping_batch3_result.xlsx")

st.dataframe(df)
st.write(df)

st.table(df)

st.metric(label='Population', value = 900, delta = 100, delta_color = "normal")