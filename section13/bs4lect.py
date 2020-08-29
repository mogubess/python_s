from bs4 import BeautifulSoup
import requests


html = requests.get('https://www.python.org')

soup = BeautifulSoup(html.text, 'html.parser')

titles = soup.find_all('title')
print(titles)

intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)
