from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup as bs
import json

allPolygonDAO = []
URL = 'https://polygon.technology/ecosystem/'
  
dao_Objects = {
    "chains": ["polygon"],
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

for page in range(1,1639):
      # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example

   
    req = requests.get(URL + str(page) )
    # print(req.text)
    soup = bs(req.text, 'html.parser')

    containers = soup.find_all('div',class_="ecosystemWrap_RsruN")

    for container in containers:
        try:

            base_class = container.find('div',class_="logo_woz0y")
            image_link = base_class.find_all("img")
            for img in image_link:
                image_ = img["src"]
                # print(image_)
                dao_Objects["dao_logo"] = image_
        except:
            continue

        try:

            getDesc = container.find('p')
            dao_Objects["description"] = getDesc.text
            # print(getDesc.text)
        except:
            continue
        try:

            getName = container.find('h1')
            dao_Objects["dao_name"] = getName.text
            # print(getName.text)
        except:
            continue

        try:
            getTwitterLink = container.find('a')
            twitter_ = getTwitterLink["href"]
            dao_Objects["twitter_link"] = twitter_
            print(page,twitter_)
        except:
            continue
    

        allPolygonDAO.append(dao_Objects)

        dao_Objects = {
            "chains": ["polygon"],
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


with open("PolygonRawdata.json", "w") as file:
    json.dump(allPolygonDAO, file)