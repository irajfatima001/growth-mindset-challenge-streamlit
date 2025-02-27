
# from fpdf import FPDF
# import streamlit as st
# import pandas as pd
# import os
# import numpy as np
# from io import BytesIO

# st.set_page_config(page_title="Data Sweeper", layout='wide')

# # Stylish CSS
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(135deg, #1e3c72, #2a5298);
#             font-family: 'Arial', sans-serif;
#         }
#         .main-title {
#             text-align: center;
#             font-size: 2.5rem;
#             font-weight: bold;
#             color: white;
#             margin-bottom: 20px;
#         }
#         .sub-title {
#             text-align: center;
#             font-size: 1.5rem;
#             color: white;
#         }
#         .card {
#             background: white;
#             padding: 20px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
#             margin: 20px auto;
#             max-width: 800px;
#         }
#         .stButton>button {
#             background: linear-gradient(135deg, #00c6ff, #0072ff);
#             color: white;
#             font-size: 1.1rem;
#             padding: 10px;
#             border-radius: 10px;
#             border: none;
#             transition: 0.3s;
#         }
#         .stButton>button:hover {
#             background: linear-gradient(135deg, #0072ff, #00c6ff);
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Page Title
# st.markdown('<h1 class="main-title">🚀 Data Sweeper</h1>', unsafe_allow_html=True)
# st.markdown('<h2 class="sub-title">Transform, Clean & Visualize Your Data Easily!</h2>', unsafe_allow_html=True)

# # File Uploader
# # uploaded_files = st.file_uploader("📂 Upload CSV or Excel Files:", type=["csv", "xlsx"], accept_multiple_files=True)

# # Global Session States
# # if "file_history" not in st.session_state:
# #     st.session_state.file_history = []
# if "undo_stack" not in st.session_state:
#     st.session_state.undo_stack = {}
# if "redo_stack" not in st.session_state:
#     st.session_state.redo_stack = {}

# # ✅ Function to save history 
# def save_history(file_name, df):
#     if file_name not in st.session_state.undo_stack:
#         st.session_state.undo_stack[file_name] = []
#     st.session_state.undo_stack[file_name].append(df.copy())

# # ✅ Function for undo
# def undo(file_name):
#     if file_name in st.session_state.undo_stack and len(st.session_state.undo_stack[file_name]) > 1:
#         if file_name not in st.session_state.redo_stack:
#             st.session_state.redo_stack[file_name] = []
#         st.session_state.redo_stack[file_name].append(st.session_state.undo_stack[file_name].pop())
#         return st.session_state.undo_stack[file_name][-1]
#     return None

# # ✅ Function for redo
# def redo(file_name):
#     if file_name in st.session_state.redo_stack and st.session_state.redo_stack[file_name]:
#         df = st.session_state.redo_stack[file_name].pop()
#         st.session_state.undo_stack[file_name].append(df)
#         return df
#     return None

# # if uploaded_files:
# #     for file in uploaded_files:
# #         file_ext = os.path.splitext(file.name)[-1].lower()

# #         # ✅ Read the file based on extension
# #         if file_ext == ".csv":
# #             df = pd.read_csv(file)
# #         elif file_ext == ".xlsx":
# #             df = pd.read_excel(file)
# #         else:
# #             st.error(f"❌ Unsupported file type: {file_ext}")
# #             continue

# #         # ✅ Prevent duplicate history entry
# #         if not any(entry["File Name"] == file.name for entry in st.session_state.file_history):
# #             st.session_state.file_history.append({"File Name": file.name, "Size (KB)": f"{file.size/1024:.2f} KB"})

# #         # ✅ Save initial history (but don't duplicate it)
# #         if file.name not in st.session_state.undo_stack:
# #             save_history(file.name, df)

# #         st.subheader(f"📄 File: {file.name}")
# #         st.write(f"📏 Size: {file.size / 1024:.2f} KB")
# #         st.dataframe(df.head())

# # ✅ Check for duplicate files before processing
# # ✅ File Uploader
# uploaded_files = st.file_uploader("📂 Upload CSV or Excel Files:", type=["csv", "xlsx"], accept_multiple_files=True)

# # ✅ Session state initialize
# if "file_history" not in st.session_state:
#     st.session_state.file_history = {}  # Dictionary to store file name & dataframe

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"❌ Unsupported file type: {file_ext}")
#             continue
        
