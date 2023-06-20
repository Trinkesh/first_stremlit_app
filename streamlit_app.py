
import streamlit 
import snowflake.connector
import requests
import pandas
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 Blueberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket smoothies')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# lets add a pick list here so they can pick fruit they wanted to include

# adding a function to show only selected fruits from the list into the table


fruit_selected =   streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

# display the table on the page 
streamlit.dataframe(fruits_to_show)

# lets add some request libabry to display fruitevice api response
# lets get the fruite vice data looking little nicer

# new section to display frute vise api reponse 
# create a repetable code block

def get_fruityvice_data(this_fruit_choice):
	
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
  	streamlit.error("Please select a fruit to get the information.")
  else:
        back_from_function = get_fruityvice_data(fruit_choice)
	streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

# don't run anything past here while we troubleshoot 

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruite load list conatins:")
streamlit.dataframe(my_data_rows) 


#added some changes 

fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding Jackfruit', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

