import streamlit as st
from run import run
import base64
def main():
    original_title = '<p style="font-family:Consolas; color:Black; font-size: 50px;"><b>Automatic Email Attachment Extractor</b></p>'
    st.markdown(original_title, unsafe_allow_html=True)
    run()
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
set_png_as_page_bg('background.png')
if __name__ == '__main__':
    main()
    