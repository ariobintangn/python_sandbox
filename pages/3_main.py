import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,4),
    columns=["a","b","c","d"]
)

x = st.text_input("Favorite Movie?")
st.write(f"you favorite movie is: {x}")

data = pd.read_csv("movies.csv")

filtered_data = data[['budget','title','director','genres']]
filtered_data.index = filtered_data.index + 1

top_50_data = filtered_data.head(50)

directors = sorted(top_50_data['director'].unique())
selected_director = st.selectbox("Select Director", options=["All"] + list(directors))

if selected_director != "All":
    top_50_data = top_50_data[top_50_data['director'] == selected_director]

budget_by_director = top_50_data.groupby('director')['budget'].sum().reset_index()

st.write(top_50_data)
st.bar_chart(budget_by_director.set_index('director'))

st.bar_chart(chart_data)
st.line_chart(chart_data)