from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import sys
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl
# from PyQt4.QtWebKit import QWebPage
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QUrl
import json
# Installation Guide:
# first install BeautifulSoup, requests, and lxml, qt4
# for qt4: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4
# for qt5: pip install PyQt5 and pip install PyQtWebEngine

# class Client(QWebPage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebPage.__init__(self)
#         self.loadFinished.connect(self.on_page_load)
#         self.mainFrame().load(QUrl(url))
#         self.app.exec_()
    
#     def on_page_load(self):
#         self.app.quit()
# class Page(QWebEnginePage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebEnginePage.__init__(self)
#         self.html = ''
#         self.loadFinished.connect(self._on_load_finished)
#         self.load(QUrl(url))
#         self.app.exec_()

#     def _on_load_finished(self):
#         self.html = self.toHtml(self.Callable)
#         print('Load finished')

#     def Callable(self, html_str):
#         self.html = html_str
#         self.app.quit()

# url = 'https://leetcode.com/problemset/algorithms/'
# client_response = Client(url)
# source1 = client_response.mainFrame().toHtml()
# soupy = BeautifulSoup(source1, 'lxml')
# page = Page(url)
# soupy = BeautifulSoup(page.html, 'lxml')
# js_test = soupy.find('p', class_='jstest')
# print(js_test)

chrome_path = r"C:\Users\vaitnx\Documents\GitHub\LeetCodeScraper\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

soupsource= driver.get("https://leetcode.com/problemset/algorithms/")
soup = BeautifulSoup(soupsource, 'lxml')
review = driver.find_element_by_xpath("//div[@id='question-app']")
print(soup.text)
# review = driver.find_elements_by_class_name("question-list-table")
# for post in review: 
#     print(post.text)

# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)
#     print('YES')


# str = "two-sum"
# source = requests.get('https://leetcode.com/problems/' + str + '/').text
# apisource = requests.get('https://leetcode.com/api/problems/all/')
# soup = BeautifulSoup(source, 'lxml')
# text = soup.prettify()
# file=open('testfile.txt','w', encoding='utf-8') 
# file.write(text)



# r = apisource.json()
# listOfQuestionNames=list()
# file=open('testfile.txt','w', encoding='utf-8') 
# r["stat_status_pairs"].reverse()
# for question in r["stat_status_pairs"]:
#     listOfQuestionNames.append(question["stat"]["question__title_slug"])
#     file.write(question["stat"]["question__title_slug"])
#     file.write("\n")
# file.close()
# question = soup.find_all('div', class_="assess-bar")
# question = soup.find_all('tbody', class_='reactable-data')
# newDictionary=json.loads(str(soup))
# text = soup.prettify()
# file.write(text) 
# file.write(newDictionary) 
# file=open('testfile.txt','w', encoding='utf-8') 
# text = apisource
# file.write(text)
