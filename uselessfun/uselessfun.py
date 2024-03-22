import requests as r
import json

def Joke():
    url = "https://icanhazdadjoke.com"
    headers = {
        'Accept': 'text/plain'
    }
    response = r.get(url=url, headers=headers)
    print(response.text)

def Affirmation():
    url = "https://www.affirmations.dev"
    response = r.get(url=url)
    response = response.json()
    print(response["affirmation"])

def Age():
    name = input("Input name: ")
    url = f"https://api.agify.io/?name={name}"
    response = r.get(url=url)
    response = response.json()
    print(response["age"])

def Chuck_Norris():
    url = "https://api.chucknorris.io/jokes/random"
    response = r.get(url=url)
    response = response.json()
    print(response["value"])

def Country():
    country = input("Input country name: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = r.get(url=url)
    response = response.json()
    print(json.dumps(response, indent=2))

def Weather():
    url = "https://wttr.in"
    response = r.get(url=url)
    response = response.text
    print(response)

def Menu():
    print('''
    1. Dad joke
    2. Affirmation
    3. Guess age from name
    4. Chuck Norris fact
    5. Country facts
    6. Weather
    0. Quit
        ''')

def main():
    while True:
        try:
            Menu()
            answer = input("Pick an option: ")
            if not answer.isdigit():
                print("\nThat's not a number silly...")
            else:
                answer = int(answer)
                if answer == 1:
                    Joke()
                elif answer == 2:
                    Affirmation()
                elif answer == 3:
                    Age()
                elif answer == 4:
                    Chuck_Norris()
                elif answer == 5:
                    Country()
                elif answer == 6:
                    Weather()
                elif answer == 0:
                    return
        except KeyboardInterrupt:
            return

if __name__ == "__main__":
    main()