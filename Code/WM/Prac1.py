!python -m pip install kora -q

import csv
from bs4 import BeautifulSoup
from kora.selenium import wd
wd.get('https://www.amazon.in/')
wd.page_source

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=options)
wd.get("https://www.amazon.in/")
print(wd.page_source) # results

def get_url(search_term):
  template = "https://www.amazon.in/s?k={}&rh=n%3A1389401031&ref=nb_sb_noss"
  search_term = search_term.replace(' ','+')
  return template.format(search_term)
url = get_url('laptops')
print(url)

wd.get(url)
soup = BeautifulSoup(wd.page_source, 'html.parser')
result = soup.find_all('div',{'data-component-type':'s-search-result'})
len(result)
print(result[2])


item = result[2]
atag = item.h2.a
atag.text


price_parent = item.find('span','a-price')
price_parent.find('span','a-offscreen').text


rating = item.i.text
print(rating)


review_count = item.find('span', {'class':'a-size-base','dir':'auto'})
print(review_count)


def extract_record(item1):
  atag = item1.h2.a
  description = atag.text.strip()
  url = "https://www.amazon.in/" + atag.get('href')
  price_parent = item1.find('span','a-price')
  #price_parent.find('span','a-offscreen').text
  rating = ""
  result = (description, price_parent, rating)
  return result


url = get_url('mouse')
wd.get(url)
soup = BeautifulSoup(wd.page_source, 'html.parser')
records = []
results = soup.find_all('div',{'data-component-type':'s-search-result'})


for item in results:
  records.append(extract_record(item))
records[0]
print("printing records")
for x in range(len(records)):
  print(records[x])
