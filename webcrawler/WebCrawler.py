import requests
from bs4 import BeautifulSoup

test = requests.get("https://accenture.com")
soup = BeautifulSoup(test.text, "html.parser")

#Finds all images in img tag
for link in soup.find_all("img"):
	print(link.get("src"))

##Finds all links in "a" tag
for link in soup.find_all("a"):
	print(link.get("href"))

print("Testing Again")