#         # ✅ Allow re-upload but prevent history duplication
#         if file.name in st.session_state.file_history:
#             st.warning(f"⚠️ '{file.name}' is already uploaded. Overwriting the previous version.")

#         # ✅ Save the latest uploaded file
#         st.session_state.file_history[file.name] = df

#         # ✅ Show the file
#         st.subheader(f"📄 File: {file.name}")
#         st.write(f"📏 Size: {file.size / 1024:.2f} KB")
#         st.dataframe(df.head())


#         # Undo / Redo
#         col1, col2 = st.columns(2)
#         with col1:
#            if st.button(f"↩️ Undo {file.name}", key=f"undo_{file.name}"):
#               df = undo(file.name)
#               if df is not None:
#                  st.success(f"Undo successful for {file.name}!")

#         with col2:
#            if st.button(f"↪️ Redo {file.name}", key=f"redo_{file.name}"):
#               df = redo(file.name)
#               if df is not None:
#                  st.success(f"Redo successful for {file.name}!")

#         # ✅ Data Cleaning Options
#         st.subheader("🛠 Data Cleaning")
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button(f"🗑 Remove Duplicates from {file.name}"):
#                 df.drop_duplicates(inplace=True)
#                 st.write("✅ Duplicates Removed!")

#         with col2:
#             missing_option = st.selectbox(
#                 f"📉 Handle Missing Values ({file.name})",
#                 ["None", "Mean", "Median", "Mode"],
#                 key=f"missing_{file.name}"  
#             )

#             if missing_option != "None":
#                 for col in df.select_dtypes(include=np.number).columns:
#                     if missing_option == "Mean":
#                         df[col].fillna(df[col].mean(), inplace=True)
#                     elif missing_option == "Median":
#                         df[col].fillna(df[col].median(), inplace=True)
#                     elif missing_option == "Mode":
#                         df[col].fillna(df[col].mode()[0], inplace=True)
#                 st.write(f"✅ Missing values filled using {missing_option}!")

#         # ✅ Data Visualization
#         st.subheader("📊 Data Visualization")
#         numeric_columns = df.select_dtypes(include=np.number).columns

#         if len(numeric_columns) > 0:
#             vis_col = st.selectbox("📈 Choose Column for Visualization", numeric_columns)
#             if vis_col:
#                 st.bar_chart(df[vis_col])
#         else:
#             st.warning("⚠️ No numeric columns available for visualization.")

#         # ✅ Generate PDF Report
#         st.subheader("📄 Generate PDF Report")
#         if st.button(f"📥 Download Report for {file.name}"):
#             pdf = FPDF()
#             pdf.add_page()
#             pdf.set_font("Arial", size=12)
#             pdf.cell(200, 10, f"Data Report - {file.name}", ln=True, align='C')

#             pdf.cell(200, 10, f"File Size: {file.size / 1024:.2f} KB", ln=True)
#             pdf.cell(200, 10, f"Total Rows: {df.shape[0]}", ln=True)
#             pdf.cell(200, 10, f"Total Columns: {df.shape[1]}", ln=True)

#             pdf_output = pdf.output(dest='S').encode('latin1')

#             st.download_button(label="📥 Download PDF Report",
#                             data=pdf_output,
#                             file_name=f"{file.name}_report.pdf",
#                             mime="application/pdf")
            

