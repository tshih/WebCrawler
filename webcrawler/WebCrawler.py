import requests
import shutil
import os
from bs4 import BeautifulSoup

currentPath = os.getcwd()
imgPath = currentPath + "/CrawledImages"


if os.path.exists(imgPath):
	shutil.rmtree(imgPath)
os.makedirs(imgPath)

test = requests.get("https://accenture.com")
soup = BeautifulSoup(test.text, "html.parser")

savePath = imgPath + "/logo-accenture.png"

testImg = requests.get("https://www.accenture.com/t20150523T054234__w__/us-en/_acnmedia/Accenture/Dev/ComponentImages/logo-accenture.png", stream=True)
testImg.raw.decode_content = True
with open(savePath, "wb") as f:
	shutil.copyfileobj(testImg.raw, f)

#Finds all images in img tag that are 
for link in soup.find_all("img"):
	if(link.get("src")): # Checks if src tag exists
		print(os.path.basename(link.get("src"))) #Print only the base file name





###Finds all links in "a" tag
#for link in soup.find_all("a"):
#	print(link.get("href"))