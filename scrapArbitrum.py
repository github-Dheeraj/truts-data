from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup
import json

tempLinks = []
allDaoData = []
dao_Objects = {
    "chains": ["arbitrum"],
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

with open('pages.html', 'r') as f:
    html_string = f.read()


page = html_string

soup = BeautifulSoup(page, "html.parser")
results = soup.find("div", class_="client-boxes")

dao_elements = results.find_all("div", class_="client-box-out")


for dao_element in dao_elements:
  
    client_box = dao_element.find("div", class_="client-box")
    cover_box = client_box.find("div", class_="cover-box")
    # image_link = client_box.find_all("div", string="data-src")
    text_box = client_box.find("div", class_="text-box")

    # get website link
    floating_icon = text_box.find("div", class_="client-pic")
    main_links = floating_icon.find_all("a")
    for link in main_links:
        link_url = link["href"]
        dao_Objects["website_link"] = link_url
        # print(link_link)
        image_link = link.find_all("img")
        for img in image_link:
            image_link = img["src"]
            dao_Objects["dao_logo"] = image_link
            # print(image_link)

    text_box_in = text_box.find("div", class_="text-box-in")
    get_title = text_box_in.find("h4")
    # print(get_title.text)
    dao_Objects["dao_name"] = get_title.text
    get_category = text_box_in.find("p")
    # print(get_category.text)
    dao_Objects["dao_category"] = [get_category.text]


    socials = text_box_in.find("div", class_="socials")
    links = socials.find_all("a")
    for link in links:
        link_url = link["href"]
        tempLinks.append(link_url)
        if "twitter" in link_url:
            dao_Objects["twitter_link"] =link_url
        if "discord" in link_url:
            dao_Objects["discord_link"] =link_url
        if  "github" in link_url:
            dao_Objects["additional_link"] =link_url
            
        # print(link_link)

    # try:
    #     if tempLinks[0] !="":
    #         dao_Objects["discord_link"] =tempLinks[0]
        
    # except:
    #     pass

    # try:
    #     if tempLinks[1] !="":
    #         dao_Objects["twitter_link"] =tempLinks[1]
    # except:
    #     pass

    # try:
    #     if tempLinks[2] != "":
    #         dao_Objects["additional_link"] =tempLinks[2]
    # except:
    #     pass


    allDaoData.append(dao_Objects)
    tempLinks.clear()
    dao_Objects = {
        "chains": ["arbitrum"],
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
    

with open("arbitrumData.json", "w") as file:
    json.dump(allDaoData, file)