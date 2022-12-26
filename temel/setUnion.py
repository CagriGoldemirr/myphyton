# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:33:57 2022

@author: Asus
"""
setA = {1,3,5,7,9}  #union=birleştirme,birleşmek
setB = {2,4,6,8}

print(setA | setB)  # bunu kullanarak iki seti union yaparak ikisini birleştirdim
print(setA.union(setB)) #böyle de ikisin birleştirebilirm


set1 = {"Ali","Caner","Veli"}
set2 = {"Azra","Nehir","Caner"}
print(set1 | set2)
print(set1.union(set2)) # metinsel verileri birleştiriken rastgele birleştiriyor 

print(set1 - set2)











setx = {"12","36","9","5"}
sety = {"5","45","1","36"}
print(setx | sety)
print(setx & sety) # bu da iki dizideki ortak elemanları göstermek için kullanılır
print(setx.intersection(sety)) # böyle de ortak elemları bulabilirz bu da farklı yol


set1 = {"Ali","Caner","Veli"}
set2 = {"Azra","Nehir","Caner"}
print(set1 | set2)
print(set1.union(set2)) # metinsel verileri birleştiriken rastgele birleştiriyor 

print(set1 - set2) # bu da set1 den set2 yi çıkar anlamına geliyor  kümelerdeki a/b ya da b/a gibi 
print(set1.difference(set2)) # bu da aynı işlevi yerine getiriyor

print(set1 ^ set2) # bu da ortak elenman harici diğer verileri gösteriyor
print(set1.symmetric_difference(set2)) # bu da bir farklı yolu














