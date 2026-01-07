import streamlit as st
import functions as fn

st.title("To do List")

todolist = fn.read_todos()
for todo in todolist:
    st.checkbox(todo)

st.text_input("",placeholder="Add to do")

