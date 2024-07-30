import os
import streamlit as st
import langchain_helper

os.environ[
    "OPENAI_API_KEY"] = ""

st.title("Restaurant Menu Item Generator")

cuisine = st.selectbox(label="Select Food Category",
                       options=["Indian", "Mexican", "Italian", "Chinese"])

if cuisine:
  response = langchain_helper.generate_restraunts_menu_items(cuisine)

  st.header(f"Restaurant Name: {response['restraunt_name'].strip()}")

  menu_items = response["menu_items"].strip().split(",")

  st.write("***Menu Items***")

  for item in menu_items:
    st.write(f"- {item}")
