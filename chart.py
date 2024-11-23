import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("my.csv")

st.line_chart(df, x="population", y=["lon", "lat"])

st.area_chart(df, x="population", y=["lon", "lat"])

st.bar_chart(df, x="population", y=["lon", "lat"])

st.map(df)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(df['population'], df['lon'], label='Longitude')
ax.plot(df['population'], df['lat'], label='Latitude')

# Add labels and title
ax.set_xlabel('Population')
ax.set_ylabel('Coordinates')
ax.set_title('Population vs Coordinates')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)