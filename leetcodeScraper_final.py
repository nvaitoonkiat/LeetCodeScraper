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

# Use BeautifulSoup4 to extract HTML source code for 
# links to each question and intialize array to store them 
soup = BeautifulSoup(browser.page_source, 'lxml')
questionsList = soup.find_all('tbody', class_='reactable-data')
questionLinks = []


for q in questionsList:
    for a in q.find_all('a', href=lambda href: href and "/problem" in href):
        if a.next_sibling.next_sibling:
            continue
        else:
            questionLinks.append(a['href'])


# Prints questions out into a blank pdf page. On every 50 questions, open and write to a new file.
pdf = fpdf.FPDF(format='letter')
pdf.add_font('Arial', '', 'C:\Windows\Fonts\Arial.ttf', uni=True)
pdf.set_font('Arial', '', 12)
startNum=1
endNum=50

for urlQuestion in questionLinks:
    if startNum > endNum:
        pdf.output("LC-Questions_" + str(startNum) + "-" + str(endNum) + ".pdf")
        pdf = fpdf.FPDF(format='letter')
        pdf.add_font('Arial', '', 'C:\Windows\Fonts\Arial.ttf', uni=True)
        pdf.set_font('Arial', '', 12)
        endNum += 50
    print(urlQuestion)
    browser.implicitly_wait(30)
    browser.get("https://leetcode.com/" + urlQuestion)
    browser.find_element_by_class_name("content__u3I1")
    soup_level2 = BeautifulSoup(browser.page_source, 'lxml')
    question = soup_level2.find_all('div', class_='content__u3I1')
    title = soup_level2.find(id='question-title')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(5, title.text)
    pdf.ln()
    pdf.ln()
    for qst in question:
        pdf.write(5, qst.text)
    startNum += 1
pdf.output("LC-Questions_" + startNum + "-" + endNum + ".pdf")

# Exit program
browser.quit()
