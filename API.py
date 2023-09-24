import streamlit as st
import requests
import json

BASE_URL = 'http://20.225.244.87:8000'

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

    languages = parse_text_input(data['languages'])
    
    licenses = []
    for opt in data['licenses']:
        if opt:
            licenses.append(opt)

    topics = parse_text_input(data['topics'])

    if len(licenses) > 0:
        # Advanced search
        query = f"""
            - Programming languages: {languages}
            - Licenses: {licenses}
            - Content: {topics}
        """
    else:
        query = f"""
            - Programming languages: {languages}
            - Content: {topics}
        """

    try:
        response = requests.get(BASE_URL + '/process_string/?input_string=' + query)
        response = response.content.decode('utf-8')
        response = json.loads(response)
    except Exception as e:
        st.error('Please try again. An error has occurred', icon='🚨')

        return None
    
    return response