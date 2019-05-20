from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests, sys, json, time, lxml, fpdf

# Grab the algorithms page of LeetCode and wait (2.5 s) for problems 
# to dynamically load using selenium
urlMain = "https://leetcode.com/problemset/algorithms/"
browser = webdriver.Chrome()
browser.implicitly_wait(30)
browser.get(urlMain)
browser.find_element_by_class_name("question-list-table")
browser.find_element_by_xpath("//*[@id='question-app']/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select/option[@value='9007199254740991']").click()
# 
# Use BeautifulSoup4 to extract HTML source code for 
# links to each question and intialize array to store them
soup = BeautifulSoup(browser.page_source, 'lxml')
questionsList = soup.find_all('tbody', class_='reactable-data')
questionLinks = []

# with open('scrape.txt', 'w', encoding='utf-8') as file:
#     # file.write(text)
#     # file.write(element.text)
#     file.write(soup.prettify())
pdf = fpdf.FPDF(format='letter')
for q in questionsList:
    for a in q.find_all('a', href=lambda href: href and "/problem" in href):
		# print(a['href'])
        if a.next_sibling.next_sibling:
            continue
        else:
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            questionLinks.append(a['href'])
            pdf.write(5, a['href'])

# file=open('testfile.txt','w', encoding='utf-8') 
# pdf = fpdf.FPDF(format='letter')
# for urlQuestion in questionLinks:
#     # print(urlQuestion)
#     browser.implicitly_wait(30)
#     browser.get("https://leetcode.com/" + urlQuestion)
#     if browser.find_element_by_class_name("content__u3I1"):
#             continue
#     browser.find_element_by_class_name("content__u3I1")
#     soup_level2 = BeautifulSoup(browser.page_source, 'lxml')
#     question = soup_level2.find_all('div', class_='content__u3I1')
#     for qst in question:
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)
#         pdf.write(5, qst.text)
#         # print(qst.text)
#         # file.write(qst.text)

# # file.close()
pdf.output("testings.pdf")


browser.quit()
