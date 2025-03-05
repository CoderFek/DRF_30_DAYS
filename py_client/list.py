import requests
from getpass import getpass

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'

username = input("What is your username? \n")
password = getpass("Enter your password: \n")

auth_response = requests.post(auth_endpoint, json={'username':username, 'password': password})

# print(response.text)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = 'http://127.0.0.1:8000/api/products/'
    response = requests.get(endpoint, headers=headers)
    print(response.json())