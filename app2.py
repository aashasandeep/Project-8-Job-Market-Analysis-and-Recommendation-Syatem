import pandas as pd
import plotly.express as px
import streamlit as st




 # Create Streamlit app
st.title('Remote Work Trends Dashboard')

# Refresh button
if st.button('Refresh Data'):
        st.experimental_rerun() 

from PIL import Image 

img = Image.open("Pro-8 Average Hourly Rates by Country.png")
st.image(img)

img = Image.open("Pro-8 Bubble plot of keywords correlation with salary.png")
st.image(img)

img = Image.open("Pro-8 Top Emerging job titles over time.png")
st.image(img)

img = Image.open("Pro-8 Number of postings.png")
st.image(img)




