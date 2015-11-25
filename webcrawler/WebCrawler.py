import requests

print("Hello World")

test = requests.get("https://accenture.com")

print (test.text)