# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:41:44 2022

@author: Asus
"""

            #SET 
#listeleler benzer. en önemli özelliği  indexsiz ve sıraasız elemanlardan oluşmasıdır.veri tekrarıs söz konusu olamaz.tüm elemanlar eşsizdir.  
#hızlı çalışırlar
my_set = {1, 2, 3, 4}
print(my_set)
studentSets = {"Engin","Cagri","Ahmet",}
print(studentSets) # benim yazdığım sıra ile çıktıdaki sıra farklı  çünküliste ve tuple daki gibi 0. eleman 1. eleman vs gibi şeyler yok  phyton kendisi karar veriyor 


studentSets2 = {"Engin","Cagri","Ahmet","Ahmet"}  # ahmeti iki defa yazsam bile çıktıda 2 defa yazılan değer 2 defa çıkmıyorçıktıda aynıysa 1 tane çıkıyor
print(studentSets2)
 #sette index olmadığı için her bir elemana listedeki gibi şak diye(kolayca) ulaşammyıyoruz ama arayabiliyoruz
 
for student in studentSets:  # bu for lu kalıbı kullanark setteki verileri tek tek alt alta yazdırabilirm
    print(student)


print("cagri" in studentSets) # bu şu anlama geliyor benim setimde "cagri" diye bir şey var mı yok mu phyton  büyük- küçük duyarlı olduğu için cagri yi bulamıyor ve false yazısı çıkıyor


print("Cagri" in studentSets) #true yazarak benim listemde Cagri nin var olduğunu öğrenebildim

print("Engin" in studentSets)

if  "Engin" in studentSets:    # ıf kalıbı böyle de kullanılır eşitlis vs olmadan da
    print("engin sette var")           
 #peki ben listdeki Cagri verisinin yerine Aynur yazdırabliri miyim?HAYIR SETTE BUNA İZİN YOK
 # ama yeni veri ekleyebilirz 
studentSets.add("Aynur") # tek bir eleman ekleyceksem bunu kullanabilirm
print(studentSets)
 
studentSets.update(["Caner","Nevzat"]) # eğer birden fazla eleman ekleyeceksem update yi kullanırım

print(studentSets)

print(len(studentSets)) #listedeki gib burada da benzer fonksiyonları kullanabiliyoruz

studentSets.remove("Cagri") # bu fonksiyonu kullanark istediğim herhangi bir elemanı silebirim
print(studentSets)


x = studentSets.pop() # bu fonksiyon listeden herhangi bir  elemanı silmeye yarıyor ama silerken phyton kendi kafasına göre siliyor bellş bir kuralı yok
print(studentSets)




studentSets2.clear()  # bu da tüm setteki elemanları silmeye yarıyor len fonk o dizide uygulayarak kontrol etitm ve 0 çıktı
print(studentSets2)
print(len(studentSets2))

del studentSets2 # bu da tamamaen seti siliyor 















