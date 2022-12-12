from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup as bs
import json

allResources = []
URL = 'https://university.polygon.technology/'
  
dao_Objects = {
    "title": "",
    "description": "",
    "resource_link": "",
    "tags": ["tutorials"],
    
}

req = requests.get(URL  )
# print(req.text)
soup = bs(req.text, 'html.parser')

containers = soup.find_all('div',class_="css-1ahj0ux")
for container in containers:
    base_classes = container.find_all('div',class_="css-v1ls2g")
    for mainclass in base_classes:
        maincalss = mainclass.find('div',class_="css-rmlqu9")
        headingClass = maincalss.find('h4',class_="css-wmy2fu")
        print(headingClass.text)
        dao_Objects["title"] = headingClass.text
        descClass = maincalss.find('div',class_="css-1eyj61a")
        print(descClass.text)
        dao_Objects["description"] = descClass.text
        allResources.append(dao_Objects)

        dao_Objects = {
            "title": "",
            "description": "",
            "resource_link": "",
            "tags": ["tutorials"],
        }


with open("PolygonAcademy.json", "w") as file:
    json.dump(allResources, file)