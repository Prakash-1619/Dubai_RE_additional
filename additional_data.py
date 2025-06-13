import streamlit as st
import pandas as pd

st.set_page_config(page_title="Additional Data Analysis", layout="centered")

st.title("Additional_data")

# Path to your Excel file
excel_file_path = ""  # <- Replace with your actual file name

# Check if file exists

# Read the Excel file
Preview,Alldata,Datasummary = st.tabs("Preview","Quick Summary","Data Summary")
with Preview:
  xls = pd.ExcelFile(excel_file_path)
  sheet_names = xls.sheet_names
  sheet = st.selectbox("Select Data file", sheet_names)

  # Read selected sheet
  df = pd.read_excel(excel_file_path, sheet_name=sheet)

  # Display DataFrame
  st.dataframe(df, use_container_width=True)
with Alldata:
  xls = pd.ExcelFile(excel_file_path)
  #sheet_names = xls.sheet_names
  #sheet = st.selectbox("Select sheet", sheet_names)

  # Read selected sheet
  #df = pd.read_excel(excel_file_path, sheet_name=sheet)
  #st.success(f"Showing data from '{sheet}'")

  # Display DataFrame
  st.dataframe(xls, use_container_width=True)
with Datasummary:
  with Preview:
  xls = pd.ExcelFile(excel_file_path)
  sheet_names = xls.sheet_names
  sheet = st.selectbox("Select Data file", sheet_names)

  # Read selected sheet
  df = pd.read_excel(excel_file_path, sheet_name=sheet)

  # Display DataFrame
  st.dataframe(df, use_container_width=True)
