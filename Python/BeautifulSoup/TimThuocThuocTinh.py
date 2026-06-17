from bs4 import BeautifulSoup
import requests

url = 'https://tuoitre.vn/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print('Failed to load the website')

content_tag = soup.find_all(class_= 'section__middle-news')

for content in content_tag:
    text = content.text
    print(text)