import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

image = Image.open('media/app_logo.png')

st.image(image, use_column_width=True)

menu = option_menu(None, ["Jobs", "Collaborate"], 
    icons=['clipboard-fill', 'code-square'], menu_icon="cast", default_index=0,
    orientation="horizontal", key="menu")

selection = st.session_state.menu
if selection and selection == "Collaborate":
    # Title 
    st.subheader("What topic(s) are you interested in? (Machine Learning, Medicine, etc.)")
    # Taking user input
    user_input = st.text_input("Write your topic(s) of interest separated by a comma:")
    # Displaying user input
    if user_input:
        st.write(f'You typed: {user_input}')

    # Title
    st.subheader("What language(s) would you like to use?")
    # Taking user input
    user_input = st.text_input("Write your language(s) of interest separated by a comma:")
    # Displaying user input
    if user_input:
        st.write(f'You typed: {user_input}')

    # Toggle
    on = st.toggle('Advanced Search')
    if on:
        # Title
        st.subheader("What type of license do you prefer?")
        # Create two columns
        col1, col2 = st.columns(2)
        # Place checkboxes in the columns
        mit = col1.checkbox('MIT')
        apache = col1.checkbox('Apache-2.0')
        gpl_2 = col1.checkbox('GPL-2.0')
        gpl_3 = col2.checkbox('GPL-3.0')
        bsd = col2.checkbox('BSD-3-clause')


else:
    uploaded_file = st.file_uploader("Upload your Resume", accept_multiple_files=False)
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)




