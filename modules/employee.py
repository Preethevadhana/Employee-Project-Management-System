import streamlit as st
import pandas as pd

# Sample employee data
employees = [
    {
        "ID": 1,
        "Name": "John Smith",
        "Department": "IT",
        "Designation": "Software Engineer",
        "Status": "Active"
    },
    {
        "ID": 2,
        "Name": "Emma Johnson",
        "Department": "HR",
        "Designation": "HR Manager",
        "Status": "Active"
    }
]

def employee_page():
    st.title("👨‍💼 Employee Management")

    st.subheader("Employee List")
    df = pd.DataFrame(employees)
    st.dataframe(df, use_container_width=True)

    st.subheader("Add Employee")

    name = st.text_input("Employee Name")
    department = st.text_input("Department")
    designation = st.text_input("Designation")
    status = st.selectbox("Status", ["Active", "Inactive"])

    if st.button("Add Employee"):
        st.success(f"{name} added successfully!")