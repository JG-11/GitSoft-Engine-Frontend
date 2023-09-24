import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_card import card
from PIL import Image
import API
import random
import pandas as pd

CARDS_COLORS = ["f94144", "f3722c", "f8961e", "f9844a", "f9c74f",
                "90be6d", "43aa8b", "4d908e", "577590", "277da1"]


image = Image.open('media/app_logo.png')

st.image(image, use_column_width=True)

menu = option_menu(None, ["Collaborate", "Jobs", "Example Data"],
                   icons=['code-square', 'clipboard-fill', 'eye'], menu_icon="cast", default_index=0,
                   orientation="horizontal", key="menu")

selection = st.session_state.menu
if selection and selection == "Jobs":
    uploaded_file = st.file_uploader(
        "Upload your Resume", accept_multiple_files=False)
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
    
    send = st.button('Get recommendations', use_container_width=True)
elif selection is None or selection == "Collaborate":
    # Title
    st.subheader(
        "What topic(s) are you interested in? (Machine Learning, Medicine, etc.)")
    # Taking user input
    topics = st.text_input(
        "Write your topic(s) of interest separated by a comma:")

    # Title
    st.subheader("What language(s) would you like to use?")
    # Taking user input
    languages = st.text_input(
        "Write your language(s) of interest separated by a comma:")

    # Toggle
    on = st.toggle('Advanced Search')
    licenses = []
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

        licenses.append("mit" if mit else None)
        licenses.append("apache-2.0" if apache else None)
        licenses.append("GPL-2.0" if gpl_2 else None)
        licenses.append("GPL-3.0" if gpl_3 else None)
        licenses.append("BSD-3-clause" if bsd else None)
    
    send = st.button('Get recommendations', use_container_width=True)
else:
    df = pd.read_csv('data/github_repos_dataset.csv')

    st.dataframe(df, hide_index=True)

    send = None

if send:
    data = {"languages": languages, "licenses": licenses, "topics": topics}

    with st.spinner('Generating recommendations...'):
        recommendations = API.get_collaboration_recommendations(data)

    if recommendations:
        st.info(recommendations['output_string']['message']['content'], icon="ℹ️")

        total_repos = len(recommendations['watchers'])
        if total_repos > 0:
            st.subheader(f'_Grid of the :red[{total_repos} recommended] repositories_', divider='red')
        
        col1, col2 = st.columns(2)
        for i in range(total_repos):
            if i in range(0, total_repos // 2):
                with col1:
                    card(
                        title = recommendations["reponame"][i],
                        text = f"{recommendations['watchers'][i]} watchers",
                        image = f"https://singlecolorimage.com/get/{random.choice(CARDS_COLORS)}/1x1",
                        url = f"https://github.com/search?q={recommendations['reponame'][i]}+in:name",
                        key=str(i),
                    )
            else:
                with col2:
                    card(
                        title = recommendations["reponame"][i],
                        text = f"{recommendations['watchers'][i]} watchers",
                        image = f"https://singlecolorimage.com/get/{random.choice(CARDS_COLORS)}/1x1",
                        url = f"https://github.com/search?q={recommendations['reponame'][i]}+in:name",
                        key=str(i),
                    )