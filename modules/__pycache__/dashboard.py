import streamlit as st

def dashboard_page():
    st.title("📊 Enterprise Analytics Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Employees", 120)

    with col2:
        st.metric("Active Projects", 15)

    with col3:
        st.metric("Completed Projects", 30)

    with col4:
        st.metric("Pending Tasks", 48)

    st.divider()

    st.subheader("Department Performance")

    st.progress(85, text="IT Department")
    st.progress(72, text="HR Department")
    st.progress(91, text="Finance Department")

    st.divider()

    st.subheader("Attendance Statistics")

    st.metric("Today's Attendance", "95%")

    st.success("Dashboard loaded successfully.")