# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:11:14 2022

@author: Asus
"""#listelemeyi neden kullanırız?
#zaman zaman elimizde yüzlerce veri olacak bu verileri tek tek ogrenci1 ogrenci2 diye tek etk yazmak bizi  yorar op yüzden listeleme mantığını iyi bilmemiz gerek.bu veriler bize bazen wordden bazen başka bir kaynaktan gelebilir.tek bir noktadan bir çok veriyi rahatlıkla kontrol edebilmek için listelemeye ihtiyaç duyarız 
ogrenci1 = "engin"
ogrenci3 = "cagri"
ogrenci2 = "ayse"
ogrenciler = ["engin","cagri","ayse"]
print(ogrenciler[1]) # Ogrenciler listesindeki  sıralı verileriden 1. yazdır demek oluyor bu
print(ogrenciler)




ogrenciler.append("kemal") # bu da listeye yeni eleman eklemek için kullanılır
ogrenciler.remove("cagri") # bu da listeden bir ogeyi çıkarmak için kullanılır
ogrenciler[0] = "veli" # bu da 0. elemanı değiştirmek için kullanılıyor

print(ogrenciler)

sehirler = list(("ankara","istanbul"))
print(sehirler)
sehirler.append("balıkesir")
print(sehirler)
sehirler.remove("ankara")
print(sehirler)


#DİĞER FONKSİYONNLAR


 #print(sehirler.clear()) # clear ın işlevi sehirler isimli listeyi temizle demek ve cevabıda none
#print(sehirler) # bunun cevabı da bir hiçtir çünkü artık sehirler isimli listeyi temizledim

print(sehirler.count("aydın"))  # bu da listedeki aydın isimli verilerin sayosonoı gösteriyor yani 0
print(sehirler.count("balıkesir")) # balıkesir isimli veri 1 tane olduğu için 1 yazısı çıktı consolda

#print("balıkesir sayısı = " + sehirler.count("balıkesir"))  # burdakı kod hatallı çünkü  + dan önceki veri metinsel bir veri ama + dan sonraki veri sayısal bir veri ikisi uyumsuz
print("istanbul sayısı = " + str(sehirler.count("istanbul")))
print("balıkesir indexi = " + str(sehirler.index("balıkesir"))) #balıkesir index olarak kaçıncı sıradadır demek bu
print(sehirler)
print("istanbul indexi = " + str(sehirler.index("istanbul")))
sehirler.append("izmir")
print(sehirler)
sehirler.pop(1) #listedeki 1. elemanı silmeye\çıkarmaya yarıyor bu



sehirler.insert(0,"van") # bu da listenın 0. indexine  bir eleman eklemeye yarıyor


print(sehirler)

sehirler.reverse() # bu da listeyi terse çevirmeye yarıyor 
print(sehirler)


sehirler2 = sehirler
sehirler2[0] ="rize" # bu da 0.sıradakı elemaı çıkartıp yerine rizeyi koydu
print(sehirler)
print(sehirler2)



sehirler3 = sehirler.copy()  #bu sehirleri yeni değişken olan sehirler3 e kopyala demek bu sayede iki listedeki içerikler aynı oldu
print(sehirler3)
print(sehirler2)
print(sehirler)
sehirler.extend(sehirler3)     #diyelimki elimde iki tane farklı dizi var amacım bunları birleştirmekse bun kullanabilirm
print(sehirler) # rize istanbul vanı iki kere yazdı aynı listede
sehirler.sort() # bu da sehirler listesinin içindeki elemanları a dan z ye kadar alfabetik olarak sıraladı ama yazdırmak istiyorsam print kullanmama lazım

print(sehirler)









