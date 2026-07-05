import streamlit as st

def department_page():
    st.title("🏢 Department Management")

    st.subheader("Create Department")

    department_name = st.text_input("Department Name")
    department_head = st.text_input("Department Head")

    if st.button("Create Department"):
        st.success(f"Department '{department_name}' created successfully!")

    st.divider()

    st.subheader("Department Statistics")

    st.metric("Total Departments", 5)
    st.metric("Department Heads", 5)