import streamlit as st
from pre_process import pre_process

# Configure layout of page, must be first streamlit call in script
st.set_page_config(layout="wide")

uploaded_file = st.file_uploader("Upload last month MR")

downloaded = False

if uploaded_file:
    new_mr, new_name = pre_process(uploaded_file)
    st.write("Thanks for uploading, now you can download the new MR")
    downloaded = st.download_button(
        label="Download", data=new_mr.getvalue(), file_name=new_name
    )

if downloaded:
    st.write("File Downloaded!")
