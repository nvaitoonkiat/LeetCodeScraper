from bs4 import BeautifulSoup
import requests
import json
str = "two-sum"
source = requests.get('https://leetcode.com/problems/' + str + '/').text
apisource = requests.get('https://leetcode.com/api/problems/all/')
# r = apisource.json()
# listOfQuestionNames=list()
# file=open('testfile.txt','w', encoding='utf-8') 
# r["stat_status_pairs"].reverse()
# for question in r["stat_status_pairs"]:
#     listOfQuestionNames.append(question["stat"]["question__title_slug"])
#     file.write(question["stat"]["question__title_slug"])
#     file.write("\n")
# file.close()


soup = BeautifulSoup(source, 'lxml')
text = soup.prettify()
file=open('testfile.txt','w', encoding='utf-8') 
file.write(text)

# question = soup.find_all('div', class_="assess-bar")
# question = soup.find_all('tbody', class_='reactable-data')
# newDictionary=json.loads(str(soup))
# text = soup.prettify()
# file.write(text) 
# file.write(newDictionary) 
# file=open('testfile.txt','w', encoding='utf-8') 
# text = apisource
# file.write(text)