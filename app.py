import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_card import card
from PIL import Image
import API
import json
import random


image = Image.open('media/app_logo.png')

st.image(image, use_column_width=True)

menu = option_menu(None, ["Collaborate", "Jobs"],
                   icons=['code-square', 'clipboard-fill'], menu_icon="cast", default_index=0,
                   orientation="horizontal", key="menu")

selection = st.session_state.menu
if selection and selection == "Jobs":
    uploaded_file = st.file_uploader(
        "Upload your Resume", accept_multiple_files=False)
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
else:
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

        licenses.append(mit)
        licenses.append(apache)
        licenses.append(gpl_2)
        licenses.append(gpl_3)
        licenses.append(bsd)

# Button
send = st.button('Get recommendations', use_container_width=True)
if send:
    data = {"languages": languages, "licenses": licenses, "topics": topics}

    """
    recommendations = API.get_collaboration_recommendations(data)
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        colors_api = "https://singlecolorimage.com/get/33fd8f/400x100"
        colors = ["#f94144", "#f3722c", "#f8961e", "#f9844a", "#f9c74f", "#90be6d", "#43aa8b", "#4d908e", "#577590", "#277da1"]

        response = json.loads(recommendations)
        for obj in response:
            repo = response[obj]
            st_card(
                title = repo["repository_name"],
                image = f"https://singlecolorimage.com/get/{random.choice(colors)}/125x125",
                url = f"https://github.com/{repo['repository_name']}",
            )
    """

    recommendations = json.dumps(
        {
            "0": [
                {"repository_name": "krahets/hello-algo", "watchers_count": 100},
            ],
            "1": [
                {"repository_name": "rasbt/python-machine-learning-book",
                    "watchers_count": 500},
            ],
            "2": [
                {"repository_name": "krahets/hello-algo", "watchers_count": 100},
            ],
            "3": [
                {"repository_name": "rasbt/python-machine-learning-book",
                    "watchers_count": 500},
            ],
            "4": [
                {"repository_name": "krahets/hello-algo", "watchers_count": 100},
            ],
            "5": [
                {"repository_name": "rasbt/python-machine-learning-book",
                    "watchers_count": 500},
            ],
            "6": [
                {"repository_name": "krahets/hello-algo", "watchers_count": 100},
            ],
            "7": [
                {"repository_name": "rasbt/python-machine-learning-book",
                    "watchers_count": 500},
            ],
            "8": [
                {"repository_name": "krahets/hello-algo", "watchers_count": 100},
            ],
            "9": [
                {"repository_name": "rasbt/python-machine-learning-book",
                    "watchers_count": 500},
            ],
            "10": [
                {"repository_name": "krahets/hello-algo", "watchers_count": 100},
            ],
        }
    )

    if recommendations:
        colors = ["f94144", "f3722c", "f8961e", "f9844a", "f9c74f",
                  "90be6d", "43aa8b", "4d908e", "577590", "277da1"]

        response = json.loads(recommendations)
        col1, col2 = st.columns(2)
        for i, obj in enumerate(response):
            repo = response[obj][0]
            
            if i in range(0, 6):
                with col1:
                    card(
                        title = repo["repository_name"],
                        text = f"{repo['watchers_count']} watchers",
                        image = f"https://singlecolorimage.com/get/{random.choice(colors)}/1x1",
                        url = f"https://github.com/{repo['repository_name']}",
                        key=str(i),
                    )
            else:
                with col2:
                    card(
                        title = repo["repository_name"],
                        text = f"{repo['watchers_count']} watchers",
                        image = f"https://singlecolorimage.com/get/{random.choice(colors)}/1x1",
                        url = f"https://github.com/{repo['repository_name']}",
                        key=str(i),
                    )