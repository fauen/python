import requests as r

def GetDepartures(key, siteid):
    url = f"https://api.sl.se/api2/realtimedeparturesV4.json?key={key}&siteid={siteid}&timewindow=15&bus=false&train=false&tram=false&ship=false"
    getData = r.get(url)
    getDataJson = getData.json()
    return getDataJson

userKey = input("Input key: ")
userSiteID = input("Input siteid: ")
getTheData = GetDepartures(userKey, userSiteID)
#print(f"{getTheData["ResponseData"]["Metros"][0]["Destination"]} - {getTheData["ResponseData"]["Metros"][0]["DisplayTime"]}")
for subway in getTheData["ResponseData"]["Metros"]:
    print(f"{subway["Destination"]} - {subway["DisplayTime"]}")