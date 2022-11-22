

from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup 
import json

allCosmosDAO = []
URL = 'https://cosmos.network/ecosystem/wallets/'
dao_Objects = {
    "chains": ["cosmos"],
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

with open('cosmosWallet.html', 'r') as f:
    html_string = f.read()


page = html_string

soup = BeautifulSoup(page, "html.parser")

results = soup.find_all("div", class_="card-items")

for result in results:
    dao_elements = result.find_all("div", class_="item")
    for dao in dao_elements:
        website = dao.find("a")
        print(website["href"])
        dao_Objects["website_link"] = website["href"]

        image = website.find("img")
        image_url = image["src"]
        dao_Objects["dao_logo"] = image_url
        print(image_url)

        class_text = dao.find("div", class_="text")
        name = class_text.find("a")
        print(name.text)
        dao_Objects["dao_name"] = name.text.strip()

        categorie_text = class_text.find("div", class_="tm-muted")
        category = categorie_text.text.strip()
        dao_Objects["dao_category"].append("wallet")
        print(category)


        text_list = class_text.find("div", class_="text__list")
        links = text_list.find_all("a")
        for link in links:
            link_url = link["href"]
            if "twitter" in link_url:
                dao_Objects["twitter_link"] =link_url
            if "discord" in link_url:
                dao_Objects["discord_link"] =link_url
            if  "github" in link_url:
                dao_Objects["additional_link"] =link_url
            
                
        allCosmosDAO.append(dao_Objects)

        dao_Objects = {
            "chains": ["cosmos"],
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

with open("cosmosWalletdata.json", "w") as file:
    json.dump(allCosmosDAO,file)