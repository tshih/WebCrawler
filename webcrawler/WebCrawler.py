import requests
import shutil
import os
import re
from bs4 import BeautifulSoup

def cleanFolderAbsolute(folderPath):
	if os.path.exists(folderPath):
		shutil.rmtree(folderPath)
	os.makedirs(folderPath)


currentPath = os.getcwd()

startingSiteURL = "http://finalfantasy.wikia.com/wiki/List_of_Final_Fantasy_VIII_Triple_Triad_cards"
imgPath = currentPath + "/TripleTriadCards"

cleanFolderAbsolute(imgPath)

startingSite = requests.get(startingSiteURL)
soup = BeautifulSoup(startingSite.text, "html.parser")

for a in soup.find_all("a", class_="image image-thumbnail"):
	cardImgURL = a.get("href")
	if(cardImgURL):
		# print(cardImgURL)
		fileName = re.search("/[\w-]+\.png", cardImgURL).group(0)
		savePath = imgPath + fileName
		cardImg = requests.get(cardImgURL, stream=True)
		cardImg.raw.decode_content = True
		with open(savePath, "wb") as f:
			shutil.copyfileobj(cardImg.raw, f)






# tables = soup.find_all("table", class_="full-width FFVIII table")
# print(tables)


###Finds all links in "a" tag
#for link in soup.find_all("a"):
#	print(link.get("href"))