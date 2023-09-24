import streamlit as st
import requests

BASE_URL = 'https://meowfacts.herokuapp.com/'

def parse_text_input(text):
    arr = text.split(',')
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
    
    return arr

def get_collaboration_recommendations(data):
    """
        {
            "languages": [Java, Python, C++, JavaScript],
            "licenses": [MIT, Apache, GPL],
            "topics": [Computer Science, Medicine],
        }
    """

    languages = parse_text_input(data.languages)
    
    licenses = []
    for opt in data.licenses:
        if opt:
            licenses.append(opt)

    topics = parse_text_input(data.topics)

    query = f"""
        - Programming languages: {languages}
        - Licenses: {licenses}
        - Content: {topics}
    """

    try:
        response = requests.post(BASE_URL, data=query)
        response = response.json()

        """
        {
            0: {
                "repository_name": "",
                "watchers_count": 100,
            },
            1: {
                "repository_name": "",
                "watchers_count": 500,
            }
        }
        """
    except Exception as e:
        st.error('Please try again. An error has occurred')

        return None
    
    return response
