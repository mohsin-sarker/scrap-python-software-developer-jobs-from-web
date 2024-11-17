import requests
from bs4 import BeautifulSoup


def get_response(url): 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        raise Exception
    except:
        return f'An error has been ocurred with status_code: {response.status_code}'
    

def get_card_contents(url, class_name):
    contents = get_response(url)
    card_contents = contents.find_all('div', class_ = class_name)
    return card_contents