import streamlit as st

def attendance_page():
    st.title("📅 Attendance Management")

    st.subheader("Mark Attendance")

    employee_name = st.text_input("Employee Name")
    attendance_status = st.selectbox(
        "Attendance Status",
        ["Present", "Absent", "Leave"]
    )

    if st.button("Mark Attendance"):
        st.success(f"Attendance marked for {employee_name}")

    st.divider()

    st.subheader("Attendance Summary")

    st.metric("Present Today", 95)
    st.metric("Absent Today", 5)
    st.metric("On Leave", 2)