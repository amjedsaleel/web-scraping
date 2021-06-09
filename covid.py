import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
s = BeautifulSoup(response.content, 'html.parser')

data = s.find_all('div', class_='maincounter-number')
total_cases = data[0].get_text().strip()
total_deaths = data[1].get_text().strip()
recovered = data[2].get_text().strip()

print('Total Cases: ', total_cases)
print('Total deaths: ', total_deaths)
print('Recovered: ', recovered)
