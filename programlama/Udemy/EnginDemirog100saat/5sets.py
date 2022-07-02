# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:04:44 2018

@author: Engin
"""
#sıralı gelmez biz sıralı versek de.
studentsSet = {"Engin","Derin","Salih","Ahmet"}
studentsSet2 = set("Mehmet","Veli","Ayşe")
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Derin" in studentsSet)   bu true döner içinde var çünkü

#verisetinde var mı yok diye bakar in ile.
if "Derin" in studentsSet:
    print("Listede var")
    
#varolan bir datayı değiştiremeyiz ama ekleme yapabiliriz
studentsSet.add("Ali")
print(studentsSet)

#birden fazla eleman eklemek istediğimizde kullanabiliriz.
studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet)

print(len(studentsSet))

#bulamazsa hata fırlatır
studentsSet.remove("Selin") 
print(len(studentsSet))

#bulamazsa hata fırlatmasın istersek discard deriz
studentsSet.discard("Selin")
print(len(studentsSet))

#pop kullanırsak hangisini sildiğini bilemeyiz tehlikeli
#bunu kullanmak

x = studentsSet.clear()  #tüm seti temizler
print(len(studentsSet))
del studentsSet  #komple seti siler 
print(studentsSet)
















