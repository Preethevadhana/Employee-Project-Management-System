import streamlit as st

def reports_page():
    st.title("📄 Reports")

    st.subheader("Download Reports")

    report_type = st.selectbox(
        "Select Report",
        [
            "Employee Report",
            "Department Report",
            "Project Report",
            "Task Report",
            "Attendance Report",
            "Performance Report"
        ]
    )

    export_type = st.selectbox(
        "Export Format",
        [
            "PDF",
            "CSV",
            "Excel"
        ]
    )

    if st.button("Generate Report"):
        st.success(f"{report_type} generated successfully in {export_type} format.")