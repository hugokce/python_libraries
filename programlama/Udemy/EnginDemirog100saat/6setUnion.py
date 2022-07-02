# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)    #iki seti birleştiriyoruz tekil olarak
print(setA.union(setB))   #1,2,3,4,5,6,7,8
print(setB.union(setA))

print(setA & setB)    #kesişim elemanları verir.
print(setA.intersection(setB))   #1,3,4
print(setB.intersection(setA))

print(setA - setB)     #fark bulur   2,5
print(setA.difference(setB))
print(setB.difference(setA))     8,6,7

print(setA ^ setB)     #ikisinin birbirinden farklı olan değerleri verir
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
#2,5,8,6,7 verir  1,3,4 harici kalanları verir.

