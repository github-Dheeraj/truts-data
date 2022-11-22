import json


trutsData = []
arbitrumData = []
completeDataFile = []

with open("RawTrutsData1.json", "r") as dataFile:
    data = json.load(dataFile)
    completeDataFile = data
    print("length: " , len(completeDataFile))

with open("./CompleteData/cosmosRawdata.json", "r") as arbitrumFile:
    arbitrumData = json.load(arbitrumFile)
    
isThere = False
for eachDataArb in arbitrumData:
    for eachData in completeDataFile:
        if( eachDataArb["twitter_link"] == eachData[ "twitter_link"]):
            # eachData["chain"].append("arbitrum-one")
            # print(eachData["chain"])
            trutsData.append(eachData)
            break
        
            

for eachDataArb in arbitrumData:
    for eachData in trutsData:
        if(eachDataArb["twitter_link"] == eachData["twitter_link"]):
            print(eachData["twitter_link"])
            isThere = True
    
    if isThere == False:
        completeDataFile.append(eachDataArb)

    if isThere == True:
        isThere = False
    
print("length truts" , len(trutsData))
print("length arb" , len(completeDataFile))

with open("RawTrutsData2.json", "w") as File:
    json.dump(completeDataFile, File)
    

 