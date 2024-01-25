def ms_user_get(user, token):
    import requests as r
    headers = {
        'Authorization': f"{token}",
        'Content-Type': f"application/json"
    }
    user = r.get(f"https://graph.microsoft.com/v1.0/users/{user}", headers=headers)
    return user.json()

def ms_manager_get(user, token):
    import requests as r
    headers = {
        'Authorization': f"{token}",
        'Content-Type': 'application/json'
    }
    user = r.get(f"https://graph.microsoft.com/v1.0/users/{user}/manager", headers=headers)
    return user.json()
    
def ms_manager_set(user, manager, token):
    import requests as r
    headers = {
        'Authorization': f"{token}",
        'Content-Type': 'application/json'
    }
    body = {
        "@odata.id": f"https://graph.microsoft.com/v1.0/users/{manager}"
    }
    manager = r.put(f"https://graph.microsoft.com/v1.0/users/{user}/manager/$ref", headers=headers, json=body)
    
def ms_group_update(user, group, token):
    import requests as r
    headers = {
        'Authorization': f"{token}",
        'Content-Type': 'application/json'
    }
    body = {
        "members@odata.bind": [
            f"https://graph.microsoft.com/v1.0/directoryObjects/{user}"
        ]
    }
    group = r.patch(f"https://graph.microsoft.com/v1.0/groups/{group}", headers=headers, json=body)