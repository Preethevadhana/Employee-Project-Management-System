import streamlit as st

def project_page():
    st.title("📁 Project Management")

    st.subheader("Create Project")

    project_name = st.text_input("Project Name")
    description = st.text_area("Project Description")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    status = st.selectbox(
        "Project Status",
        ["Planning", "In Progress", "Completed"]
    )

    if st.button("Create Project"):
        st.success(f"Project '{project_name}' created successfully!")

    st.divider()

    st.subheader("Project Overview")

    st.metric("Active Projects", 10)
    st.metric("Completed Projects", 4)