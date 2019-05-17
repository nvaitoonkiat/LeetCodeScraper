from bs4 import BeautifulSoup
from selenium import webdriver
import requests, sys, json, time, lxml

# Grab the algorithms page of LeetCode and wait (2.5 s) for problems 
# to dynamically load using selenium
urlMain = "https://leetcode.com/problems/two-sum/"
browser = webdriver.Chrome()
browser.get(urlMain)
time.sleep(2.5)

# Use BeautifulSoup4 to extract HTML source code for 
# links to each question and intialize array to store them
soup = BeautifulSoup(browser.page_source, 'lxml')
questionsList = soup.find_all('tbody', class_='reactable-data')
questionLinks = []

for q in questionsList:
    for a in q.find_all('a', href = lambda href: href and "/problem" in href):
        # print(a['href'])
        questionLinks.append(a['href'])

for urlQuestion in questionLinks:
    # print(urlQuestion)
    browser2 = webdriver.Chrome()
    browser2.get("https://leetcode.com/" + urlQuestion)
    time.sleep(5)
    soup_level2 = BeautifulSoup(browser.page_source, 'lxml')
    question = soup_level2.find_all('div', class_='content__u3I1')
    print(question)
    # print(question.text)
    browser2.close()
    


# with open('scrape.txt', 'w', encoding='utf-8') as file:
#     # file.write(text)
#     # file.write(element.text)
#     file.write(str(test))

browser.quit()