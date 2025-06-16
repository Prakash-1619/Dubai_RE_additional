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
    data_sub_tab = st.tabs(["Preview", "Quick Summary", "Data Summary"])

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
    st.subheader("📈 Chart Visualization")

    sheet = st.selectbox("Select Data file", sheet_names_main, key="chart_sheet")
    df = pd.read_excel(excel_file_path, sheet_name=sheet)

    #st.write("Data Preview")
    #st.dataframe(df.head(), use_container_width=True)

    plot_type = st.selectbox("Select Plot Type", ["Line", "Bar"])

    # Define column types
    categorical_columns = df.select_dtypes(include=['object', 'string']).columns.tolist()
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    # Ensure 'Year' column is present
    if "Year" not in df.columns:
        st.error("❌ 'Year' column not found in the dataset.")
    else:
        if plot_type == "Line":
            value_col = st.selectbox("Select Numeric Column (Y-Axis)", [col for col in numeric_columns if col != "Year"])
            category_col = st.selectbox("Select Category Column (Legend)", categorical_columns)

            fig = px.line(
                df,
                x="Year",
                y=value_col,
                color=category_col,
                markers=True,
                title=f"Line Chart: {value_col} over Years by {category_col}"
            )

        else:  # Bar plot (not grouped)
            category_col = st.selectbox("Select Category Column (X-Axis)", categorical_columns)
            value_col = st.selectbox("Select Numeric Column (Y-Axis)", [col for col in numeric_columns if col != "Year"])

            fig = px.bar(
                df,
                x=category_col,
                y=value_col,
                color="Year",  # still colored by year
                title=f"Bar Chart: {value_col} by {category_col} with Year as Legend"
            )

        st.plotly_chart(fig, use_container_width=True)
