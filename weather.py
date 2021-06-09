import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://forecast.weather.gov/MapClick.php?lat=41.884250000000065&lon=-87.63244999999995#.YMCbiZozZH7'
page = requests.get(url)
page_content = BeautifulSoup(page.content, 'html.parser')

weak = page_content.find(id='seven-day-forecast-list')
items = page_content.find_all('div', class_='tombstone-container')
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_name = [item.find(class_='period-name').get_text() for item in items]
print(period_name)

short_desc = [item.find(class_='short-desc').get_text() for item in items]
print(short_desc)

temp = [item.find(class_='temp').get_text() for item in items]
print(temp)
