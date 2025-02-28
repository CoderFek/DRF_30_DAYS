import requests

endpoint = 'http://127.0.0.1:8000/api/products/11/'
response = requests.get(endpoint)

print(response.text)
#print(response.json())