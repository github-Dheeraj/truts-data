
from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup 
import json

allSyscoinDAO = []
dao_Objects = {
    "chains": ["syscoin"],
    "dao_name" :"",
    "description" : "",
    "dao_category" : [],
    "dao_logo" :"",
    "dao_cover":"",
    "website_link" :"",
    "discord_link" :"",
    "twitter_link" :"",
    "additional_link" :""
}

html_string =""

with open('syscoinData.html', 'r') as f:
    html_string = f.read()

page = html_string

soup = BeautifulSoup(page, "html.parser")

results = soup.find("div", class_="project-container")
projectClass = results.find_all("div" , class_="project")

string_image = "https://syscoin.org/"

for project in projectClass:
    title = project.find("h4")
    print(title.text.strip())
    dao_Objects["dao_name"] = title.text.strip()

    dao_Objects["dao_category"] = project["data-cat"]

    image_sub = project.find("img")
    print(string_image+ image_sub["src"])
    dao_Objects["dao_logo"] = string_image+ image_sub["src"]

    name_sub = project.find("a")
    print(name_sub["href"])
    dao_Objects["website_link"] = name_sub["href"]

    description_sub = project.find("div", class_ ="project-description")
    print(description_sub.text)
    dao_Objects["description"] = description_sub.text

    allSyscoinDAO.append(dao_Objects)
    dao_Objects = {
        "chains": ["syscoin"],
        "dao_name" :"",
        "description" : "",
        "dao_category" : [],
        "dao_logo" :"",
        "dao_cover":"",
        "website_link" :"",
        "discord_link" :"",
        "twitter_link" :"",
        "additional_link" :""
    }

with open("syscoinRawData.json", "w") as file:
    json.dump(allSyscoinDAO,file)