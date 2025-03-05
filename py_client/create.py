import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

headers = {
        "Authorization": "Token 89de73e960ba670406dd46da5b4756a21e8a7a8b"
    }
data = {
    "title":"This is created using new token",
    "price": 101.00
}
response = requests.post(endpoint, json=data, headers=headers)

# print(response.text)
print(response.json())