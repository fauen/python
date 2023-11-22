import requests as r
import tkinter as tk
from pprint import pprint as pp

def getSLinformation():
    #key = keyInput.get()
    #siteId = siteInput.get()
    key = ""
    siteId = ""
    url = f'https://api.sl.se/api2/realtimedeparturesV4.json?key={key}&siteid={siteId}&timewindow=30'
    getInfo = r.get(url)
    jsonData = getInfo.json()
    pyList = jsonData['ResponseData']['Metros']
    print([dest for dest in pyList if(dest['Destination'] == '')])
    #outputString.set(jsonData)
    
getSLinformation()

# window = tk.Tk()

# mainFrame = tk.Frame(window, padx=10, pady=10)
# mainFrame.pack()
# frameLabel = tk.LabelFrame(mainFrame, text="SL Departure")
# frameLabel.pack()
# keyLabel = tk.Label(mainFrame, text="Input key")
# keyLabel.pack()
# keyInput = tk.Entry(mainFrame)
# keyInput.pack()
# siteLabel = tk.Label(mainFrame, text="Input siteId")
# siteLabel.pack()
# siteInput = tk.Entry(mainFrame)
# siteInput.pack()

# submitButton = tk.Button(mainFrame, text="Submit", command=getSLinformation)
# submitButton.pack()

# outputString = tk.StringVar()
# outputLabel = tk.Label(mainFrame, textvariable=outputString)
# outputLabel.pack()

# window.mainloop()