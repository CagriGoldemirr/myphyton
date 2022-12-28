# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:30:04 2022

@author: Asus
"""
#FONKSİYONLAR
#bir kodu bir  çok yerde kullanmanız gerekiyorsa her yere tekrar tekrar yazmamızı engeller

#kdv hesaplayıcı kodumuz var.diyelimki uygulamada 100 tane yerde kdv kodununz kullanmamız gerekiyor tekrar tekara yazmak veya kopyala yapıştır yapmak yerine bundan yararlanabilirz . kdv oranı değişirse tek tek bunları değiştirmemiz gerekecek o yüzden bu yazacağımız kod bize kolaylık sağlaysehir
sehir = "Ankara"

sonuc = (sehir.upper()) # bu da bir fonksiyon ama bir parametretye sahip değil 
print(sonuc)
print(sehir.endswith("a")) # bu da bir fonksiyon  ama bunu parametresş var şehir isimli değişkenin değeri a ile bitiyor mu


def selamVer(isim):     # eğer parantezin içini boş bırakırsam ben bu fonksiyonu herhangi bir parametreye bağlamadım demektir . buradaki selmaver bu fonksiyonun ismi.benim parametrem İSİM
    print("Merhaba" + " " + isim)
selamVer("cagri") #buraya yazmamızın sebebi bu satırdaki kod fonksiyonu çağırmamızı sağlıyor
selamVer("ahmet")
selamVer("mehmet")
selamVer("ali")
selamVer("nevzat")
selamVer("caner")
#selamVer() eğer böyle çalıştırmaya çalışırsam çalışmaz


 
def selamVer(isim = "ziyaretçi"): #eğer parametre vermezsek phyton default olarak yazdırır ve burada problem çıkmaz ama  bir  üsttekii kodda boşluk olarak çalıştırmaya çalışırsam kod hata veriyor ve  çalışmıyor.boşluklu şekilde çalıştırmak istiyorsam değişkene bir değer adamalıyım
    print("Hello" + " " + isim)
selamVer()
selamVer("ayse") #böyle yapınca parantez içine bir değer adadığım için ismin değişkeninin değerini okumaya/yazdırmaya gerek duymuyor


def selamVer2(isim = "ziyaretçi" , soyisim = "arkadaş"):
    print("Hello" + " " + isim + " " + soyisim)
selamVer2() #eğer parametre vermezse default olarak  isim değişkeninin değerini dşirekt alır ama parametre veririsek isim değişkeninin değerini almaz.bu olaya default parametre denir
selamVer2("güzel")  #peki buradaki güzel kelimesi nasıl oldu la isim kelimesiini yerine geldi?
selamVer2("güzel","insan") # ikincibir kelime eklediğimfde de ikinci kelimeyi arkdadaş kelimesinii yerine ekledi.alt satıra kod eklerken tırnak içine yazdığım ilk kelime ilk değişkenini yerine diye sırasıyla gider 



def sınavnotu(puan):
    print(str("sınavdan" + puan + "aldım"))
sınavnotu("yüz")    
sınavnotu("sıfır")


# def selamVer3(isim = "ziyaretçi" , soyisim): # ama böyle olursa phytonun kafası karışıyor default değer her zaman en solda olmalı.zorunlu olmayan değeri olan değişkenler en sağda olmalı eğer biri değerli biri değersiz ise
#     print("Hello" + " " + isim + " " + soyisim)    
# selamVer3()    
#selamVer3(nida)   
    

def selamVer4(isim , soyisim = "arkadaş"): # yani böyle olmalı e eğer bir değişken değersiz olacaksa bu en sağda olmalı
    print("Merhaba " + " " + isim + " " + soyisim) 
selamVer4("cagri")    
#selamVer4() böyle olunca çalışmıyor çünkü isim parametresi zornlu
selamVer4("cagri","goldemir")


        #DEĞER RETURN EDEN FONKSİYONLAR
#biz fonksiyonları ikiye ayırıypruz returnn edenler vee etmeyenler. etmyeen fonksiyonları bir emir kipi gibi düşünebilir<
#diyelimki excel e bir değer yazdırmak istiyoruz kod vasıtasıyla  prgramı çalıştırdık belki gitti yazdı belki yazmadı bunu nasıl kontrol edebilirz?gidip o excel dosyasını bulup konttrol ederiz.ama ben bu işi programdan kontrol etmek istiyorsam  değer return kullnarak kontrol edebilirm.Değer returnüne git bak bakalım o satırsa benim istediğim kelime orada var mı diye o da true or false olarak cevap verecek böyle fonksiyonlara değer return eden fonksiyonlar denir
#biz bazen kod yazarken programma direkt emir veriyotuz git ekrana  şunu yazdır gibi ama  bu bir return değil direkt yaazdırmak demek


def dikUcgenAlanıHesapla(a,b):
    return a*b/2
dikUcgenAlanıHesapla(2,3) # eğer dikucgenalanhesapla yazısını bir değişkene bağlamasaydık kod .alışmayacaktı
alan = dikUcgenAlanıHesapla(2,3)
print(alan)
#print(dikUcgenAlanıHesapla(2,3)) # eğer böyle de yazsaydık hesaplardı


