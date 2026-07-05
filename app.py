import streamlit as st

from modules.dashboard import dashboard_page
from modules.employee import employee_page
from modules.department import department_page
from modules.project import project_page
from modules.task import task_page
from modules.attendance import attendance_page
from modules.reports import reports_page

st.set_page_config(
    page_title="Enterprise Employee & Project Management System",
    page_icon="🏢",
    layout="wide"
)

st.sidebar.title("🏢 Enterprise System")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Employees",
        "Departments",
        "Projects",
        "Tasks",
        "Attendance",
        "Reports"
    ]
)

if menu == "Dashboard":
    dashboard_page()

elif menu == "Employees":
    employee_page()

elif menu == "Departments":
    department_page()

elif menu == "Projects":
    project_page()

elif menu == "Tasks":
    task_page()

elif menu == "Attendance":
    attendance_page()

elif menu == "Reports":
    reports_page()