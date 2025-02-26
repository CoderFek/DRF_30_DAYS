import requests

endpoint = 'http://127.0.0.1:8000/'
response = requests.post(endpoint, json={"title": "New123", "price":12})

print(response.text)
#print(response.json())