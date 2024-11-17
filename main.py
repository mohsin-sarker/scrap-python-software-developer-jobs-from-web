from src.contents import (
                                get_response,
                                get_card_contents
                            )   

url = 'https://realpython.github.io/fake-jobs/'

contents = get_card_contents(url, 'card-content')

# Find python jobs only
for content in contents:
    title = content.find('h2', class_ = 'title')
    company = content.find('h3', class_ = 'company')
    location = content.find('p', class_ = 'location')
    if content.find('h2', string = lambda text: 'python' in text.lower()):
        print(f'Job Title: {title.text.strip()}')
        print(f'Company: {company.text.strip()}')
        print(f'Location: {location.text.strip()}')
        print(end='\n' * 2)
        
        