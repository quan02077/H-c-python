from bs4 import BeautifulSoup
import requests

url = 'https://toidicodedao.com/'

reponse = requests.get(url)

if reponse.status_code == 200:
    print("Successfully accessed the webpage.")
    soup = BeautifulSoup(reponse.text, 'html.parser')
else:
    print("Failed to access the webpage. Status code:", reponse.status_code)

p_tag = soup.find('p')

p_content = p_tag.text
print(p_content)