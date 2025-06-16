import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Additional Data Analysis", layout="wide")

st.sidebar.title("Additional_data")

# Sidebar navigation
selected_tab = st.sidebar.radio("Choose View", ["Data", "Charts"])

# ==================== DATA VIEW ====================
if selected_tab == "Data":
    Preview, Alldata, Datasummary = st.tabs(["Preview", "Quick Summary", "Data Summary"])

    with Preview:
        excel_file_path = 'All_DataFrames.xlsx'
        xls = pd.ExcelFile(excel_file_path)
        sheet_names = xls.sheet_names
        sheet = st.selectbox("Select Data file", sheet_names, key="preview")

        df = pd.read_excel(excel_file_path, sheet_name=sheet)
        st.dataframe(df, use_container_width=True)

    with Alldata:
        excel_file_path = "Quick_data_summary.xlsx"
        df = pd.read_excel(excel_file_path, sheet_name=0)
        st.dataframe(df, use_container_width=True)

    with Datasummary:
        excel_file_path = 'Data_Summaries.xlsx'
        xls = pd.ExcelFile(excel_file_path)
        sheet_names = xls.sheet_names
        sheet = st.selectbox("Select Summary file", sheet_names, key="summary")

        df = pd.read_excel(excel_file_path, sheet_name=sheet)
        st.dataframe(df, use_container_width=True)

# ==================== CHARTS VIEW ====================
elif selected_tab == "Charts":
    st.subheader("Yearly Count by Category")

    uploaded_file = st.file_uploader("Upload Excel file with Year, Category, Count", type=["xlsx"])
    
    if uploaded_file:
        sheet_name = st.text_input("Enter Sheet Name (or leave blank for first sheet)")
        
        try:
            if sheet_name:
                df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            else:
                df = pd.read_excel(uploaded_file, sheet_name=0)
                
            st.write("Data Preview")
            st.dataframe(df.head(), use_container_width=True)

            # Column selectors
            year_col = st.selectbox("Select Year Column", df.columns, index=0)
            category_col = st.selectbox("Select Category Column", df.columns, index=1)
            value_col = st.selectbox("Select Count/Numeric Column", df.columns, index=2)

            # Plot type selector
            plot_type = st.selectbox("Select Plot Type", ["Line", "Bar"])

            # Plot
            if plot_type == "Line":
                fig = px.line(df, x=year_col, y=value_col, color=category_col, markers=True,
                              title="Line Chart: Yearly Count by Category")
            else:
                fig = px.bar(df, x=year_col, y=value_col, color=category_col, barmode='group',
                             title="Bar Chart: Yearly Count by Category")

            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error loading sheet: {e}")
    else:
        st.info("Upload an Excel file to show the chart.")
