import requests
from bs4 import BeautifulSoup
import time

def getPriceData():
    url = 'https://www.flipkart.com/superlux-pro-shotgun-battery-box-video-mic-go-lightweight-camera-condenser-microphone-super-cardioid/p/itmf8g7cgsdtfjgy?pid=MICF8G4GQGNF5U3D&lid=LSTMICF8G4GQGNF5U3DVU6843&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=00cf8487-26bc-428b-83d9-4e1f43f68932.MICF8G4GQGNF5U3D.SEARCH&ppt=sp&ppn=sp&ssid=r5l9e63rq80000001599504868957&qH=bcfdb96425fa9dba'
    r = requests.get(url)
    print(r)

    html = BeautifulSoup(r.content,'html.parser')

    print(html)

    pricingObj = html.find('div',class_='_1vC4OE')
    pricingStr = pricingObj.text
    #print(pricingObj)
    print(pricingStr)

    replaceSymbol = pricingStr.replace(pricingStr[0],'')
    replaceComma = replaceSymbol.replace(',','')
    price = int(replaceComma)
    return price
    #print(price)

priceArray=[]

#f = open('pricingdata2.txt','w')

for i in range(30):
    tempPrice = getPriceData()
    #print(tempPrice,"  ",i)
    priceArray.append(tempPrice)
    #print(str(tempPrice)+'\n')
    print()
    f = open('pricingdata3.txt','a')
    #f = open('pricingdata3.txt','a') arada a yazmış  
    f.write(str(tempPrice)+'\n')
    f.close()
    #time.sleep(5)
    #time.sleep(60*60*24)
    #f.write(str(tempPrice)+'\n')
    time.sleep(2)

f.close()
