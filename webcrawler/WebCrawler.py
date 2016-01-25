import requests
import shutil
import os
import re
from collections import defaultdict
from bs4 import BeautifulSoup

def cleanFolderAbsolute(folderPath):
	if os.path.exists(folderPath):
		shutil.rmtree(folderPath)
	os.makedirs(folderPath)

def createFolderName(h):
	return "/" + str(h.string).replace(" ", "")

def flatten(list_of_lists):
	return [val for sublist in list_of_lists for val in sublist]


currentPath = os.getcwd()

startingSiteURL = "http://finalfantasy.wikia.com/wiki/List_of_Final_Fantasy_VIII_Triple_Triad_cards"
imgPath = currentPath + "/TripleTriadCards"

cleanFolderAbsolute(imgPath)

startingSite = requests.get(startingSiteURL)
soup = BeautifulSoup(startingSite.text, "html.parser")

content = soup.find("div", class_="mw-content-ltr mw-content-text")

# for h3 in content.find_all("h3"):
# 	for h in h3.span:
# 		print(createFolderName(h))

folders = [ [ createFolderName(h) for h in h3.span] for h3 in content.find_all("h3")]
folderNames = flatten(folders)

# for table in content.find_all('table', class_="full-width FFVIII table"):
# 	for img in table.find_all("a", class_="image image-thumbnail"):
# 		print(img.get("href"))

cardImgList = [ [img.get("href") for img in table.find_all("a", class_="image image-thumbnail")] for table in content.find_all('table', class_="full-width FFVIII table")]

for i in range(0, len(folderNames)):
	folder = folderNames[i]
	os.makedirs(imgPath + folder)
	for cardImgURL in cardImgList[i]:
		fileName = re.search("/[\w-]+\.png", cardImgURL).group(0)
		savePath = imgPath + folder + fileName
		cardImg = requests.get(cardImgURL, stream=True)
		cardImg.raw.decode_content = True
		with open(savePath, "wb") as f:
			shutil.copyfileobj(cardImg.raw, f)




# for a in soup.find_all("a", class_="image image-thumbnail"):
# 	cardImgURL = a.get("href")
# 	if(cardImgURL):
# 		fileName = re.search("/[\w-]+\.png", cardImgURL).group(0)
# 		savePath = imgPath + fileName
# 		cardImg = requests.get(cardImgURL, stream=True)
# 		cardImg.raw.decode_content = True
# 		with open(savePath, "wb") as f:
# 			shutil.copyfileobj(cardImg.raw, f)






# tables = soup.find_all("table", class_="full-width FFVIII table")
# print(tables)


###Finds all links in "a" tag
#for link in soup.find_all("a"):
#	print(link.get("href"))