# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:23:31 2022

@author: Asus
"""

#TUPLE listelere benziyor ama farklılılar var
tupleliste = (2,4,6,"ankara") #listede köşeli parantez kullanyorduk ama burda parantez kullanıyoruz
liste =[2,4,6,"ankara"]








print(type(tupleliste))
print(type(liste))

tupledeger = ("cagri")
tupledeger10 = ("cagri",)
listedeger = ["cagri"]
print(tupledeger) 
print(listedeger)
#ikiside aynı olmasına rağmen biri parantez işaretli oldu  bu tuple ve liste farklarından biri
print(type(tupledeger)) # bunun cevabı yanı türü string çıktı ama bunun türü tuple bir terslık var o yüzden bunun sonuda virgül eklemeiz gerek

print(type(tupledeger10))




print(liste)
print(tupleliste)
tupleliste2 = (1,2,3,4,("ali"),["ayse"]) 
print(tupleliste2)
print(len(tupleliste2))
liste[0] = "6" # listenin 0. elemanın 6 yap demek buu
print(liste)
# tupleliste[2] = "4" #bu kod yanlış çünkü tuple larda bir eleman yerleştirdik mi listeler gibi değiştiremiyoruz
# print(tupleliste)

liste3 = [1,3,5,7,[8]]
tupleListe = (11,12,13,14,(-5))





print(liste3[-1]) # bu da liste3 te sağdan itibaren normal sayarak 1. terim anlamına geliyor 
print(tupleListe[-2]) # tupleListe de sağdan başlayarak 2. terim anlamına geliyor



print(tupleListe[1:2]) # neden tuplenın çıktısının yanında virgül var? sistem bunun tuple olduğunu belli etmek için sonuda virgül ekliyır

print(liste3[1:2]) 








