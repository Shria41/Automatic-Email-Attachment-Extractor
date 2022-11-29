import streamlit as st
import pandas as pd
from database import check,add_data,runp,delete_data
def run():
    tabs_font_css = """
    <style>
    div[class*="stTextArea"] label {
    font-size: 15px;
    color: black;
    }

    div[class*="stTextInput"] label {
    font-size: 30px;
    color: black;
    font-family:Consolas;

    div[class*="stcheckbox"] label {
    font-size: 30px;
    color: black;
    font-family:Consolas;
    }
    </style>
    """
    st.write(tabs_font_css, unsafe_allow_html=True)
    uname=st.text_input("Enter username: ")
    if st.checkbox('Check'):
        passw=check(uname)
        #st.success(passw)
        if(passw):
            st.success("Present in the database")
        else:
            st.success("Not present in the database")
            passw=st.text_input("Enter password: ")
            if st.button('Add'):
                add_data(uname,passw)
    if st.button("Run"):
        if(uname!="" and passw!=""):
            runp(uname,passw)
        else:
            st.success('Cannot run without respective username and password!')

    if st.button("Delete information"):
        if(uname!="" and passw!=""):
            delete_data(uname)
            st.success('Successful delete')
        else:
            st.success('Cannot delete without entering username and password!')

    