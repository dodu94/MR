import streamlit as st
from utils.pre_process import pre_process
from utils.process_extmytime import process_extmytime

# Configure layout of page, must be first streamlit call in script
st.set_page_config(layout="wide")

# add a button for the extmytime process
text = st.text_area("Copy your Extmytime here")
if text:
    total_hours, tasks_hours, message = process_extmytime(text)
    if message == "":
        st.write("Total hours:", total_hours)
        st.write("Tasks hours:", tasks_hours)
    else:
        st.write(message)

if text and message == "":
    uploaded_file = st.file_uploader("Upload last month MR")

    downloaded = False

    if uploaded_file:
        new_mr, new_name = pre_process(uploaded_file, tasks_hours, total_hours)
        st.write("Thanks for uploading, now you can download the new MR")
        downloaded = st.download_button(
            label="Download", data=new_mr.getvalue(), file_name=new_name
        )

    if downloaded:
        st.write("File Downloaded!")
