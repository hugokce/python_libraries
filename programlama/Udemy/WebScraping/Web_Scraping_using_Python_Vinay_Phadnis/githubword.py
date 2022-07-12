import requests
from bs4 import BeautifulSoup

myWord = "online"

url = 'https://github.com/trending'
baseUrl = 'https://github.com'
r = requests.get(url)
print(r)
print("Request Succesful")
html = BeautifulSoup(r.content,'html.parser')
#print(soup)
repoBox = html.find('div', class_ ='explore-pjax-container')
#print(repoBox)
repoLinks = []
print("Extracting URLs")
repoObjects = repoBox.find_all('article',class_='Box-row')
#print(repoObjects[0])
for repoObj in repoObjects:
    h1Tag = repoObj.find('h1',class_='lh-condensed')
    aTag = h1Tag.find('a')
    aUrl = aTag.attrs['href']
    print(aUrl,end='\n')
    repoLinks.append(baseUrl+aUrl)
#print(repoLinks)
print("URL extraction complete")

print("Making requests to all urls")
for link in repoLinks:
    repoReq = requests.get(link)
    print("Made request to",link)
    repoSoup = BeautifulSoup(repoReq.content,'html.parser')
    mdObject = repoSoup.find('article',class_='markdown-body')
    #print(repoReq)
    print("Searching for word")
    md = str(mdObject)
    if myWord in md:
        print("Word found")
    else:
        print("Word not found")
    print('\n'*4)


