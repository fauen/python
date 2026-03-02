import requests as r
import os

def get_logo(company: str, token: str):
    url = f"https://img.logo.dev/{company}.com?size=512?token={token}"
    response = r.get(url=url)
    output_dir = "logos"
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    if response.status_code == 200:
        with open(f"logos/{company}-logo.png", 'wb') as f:
            f.write(response.content)
    else:
        print("No logo found.")

def main(token: str):
    try:
        while True:
            company = input("Input company name: ")
            get_logo(company, token)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    token = input("Input token: ")
    main(token)
