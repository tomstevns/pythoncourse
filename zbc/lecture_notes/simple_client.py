import requests


response = requests.get('http://10.50.137.116:5000')
print(response.text)
