import requests as r
from os import system, name

def GetDepartures(siteId: int, siteName: str):
    url = f"https://transport.integration.sl.se/v1/sites/{siteId}/departures"
    getData = r.get(url)
    getDataJson = getData.json()
    ClearScreen()
    print(f"From {siteName}\n")
    for departure in getDataJson["departures"]:
        metro = departure["stop_area"]["type"]
        if metro == "METROSTN":
            print(f"{departure["destination"]} - {departure["display"]}")

def GetStops(userInput: str):
    url = f"https://transport.integration.sl.se/v1/sites?expand=true"
    getData = r.get(url)
    getDataJson = getData.json()
    for stationInfo in getDataJson:
        if userInput.lower() == stationInfo["name"].lower() and stationInfo["id"] > 9000:
            stationId = stationInfo["id"]
            stationName = stationInfo["name"]
            return stationId, stationName

def ClearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def main():
    userInput = input("What station do you want to see departures for?\n")
    GetStops(userInput)
    stationId, stationName = GetStops(userInput)
    GetDepartures(stationId, stationName)

if __name__ == "__main__":
    main()