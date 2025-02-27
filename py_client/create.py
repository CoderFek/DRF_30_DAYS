import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    "title":"This is created using generics",
    "price": 40.00
}
response = requests.post(endpoint, json=data)

# print(response.text)
print(response.json())