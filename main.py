from src.scraper import get_html_data

url = 'https://realpython.github.io/fake-jobs/'

html_elements = get_html_data(url)

print(html_elements)