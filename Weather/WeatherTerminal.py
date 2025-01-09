import requests as r
from sys import argv

def main(url: str) -> None:
    try:
        get_data = r.get(url)
        content = get_data.text
        print(content)
    except r.exceptions.RequestException:
        print("Something went wrong with the URL.")


if __name__ == "__main__":
    try:
        url = argv[1]
        main(url)
    except Exception as e:
        print("You need to specify an URL.")