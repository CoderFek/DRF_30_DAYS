import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    "title":"This is created using fbv",
    "price": 69.00
}
response = requests.post(endpoint, json=data)

# print(response.text)
print(response.json())