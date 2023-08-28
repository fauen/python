import json
import requests as r

#r = requests

menu = '''
1. Dad joke
2. Affirmation
3. Guess age from name
4. Chuck Norris fact
5. Country facts
6. Weather
0. Quit
'''

while True:
    print(menu)
    userAnswer = input("Pick an option: ")
    if userAnswer.isdigit():
        userAnswer = int(userAnswer)
        if userAnswer == 1:
            url = "https://icanhazdadjoke.com"
            headers = {"Accept": "text/plain"}
            print((r.get(url, headers = headers).text))
        elif userAnswer == 2:
            url = "https://www.affirmations.dev"
            request = r.get(url)
            jsonResponse = request.json()
            print(jsonResponse["affirmation"])
        elif userAnswer == 3:
            name = input("Input your name: ")
            url = "https://api.agify.io/?name=" + name
            request = r.get(url)
            jsonResponse = request.json()
            #for key, value in jsonResponse.items():
            #    print(f"{key}: {value}")
            print("Based on the name " + name + " the person should be " + str(jsonResponse["age"]) + " years old.")
        elif userAnswer == 4:
            url = "https://api.chucknorris.io/jokes/random"
            request = r.get(url)
            jsonResponse = request.json()
            print(jsonResponse["value"])
        elif userAnswer == 5:
            name = input("Input country: ")
            url = "https://restcountries.com/v3.1/name/" + name
            request = r.get(url)
            jsonResponse = request.json()
            for key in jsonResponse:
                print(json.dumps(key, indent=4))
        elif userAnswer == 6:
            url = "https://wttr.in"
            request = r.get(url)
            print(request.text)
        elif userAnswer == 0:
            quit()