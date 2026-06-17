from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text, "html.parser")

quo = soup.find_all("span", class_= "text")[5].text
auth = soup.find_all("small", class_= "author")[5].text

print(f"{quo} - {auth}")