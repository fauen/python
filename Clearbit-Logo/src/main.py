import requests as r

def get_logo(company):
    url = f"https://logo.clearbit.com/{company}.com?size=500"
    response = r.get(url=url)
    if response.status_code == 200:
        with open(f"{company}-logo.png", 'wb') as f:
            f.write(response.content)
    else:
        print("No logo found.")

def main():
    company = input("Input company name: ")
    get_logo(company)

if __name__ == "__main__":
    main()