import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import wget

ua = UserAgent()

r = requests.get("https://britlex.ru/dictionary.php", headers={'User-Agent': ua.random})
soup = BeautifulSoup(r.content, "html.parser")
# print(soup.find_all('div', class_='word'))
# print(soup)
