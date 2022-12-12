from curses.ascii import NUL
from pydoc import html
import requests
from bs4 import BeautifulSoup as bs
import json
import time 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('/Users/arken/Downloads/chromedriver')

driver.get('https://dappradar.com/defi/protocol/ethereum/1')
time.sleep(3)
# Create an ActionChains object
actions = ActionChains(driver)

# Scroll the page from top to bottom
for i in range(1,100):   
    actions.send_keys(Keys.ARROW_DOWN)
    
actions.perform()
# time.sleep(3)

content = driver.page_source
allDeFiResources = []

URL = 'https://dappradar.com/defi/protocol/ethereum/1'
base_url = 'http://dappradar.com'
dao_Objects = {
    "chains": [],
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

# for page in range(1,5):
#       # pls note that the total number of
#     # pages in the website is more than 5000 so i'm only taking the
#     # first 10 as this is just an example

html_string = ""
# req = requests.get(URL)
# soup = bs(req.text, 'html.parser')
# with open('dappRadar.html', 'r') as f:
#     html_string = f.read()


# page = html_string

soup = bs(content, "html.parser")
# print(soup)

containers = soup.find('table',class_="sc-ehvNnt byUOet")
# print(containers)
tbodyClass = containers.find('tbody',class_="sc-laZRCg cblYxM")
trclasses = tbodyClass.find_all('tr',class_="sc-eJDSGI gKTXmp")
for trclass in trclasses:
    eachdDao = trclass.find('td',class_="sc-oZIhv ldokJF")
    # print(eachdDao)
    atag = eachdDao.find('a')
    eachURL = base_url + atag['href']
    print(eachURL)

    driver.get(eachURL)
    time.sleep(3)
    # Create an ActionChains object
    actions = ActionChains(driver)

    # Scroll the page from top to bottom
    for i in range(1,50):   
        actions.send_keys(Keys.ARROW_DOWN)
        
    actions.perform()
    # time.sleep(3)

    content = driver.page_source
    soup = bs(content, "html.parser")
    dappClass = soup.find('div',class_="sc-fLRopR gbqaRD")
    logoClass  = dappClass.find('div',class_="sc-hrCmsx cVBNLf")
    print(logoClass.find("img")["src"])

    infoClass = dappClass.find('div',class_="sc-kJHwSc iemrCv")
    nameClass = infoClass.find('div',class_="sc-tKebc gVfBiP")
    print(nameClass.find('h1').text)

