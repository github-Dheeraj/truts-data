from asyncio import sleep
import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

with open("completeTrutsData.json", "r") as file:
    data = json.load(file)

pathToSeleniumDriver = "./chromedriver"
# pathToSeleniumDriver = "/mnt/e/all data/Denil/Dev_Tools/chromedriver.exe"
driver = webdriver.Chrome(pathToSeleniumDriver)

# print("FETCHING DAO IMGS FROM TWITTER...")
# for dao in data:
#     dao["dao_cover"] = ""
#     dao["dao_logo"] = ""
#     try:
#         link = dao["twitter_link"]
#         driver.get(link)
#         time.sleep(3)
#         content = driver.page_source
#         soup = BeautifulSoup(content, "html.parser")

#         img_link = soup.find("img", class_="css-9pa8cd")["src"]
#         img_link.replace("/600x200", "/1500x500")

#         dao["dao_cover"] = img_link
#         dao["dao_logo"] = img_link
#         print(f"Success: {dao['dao_name']}")
#     except:
#         print(f"err: {dao['dao_name']}")
# print("FETCHED DAO IMGS FROM TWITTER!!")

print("FETCHING DISCORD MEMBER COUNT...")
for dao in data:
    url = dao["discord_link"]
    if url != "":
        try:
            driver.get(url)
            time.sleep(3)
            content = driver.page_source
            soup = BeautifulSoup(content, "html.parser")
            dao["discord_members"] = soup.find_all(
                "span",
                class_="defaultColor-24IHKz text-sm-normal-3Zj3Iv pillMessage-3pHz6R",
            )[1].text.replace(" Members", "")
        except:
            print(f"err: {dao['dao_name']}")
            dao["discord_members"] = 0
    else:
        dao["discord_members"] = 0

for dao in data:
    if dao["discord_members"] != 0:
        name = dao["dao_name"]
        memb_count = dao["discord_members"].replace(",", "")
        try:
            dao["discord_members"] = int(memb_count)
        except:
            print(f"err: {name}")
    else:
        pass
print("FETCHED DISCORD MEMBER COUNT!!")
driver.close()

print("FETCHING DISCORD GUILD IDS...")
for dao in data:
    link = "https://discord.com/api/v9/invites/"
    name = dao["dao_name"]
    dao["guild_id"] = "null"
    if dao["discord_link"] != "":
        try:
            code = dao["discord_link"].split("/")[-1:]
            print(f"{name}: {code}")

            url = link + code[0]
            print(url)
            response = requests.get(url)
            guildId = response.json()["guild"]["id"]
            print(guildId)
            dao["guild_id"] = guildId
        except:
            print(f"guild err: {name}")
        finally:
            sleep(1)
            continue
    else:
        print(f"err: {name}")
print("FETCHED GUILD IDS!!")

url = "https://api.twitter.com/1.1/users/show.json?screen_name="
head = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAJ%2BjcQEAAAAAtZngAuUpvVcHJIavG0ln3F38Ilk%3Duob5Ktma1TUO4eAk5WAMsgMWPiaHaY5GLROZQqpviNaLaUHYd9"
}

print("FETCHING TWITTER DATA...")
for dao in data:
    dao["twitter_followers"] = 0
    if dao["twitter_link"] != "":

        screen_name = dao["twitter_link"].split("/")[-1:][0]
        if screen_name != "":
            cURL = url + screen_name
            try:
                response = requests.get(cURL, headers=head)
                try:
                    count = response.json()["followers_count"]
                    dao["twitter_followers"] = count
                except:
                    print(f"No follower count: {screen_name}")
                    dao["twitter_followers"] = 0
                try:
                    cover = response.json()["profile_banner_url"]
                    dao["dao_cover"] = cover
                except:
                    print(f"No cover: {screen_name}")
                    dao["dao_cover"] = ""
                try:
                    logo = response.json()["profile_image_url_https"]
                    dao["dao_logo"] = logo.replace("_normal", "_400x400")
                except:
                    print(f"No logo: {screen_name}")
                    dao["dao_logo"] = ""
                try:
                    desc = response.json()["description"]
                    dao["description"] = desc
                except:
                    print(f"No desc: {screen_name}")
                    dao["description"] = ""
                print(f"Succesfull: {screen_name}")
            except:
                name = dao["dao_name"]
                print(f"Err: {name}")
                dao["twitter_followers"] = 0
                dao["dao_cover"] = ""
                # dao["dao_logo"] = 0
                dao["description"] = ""
    else:
        dao["twitter_followers"] = 0
        dao["dao_cover"] = ""
        # dao["dao_logo"] = 0
        dao["description"] = ""

print("FETCHED TWITTER DATA!!")


print("ADDING FINAL DATA...")
for dao in data:
    dao["average_rating"] = 0
    # dao["__v"] = 0
    dao["question_list"] = {
        "q1": "Do you resonate with the vibes in the DAO community?",
        "q2": "Do you believe your opinions matter in the DAO community?",
        "q3": "Would you recommed this DAO/community to your friend?",
        "q4": "How would you rate the DAO’s onboarding experience?",
        "q5": "Do you think that DAO has great organizational structure?",
        "q6": "Do you think there are great incentives for DAO members?",
    }
    dao["question_list_rating"] = {
        "q1": 50,
        "q2": 50,
        "q3": 50,
        "q4": 50,
        "q5": 50,
        "q6": 50,
    }
    dao["review_count"] = 0
    dao["verified_status"] = True
    dao["slug"] = (
        dao["dao_name"].lower().replace(" ", "_").replace("(", "").replace(")", "")
    )

print("ADDED FINAL DATA!!")


# print("CHEKING FOR MATCHING DAOS...")
with open("final-data.json", "w") as file:
    json.dump(data, file)
