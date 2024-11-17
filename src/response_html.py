import requests


def get_html_data(url): 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except:
        return f'An error has been ocurred with status_code: {response.status_code}'
    
