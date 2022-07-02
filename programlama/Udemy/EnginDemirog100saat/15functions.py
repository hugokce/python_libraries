# -*- coding: utf-8 -*-

#%%
sehir = "Ankara"

sonuc = sehir.upper()
print(sonuc)
print(sehir.endswith("e"))  #true false döner 

#%%
def selamVer(isim = "ziyaretçi"):
    print("Merhaba " + isim)
    
#isim için parametre vermemiz gerekiyor
selamVer("Engin")
selamVer("Derin")
selamVer("Salih")
selamVer("Ahmet")
selamVer("Mehmet")
selamVer()   #ziyaretçi diyecek bize

def selamVer2(isim, soyIsim ="arkadaş"):  default değer hep sonda olmalı yoksa kafası karışır
    print("Merhaba " + isim + " " + soyIsim)

selamVer2("Derin")
selamVer2("Engin","Demiroğ")

#%%
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)

print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))  function döner

x = dikUcgenAlaniHesapla2

print(x(4,5))


