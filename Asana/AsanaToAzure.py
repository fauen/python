import os
import requests
import json
from art import text2art

api_key = None
section_id = None

#os.system("cls")

banner = text2art("Banner Text")
print(banner)

if not api_key:
    api_key = input("Input your bearer token: ")

if not section_id:
    section_id = input("Input Asana section: ")

headers = {
    "Authorization": "Bearer " + api_key,
    "Content": "application/json"
}

asana_all_tasks = requests.get("https://app.asana.com/api/1.0/sections/" + section_id + "/tasks", headers=headers)
all_tasks_json = json.loads(asana_all_tasks.text)
for tasks in all_tasks_json["data"]:
    print(tasks["gid"], tasks["name"])
#print(type(all_tasks_json["data"]["gid"]))

asana_task_id = input("Input task id: ")

asana_full_task = requests.get("https://app.asana.com/api/1.0/tasks/" + asana_task_id, headers=headers)
task_details = json.loads(asana_full_task.text)
full_name = task_details["data"]["custom_fields"][2]["display_value"]
fullname_split = full_name.split()
firstname = fullname_split[0]
lastname = fullname_split[1:]
print(firstname)
print(lastname)