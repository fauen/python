import requests as r
from datetime import date, datetime

def main() -> None:
    base_url = "https://api.pollenrapporten.se/v1/"
    regionid_sthlm = "2a2a2a2a-2a2a-4a2a-aa2a-2a2a2a303a32"
    request = r.get(url = f"{base_url}forecasts?region_id={regionid_sthlm}&current=true")
    print(request.json()["items"][0]["text"])
    pollen = request.json()["items"][0]["levelSeries"]
#    pollen_id = request.json()["items"][0]["levelSeries"][0]["pollenId"]
#    pollen_level = request.json()["items"][0]["levelSeries"][0]["level"]
    pollen_types = [
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323233", "name": "Hassel"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323236", "name": "Al"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323330", "name": "Sälg och viden"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323331", "name": "Alm"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323332", "name": "Björk"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323335", "name": "Bok"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323337", "name": "Ek"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323433", "name": "Gräs"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323530", "name": "Gråbo"},
                    {"id": "2a2a2a2a-2a2a-4a2a-aa2a-2a313a323533", "name": "Malörtsambrosia"}
                    ]
    filtered_items = []
    for item in pollen:
        item_date = datetime.fromisoformat(item["time"]).date()
        if item_date == date.today():
            filtered_items.append(item)

    for item in filtered_items:
        print(item)
        #pollen_id = item["pollenId"]
        #pollen_level = item["level"]
        #pollen_type_id = pollen_types[0]["id"]
        #pollen_name = pollen_types[0]["name"]
        #if pollen_id in pollen_type_id:
        #    print(f"{pollen_name} - {pollen_level}")

if __name__ == "__main__":
    main()
