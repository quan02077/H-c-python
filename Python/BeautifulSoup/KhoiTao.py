from bs4 import BeautifulSoup
import requests

url = 'https://sinhvien.huit.edu.vn/dashboard.html'

page = requests.get(url)


if requests.get(url).status_code == 200:
    print("Successfully accessed the webpage.")
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.prettify())
else:
    print("Failed to access the webpage. Status code:", requests.get(url).status_code)