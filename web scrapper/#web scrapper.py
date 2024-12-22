#web scrapper
import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
wrapper = soup.find_all(class_="quote")
for wrap in wrapper:
    print(wrap.find("span").text)
    