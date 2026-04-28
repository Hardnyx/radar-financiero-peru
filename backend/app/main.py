import requests
url = 'https://example.com'
data = requests.get(url)
content_json = data.json
print(data)
