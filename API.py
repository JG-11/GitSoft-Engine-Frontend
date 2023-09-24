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

    payload = {
        'languages': languages,
        'licenses': licenses,
        'topics': topics,
    }

    try:
        requests.post(BASE_URL, data=payload)
    except Exception as e:
        return 'Please try again. An error has occurred' 
    
    return None


def parse_recommendations():
    """
        {
            0: {
                "repository_name": "",
                "similarity_score": 10,
                "watchers_count": 100,
            },
            1: {
                "repository_name": "",
                "similarity_score": 15,
                "watchers_count": 500,
            }
        }
    """
    response = requests.get(BASE_URL)

    return response.json()
