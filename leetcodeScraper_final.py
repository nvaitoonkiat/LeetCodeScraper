from bs4 import BeautifulSoup
from selenium import webdriver
import requests, sys, json, time, lxml


url = "https://leetcode.com/problemset/algorithms/"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)
soup = BeautifulSoup(browser.page_source, 'lxml')
# text = soup.prettify()
test = soup.find_all('tbody', class_='reactable-data')
for tr in test:
    for a in tr.find_all('a', href = True):
        print(a['href'])
    # for a in tr:
    #     print(a.text)

# with open('scrape.txt', 'w', encoding='utf-8') as file:
#     # file.write(text)
#     # file.write(element.text)
#     file.write(str(test))

browser.quit()