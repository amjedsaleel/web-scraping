import requests
from bs4 import BeautifulSoup

url = 'https://www.passiton.com/inspirational-quotes'
page = requests.get(url)
page_content = BeautifulSoup(page.content, 'html.parser')

items = page_content.find(class_='container')
# print(items)

sub_items = page_content.find_all('div', class_='col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top')
# print(sub_items[0])

for div in page_content.find_all('div', class_='col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'):
    # print(div)
    for img in div.find_all('img'):
        # print(img)
        quotes = [img['alt']]
        print(quotes)
