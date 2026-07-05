import streamlit as st

def task_page():
    st.title("✅ Task Management")

    st.subheader("Assign New Task")

    task_name = st.text_input("Task Name")
    assigned_to = st.text_input("Assign To")
    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )
    due_date = st.date_input("Due Date")
    status = st.selectbox(
        "Status",
        ["Pending", "In Progress", "Completed"]
    )

    if st.button("Assign Task"):
        st.success(f"Task '{task_name}' assigned successfully!")

    st.divider()

    st.subheader("Task Summary")

    st.metric("Total Tasks", 25)
    st.metric("Pending Tasks", 8)
    st.metric("Completed Tasks", 17)