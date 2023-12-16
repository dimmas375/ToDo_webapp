import streamlit as st
from modules import functions as f


def web_add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    if new_todo not in todos:
        todos.append(new_todo)
        f.write_one_todo(new_todo)
    st.session_state['new_todo'] = ''
    return


st.title('ToDo App')

result, todos = f.read_todos()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_all_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input('Enter a ToDo:', placeholder='Add your todo here...', label_visibility='hidden',
              on_change=web_add_todo, key='new_todo')
