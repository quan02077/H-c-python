from bs4 import BeautifulSoup
import requests

url = 'https://toidicodedao.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print('Failed to load the website')

section_tags = soup.select('#top-posts-3.widget_top-posts')

for section in section_tags:
    text = section.text
    print(text)

