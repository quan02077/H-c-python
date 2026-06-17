import requests
from bs4 import BeautifulSoup

# URL của trang web cần phân tích
url = 'https://toidicodedao.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print('Failed to load the website')

# Tìm tất cả các phần tử có thẻ <a>
h1_tags = soup.find_all('h1')

# Trích xuất liên kết và nội dung của các phần tử <a>
for h1_tag in h1_tags:
    link = h1_tag.get('href')
    text = h1_tag.text
    print(link, text)
