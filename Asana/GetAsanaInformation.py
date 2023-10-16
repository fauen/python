import requests as r
import json

asanaBearerToken = ""

asanaHeaders = {
    'Authorization': 'Bearer ' + asanaBearerToken,
    'Content': 'application/json'
}

asanaMe = r.get("https://app.asana.com/api/1.0/users/me", headers=asanaHeaders)
asanaMeData = json.loads(asanaMe.text)
asanaGid = asanaMeData['data']['workspaces'][0]['gid']

userOptions = """
1. Get your workspace gid.
2. Get all teams in workspace.
3. Get all projects for specific team.
4. Get all tasks in a project.
5. Get the sections in a project.
6. Get all the tasks in section.
7. Get raw data of a task.
0. Nothing.
"""

while True:
    print(userOptions)
    userAnswer = input("Pick an option: ")
    if userAnswer.isdigit():
        userAnswer = int(userAnswer)
        if userAnswer == 1:
            print(f"The workspace ID is: {asanaGid}")
        elif userAnswer == 2:
            asanaTeams = r.get("https://app.asana.com/api/1.0/workspaces/" + asanaGid + "/teams", headers=asanaHeaders)
            asanaTeamsJson = json.loads(asanaTeams.text)
            asanaTeamsData = asanaTeamsJson['data']
            for item in asanaTeamsData:
                print(item['gid'] + " - " + item['name'])
        elif userAnswer == 3:
            asanaTeam = input("Input team ID: ")
            asanaProjects = r.get("https://app.asana.com/api/1.0/teams/" + asanaTeam + "/projects", headers=asanaHeaders)
            asanaProjectsJson = json.loads(asanaProjects.text)
            asanaProjectsData = asanaProjectsJson['data']
            for item in asanaProjectsData:
                print(item['gid'] + " - " + item['name'])
        elif userAnswer == 4:
            asanaProject = input("Input project ID: ")
            asanaAllTasks = r.get("https://app.asana.com/api/1.0/tasks?project=" + asanaProject, headers=asanaHeaders)
            asanaAllTasksJson = json.loads(asanaAllTasks.text)
            asanaAllTasksData = asanaAllTasksJson['data']
            for item in asanaAllTasksData:
                print(item['gid'] + " - " + item['name'])
        elif userAnswer == 5:
            asanaProject = input("Input project ID: ")
            asanaSections = r.get("https://app.asana.com/api/1.0/projects/" + asanaProject + "/sections", headers=asanaHeaders)
            asanaSectionsJson = json.loads(asanaSections.text)
            asanaSectionsData = asanaSectionsJson['data']
            for item in asanaSectionsData:
                print(item['gid'] + " - " + item['name'])
        elif userAnswer == 6:
            asanaSection = input("Input section ID: ")
            asanaTasks = r.get("https://app.asana.com/api/1.0/sections/" + asanaSection + "/tasks", headers=asanaHeaders)
            asanaTasksJson = json.loads(asanaTasks.text)
            asanaTasksData = asanaTasksJson['data']
            for item in asanaTasksData:
                print(item['gid'] + " - " + item['name'])
        elif userAnswer == 7:
            asanaTask = input("Input task ID: ")
            asanaFullTask = r.get("https://app.asana.com/api/1.0/tasks/" + asanaTask, headers=asanaHeaders)
            asanaFullTaskJson = json.loads(asanaFullTask.text)
            asanaFullTaskData = asanaFullTaskJson['data']['custom_fields']
            for item in asanaFullTaskData:
                print(f"{item['name']}: {item['display_value']}")
        elif userAnswer == 0:
            break