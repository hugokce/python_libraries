# -*- coding: utf-8 -*-

#ogrenci1 = "Engin"
#ogrenci2 = "Derin"
#ogrenci3 = "Salih"
#
#print(ogrenci1)
#print(ogrenci2)
#print(ogrenci3)

ogrenciler = ["Engin","Derin","Salih"]

#sonuna ekler append ile
ogrenciler.append("Ahmet")
#ogrenciler[4] = "Veli"   out of range hatası verir 4 yok
print(ogrenciler[3])
ogrenciler.remove("Salih") o kaydı bulur ve siler
print(ogrenciler)

#list constructor
sehirler = list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar
#print(sehirler.clear())  içine temizler
print("Ankara sayısı = " + str(sehirler.count("Ankara")))
print("Ankara indexi = " + str(sehirler.index("Ankara")))
sehirler.pop(1)   birinci indexi siler
sehirler.insert(0,"İstanbul")   0. indexe istanbul ekler
sehirler.reverse()  tersine çevirir
print(sehirler)


sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0]="İzmir"    sehirler de değişti
#ama copy deyince değişmez.


print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)   #2 listeyi biraraya getirir
sehirler.sort()
sehirler.reverse()
print(sehirler)



















