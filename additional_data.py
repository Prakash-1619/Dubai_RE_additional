import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Additional Data Analysis", layout="wide")
st.title("📊 Additional Data Explorer")

st.sidebar.title("📁 Navigation")

# Sidebar main tab selection
main_tab = st.sidebar.radio("Select View", ["Data", "Charts"])

# Excel paths outside
excel_file_path = 'All_DataFrames.xlsx'
q_summary_path = "Quick_data_summary.xlsx"
summary_path = 'Data_Summaries.xlsx'

# Load sheet names once
xls_main = pd.ExcelFile(excel_file_path)
sheet_names_main = xls_main.sheet_names

# ============== DATA SECTION =================
if main_tab == "Data":
    data_sub_tab = st.sidebar.selectbox("Data Views", ["Preview", "Quick Summary", "Data Summary"])

    if data_sub_tab == "Preview":
        sheet = st.selectbox("Select Data file", sheet_names_main, key="preview_data")
        df = pd.read_excel(excel_file_path, sheet_name=sheet)
        st.subheader(f"🔍 Preview: {sheet}")
        st.dataframe(df, use_container_width=True)

    elif data_sub_tab == "Quick Summary":
        df = pd.read_excel(q_summary_path, sheet_name=0)
        st.subheader("⚡ Quick Summary")
        st.dataframe(df, use_container_width=True)

    elif data_sub_tab == "Data Summary":
        xls_summary = pd.ExcelFile(summary_path)
        sheet_names_summary = xls_summary.sheet_names
        sheet = st.selectbox("Select Summary file", sheet_names_summary, key="summary_data")
        df = pd.read_excel(summary_path, sheet_name=sheet)
        st.subheader(f"📄 Data Summary: {sheet}")
        st.dataframe(df, use_container_width=True)

# ============== CHARTS SECTION =================
elif main_tab == "Charts":
    st.subheader("📈 Yearly Count by Category")

    sheet = st.selectbox("Select Data file", sheet_names_main, key="chart_sheet")
    df = pd.read_excel(excel_file_path, sheet_name=sheet)

    st.write("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    year_col = st.selectbox("Select Year Column", df.columns, index=0)
    category_col = st.selectbox("Select Category Column", df.columns, index=1)
    value_col = st.selectbox("Select Count/Numeric Column", df.columns, index=2)

    plot_type = st.selectbox("Select Plot Type", ["Line", "Bar"])

    if plot_type == "Line":
        fig = px.line(df, x=year_col, y=value_col, color=category_col, markers=True,
                      title="Line Chart: Yearly Count by Category")
    else:
        fig = px.bar(df, x=year_col, y=value_col, color=category_col, barmode='group',
                     title="Bar Chart: Yearly Count by Category")

    st.plotly_chart(fig, use_container_width=True)
