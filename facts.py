import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.factmonster.com/dayinhistory')
page = page.text
soup = BeautifulSoup(page, 'lxml')


for i in range(6):
    year = soup.find_all('h3')[i].text
    data = soup.find_all('p')[i].text
    fact = "On this day, in" + year + "," + data
    print(fact)