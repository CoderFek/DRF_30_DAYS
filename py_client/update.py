import requests

endpoint = 'http://127.0.0.1:8000/api/products/11/update/'

data = {
    "title": "Hello world x 100",
    "content": None,
    "price": 30
}

response = requests.put(endpoint, json=data)

# print(response.text)
print(response.json())