#             # ✅ File Conversion & Download
#         st.subheader("📂 Convert & Download")
#         conversion_type = st.radio(f"🔄 Convert {file.name} to:", ["CSV", "Excel"])

#         if st.button(f"💾 Download {file.name} as {conversion_type}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False)

#             buffer.seek(0)
#             st.download_button(
#                 label=f"📥 Download {file.name} as {conversion_type}",
#                 data=buffer,
#                 file_name=file.name.replace(file_ext, f".{conversion_type.lower()}"),
#                 mime="text/csv" if conversion_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )


# # ✅ Upload History
# st.subheader("📜 Upload History")
# if st.session_state.file_history:
#     for file_name in list(st.session_state.file_history.keys()):
#         col1, col2 = st.columns([3, 1])
#         col1.write(f"📄 {file_name}")
#         if col2.button(f"❌ Delete", key=f"delete_{file_name}"):
#             del st.session_state.file_history[file_name]
#             st.success(f"🗑 '{file_name}' removed! You can now upload it again.")
#             st.rerun()







import streamlit as st
import pandas as pd
import numpy as np
import os
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")

# ✅ Stylish UI
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
        }
        .sub-title {
            text-align: center;
            font-size: 1.5rem;
            color: white;
        }
        .stButton>button {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            font-size: 1.1rem;
            padding: 10px;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #0072ff, #00c6ff);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ✅ Page Title
st.markdown('<h1 class="main-title">🚀 Data Sweeper</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-title">Transform, Clean & Visualize Your Data Easily!</h2>', unsafe_allow_html=True)

# ✅ Session State for File Management
if "file_history" not in st.session_state:
    st.session_state.file_history = {}

if "undo_stack" not in st.session_state:
    st.session_state.undo_stack = {}

if "redo_stack" not in st.session_state:
    st.session_state.redo_stack = {}

# ✅ Function to Save History
def save_history(file_name, df):
    if file_name not in st.session_state.undo_stack:
        st.session_state.undo_stack[file_name] = []
    st.session_state.undo_stack[file_name].append(df.copy())

# ✅ Function for Undo
def undo(file_name):
    if file_name in st.session_state.undo_stack and len(st.session_state.undo_stack[file_name]) > 1:
        if file_name not in st.session_state.redo_stack:
            st.session_state.redo_stack[file_name] = []
        st.session_state.redo_stack[file_name].append(st.session_state.undo_stack[file_name].pop())
        return st.session_state.undo_stack[file_name][-1]
    return None

# ✅ Function for Redo
def redo(file_name):
    if file_name in st.session_state.redo_stack and st.session_state.redo_stack[file_name]:
        df = st.session_state.redo_stack[file_name].pop()
        st.session_state.undo_stack[file_name].append(df)
        return df
    return None

# ✅ File Upload
uploaded_files = st.file_uploader("📂 Upload CSV or Excel Files:", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file.name in st.session_state.file_history:
            st.warning(f"⚠️ '{file.name}' is already uploaded. Delete it from history first or continue working on it.")
            continue

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        # ✅ Save file in session state
        st.session_state.file_history[file.name] = df
        save_history(file.name, df)

# ✅ Uploaded File List
st.subheader("📜 Upload History")
if st.session_state.file_history:
    for file_name in list(st.session_state.file_history.keys()):
        with st.expander(f"📄 {file_name}"):
            df = st.session_state.file_history[file_name]
            st.write(f"📏 Size: {df.shape[0]} rows x {df.shape[1]} columns")
            st.dataframe(df.head())

            # Undo / Redo
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"↩️ Undo {file_name}", key=f"undo_{file_name}"):
                    new_df = undo(file_name)
                    if new_df is not None:
                        df = new_df  # ✅ Update df only if undo is successful
                        st.success(f"Undo successful for {file_name}!")
                    else:
                        st.warning("⚠️ No more undo steps available.")

            with col2:
                if st.button(f"↪️ Redo {file_name}", key=f"redo_{file_name}"):
                    new_df = redo(file_name)
                    if new_df is not None:
                        df = new_df  # ✅ Update df only if redo is successful
                        st.success(f"Redo successful for {file_name}!")
                    else:
                        st.warning("⚠️ No more redo steps available.")

            # ✅ Ensure df is never None (Prevent AttributeError)
            # if df is not None:
            #     # ✅ Data Visualization
            #     st.subheader("📊 Data Visualization")
            #     numeric_columns = df.select_dtypes(include=np.number).columns

            #     if len(numeric_columns) > 0:
            #         vis_col = st.selectbox("📈 Choose Column for Visualization", numeric_columns)
            #         if vis_col:
            #             st.bar_chart(df[vis_col])
            #     else:
            #         st.warning("⚠️ No numeric columns available for visualization.")

            # ✅ Data Cleaning Options
            st.subheader("🛠 Data Cleaning")
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑 Remove Duplicates from {file_name}"):
                    df.drop_duplicates(inplace=True)
                    st.session_state.file_history[file_name] = df
                    st.success("✅ Duplicates Removed!")
                    st.rerun()

            with col2:
                missing_option = st.selectbox(
                    f"📉 Handle Missing Values ({file_name})",
                    ["None", "Mean", "Median", "Mode"],
                    key=f"missing_{file_name}",
                )
                if missing_option != "None":
                    for col in df.select_dtypes(include=np.number).columns:
                        if missing_option == "Mean":
                            df[col].fillna(df[col].mean(), inplace=True)
                        elif missing_option == "Median":
                            df[col].fillna(df[col].median(), inplace=True)
                        elif missing_option == "Mode":
                            df[col].fillna(df[col].mode()[0], inplace=True)
                    st.session_state.file_history[file_name] = df
                    st.success(f"✅ Missing values filled using {missing_option}!")
                    st.rerun()

            # ✅ Data Visualization
            st.subheader("📊 Data Visualization")
            numeric_columns = df.select_dtypes(include=np.number).columns

            if len(numeric_columns) > 0:
                vis_col = st.selectbox("📈 Choose Column for Visualization", numeric_columns, key=f"vis_{file_name}")
                if vis_col:
                    st.bar_chart(df[vis_col])
            else:
                st.warning("⚠️ No numeric columns available for visualization.")

            # ✅ Generate PDF Report
            st.subheader("📄 Generate PDF Report")
            if st.button(f"📥 Download Report for {file_name}"):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, f"Data Report - {file_name}", ln=True, align="C")
                pdf.cell(200, 10, f"Total Rows: {df.shape[0]}", ln=True)
                pdf.cell(200, 10, f"Total Columns: {df.shape[1]}", ln=True)

                pdf_output = pdf.output(dest="S").encode("latin1")
                st.download_button(
                    label="📥 Download PDF Report",
                    data=pdf_output,
                    file_name=f"{file_name}_report.pdf",
                    mime="application/pdf",
                )

            # ✅ File Conversion & Download
            # ✅ File Conversion & Download
            st.subheader("📂 Convert & Download")
            conversion_type = st.radio(f"🔄 Convert {file_name} to:", ["CSV", "Excel"], key=f"convert_{file_name}")

            if st.button(f"💾 Download {file_name} as {conversion_type}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False)

                buffer.seek(0)
                output_file_name = file_name.rsplit(".", 1)[0] + f".{conversion_type.lower()}"  # ✅ Fixed file name

                st.download_button(
                    label=f"📥 Download {file_name} as {conversion_type}",
                    data=buffer,
                    file_name=output_file_name,  # ✅ Corrected file name
                )


            # ✅ Delete File from History
            if st.button(f"❌ Delete {file_name}", key=f"delete_{file_name}"):
                del st.session_state.file_history[file_name]
                st.success(f"🗑 '{file_name}' removed!")
                st.rerun()
