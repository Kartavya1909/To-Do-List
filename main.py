import streamlit as st

st.title("To-Do List")

task = st.text_input("Add a task", key="new_task", on_change=lambda: add_task())
def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        st.session_state.new_task = ""  # Clear input after adding task
        st.rerun() 
        
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        st.rerun()

if st.checkbox("Mark All"):
    for t in st.session_state.tasks:
        t["completed"] = True
    st.rerun()

show_completed = st.checkbox("Show Completed Tasks")
if show_completed:
    tasks_to_display = st.session_state.tasks
else:
    tasks_to_display = [t for t in st.session_state.tasks if not t["completed"]]

st.write("### Tasks")
if tasks_to_display:
    for i, t in enumerate(tasks_to_display, start=1):
        task = t["task"]
        completed = t["completed"]
        t["completed"] = st.checkbox(f"{i}. {task}", value=completed)
else:
    st.write("No tasks added")

if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]
    st.rerun()
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.rerun()