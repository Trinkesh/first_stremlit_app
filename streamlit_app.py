
import streamlit 

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 Blueberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket smoothies')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# lets add a pick list here so they can pick fruit they wanted to include

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display the table on the page 
streamlit.dataframe(my_fruit_list)
