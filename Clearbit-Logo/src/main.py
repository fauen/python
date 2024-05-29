import requests as r
import os

def get_logo(company):
    url = f"https://logo.clearbit.com/{company}.com?size=512"
    response = r.get(url=url)
    output_dir = "logos"
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    if response.status_code == 200:
        with open(f"logos/{company}-logo.png", 'wb') as f:
            f.write(response.content)
    else:
        print("No logo found.")

def main():
    try:
        while True:
            company = input("Input company name: ")
            get_logo(company)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()