def ms_graph_bearer(ms_tenant, ms_client_id, ms_client_secret):
    import requests as r
    url = f'https://login.microsoftonline.com/{ms_tenant}/oauth2/v2.0/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': f'{ms_client_id}',
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': f'{ms_client_secret}',
        'grant_type': 'client_credentials'
    }
    ms_graph_message = r.post(url, headers=headers, data=data)
    ms_graph_response = ms_graph_message.json()
    ms_bearer_token = ms_graph_response['access_token']
    return ms_bearer_token

if __name__ == "__main__":
    tenant = input("Tenant: ")
    client_id = input("Client ID: ")
    client_secret = input("Client secret: ")
    bearer = ms_graph_bearer(tenant, client_id, client_secret)
    print(f"Bearer:\n{bearer}")