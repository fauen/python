import requests as r

def main():
    url = "https://en.wikipedia.org/wiki/Wikipedia:On_this_day/Today"
    headers = {
            "User-Agent": "A simple bot"
            }
    response = r.get(url=url, headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()
