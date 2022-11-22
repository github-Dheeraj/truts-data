from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup
import json

# completeData = []
# for index in range(0, 62):
#     print(index)
#     response = requests.get("https://solana.com/api/projects/getpage?page={}&tf=3".format(index))
#     data = response.json()
#     saveData = data["resultingProjects"]
#     for proj in saveData:
#         # print(proj)
#         completeData.append(proj)
  

# with open("delete.json", "w") as file:
#     json.dump(completeData, file)
solanaRawData = []
allDaoData = []
dao_Objects = {
    "chains": ["solana"],
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
logo_slug = "https://solana.com"
with open("SolanaRawData.json", "r") as file:
    data = json.load(file)
    solanaRawData = data

for dao in solanaRawData:
    dao_Objects["dao_name"] = dao['frontmatter']['title']
    dao_Objects["description"] = dao['frontmatter']['logline']

    categoryString = dao['frontmatter']['category']
    dao_Objects["dao_category"] = categoryString.split(",")
    dao_Objects["dao_logo"] = logo_slug + dao['frontmatter']['logo']
    dao_Objects["website_link"] = dao['frontmatter']['website']
    dao_Objects["discord_link"] = dao['frontmatter']['discord']
    dao_Objects["twitter_link"] = dao['frontmatter']['twitter']
    dao_Objects["additional_link"] = dao['frontmatter']['telegram']

    allDaoData.append(dao_Objects)

    dao_Objects = {
        "chains": ["solana"],
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

    # print(dao_Objects) 

with open("SolanaFinalData.json", "w") as file:
    json.dump(allDaoData, file)