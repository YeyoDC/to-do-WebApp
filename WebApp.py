import streamlit as st
import  functions
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    st.session_state['new_todo'] = ''
    functions.update_todos(todos)

def complete_todo():
    print('')



st.title("My Todo App")
st.subheader("This is my todo app")
st.write("this app is increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.update_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
input = st.text_input(label="enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key ='new_todo')

complete_button = st.button("Complete", on_click=complete_todo)

st.write(st.session_state)