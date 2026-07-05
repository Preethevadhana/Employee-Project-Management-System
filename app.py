import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Enterprise Employee & Project Management System",
    page_icon="🏢",
    layout="wide"
)

# Title
st.title("🏢 Enterprise Employee & Project Management System")

st.write("""
Welcome to the Enterprise Employee & Project Management System.

This application helps organizations manage:

- 👨‍💼 Employees
- 🏢 Departments
- 📁 Projects
- ✅ Tasks
- 📅 Attendance
- 📊 Analytics Dashboard
- 📄 Reports
""")

st.header("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Employees", "120")

with col2:
    st.metric("Active Projects", "15")

with col3:
    st.metric("Completed Projects", "30")

with col4:
    st.metric("Pending Tasks", "48")

st.success("System is running successfully.")