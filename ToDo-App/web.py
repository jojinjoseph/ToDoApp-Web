import streamlit as st
import functions as fn

todolist = fn.read_todos()
def add_todo():
    todo = st.session_state["todo"]+"\n"
    todolist.append(todo)
    fn.add_values(todolist)
    st.session_state["todo"] = ""


st.title("To do List")
st.write("You can track your to-do list")


for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox :
        todolist.pop(index)
        fn.add_values(todolist)
        del st.session_state[todo]
        st.rerun()

st.text_input("",placeholder="Add to do",key='todo', on_change=add_todo)
