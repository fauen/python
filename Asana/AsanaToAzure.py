import os
import requests
import json
from art import text2art

api_key = ""
section_id = ""

os.system("cls")

banner = text2art("Banner Text")
print(banner)

if api_key is None:
    api_key = input("Input your bearer token: ")

if section_id is None:
    section_id = input("Input Asana section: ")

headers = {
    "Authorization": "Bearer " + api_key,
    "Content": "application/json"
}

asana_all_tasks = requests.get("https://app.asana.com/api/1.0/sections/" + section_id + "/tasks", headers=headers)
all_tasks_data = asana_all_tasks.json()
testing = json.dumps(all_tasks_data, indent=4)
print(testing)