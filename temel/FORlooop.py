# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:23:08 2022

@author: Asus
"""
#FOR
    #benzer işlemleri belirli bir şarta göre tekrarlamak için kullamılır
    #döngü tek tek elemanları çalıştırır
sehirler = ["ankara","istanbul","balıkesir","izmir"]
print(sehirler[0])
print(sehirler[1])
print(sehirler[2])
print(sehirler[3])
 #eğer 100 lerce şehir,data olsaydı tek tek yazmak zorunda mı kalacaktım?
 #döngüler birbirine benzeyen işleri daha hızlı yapılmasının sağlar
for sehir in sehirler:
    print(sehir[0:1])  #sehirler iççnde bir döngü yapacağını anlıyoruz bu satırdan. oradaki sehir nereden geliyor peki? programın kontrol ettiği,uğraştığı her bir şehrin takma adı gibi düşünebiilirz

for sehir in sehirler:
    print(sehir[0:9]) # elemanların her birinin 0 da  9. harfe kadar yazdır demek oluyor bu
for sehir in sehirler:
    print(sehir[2:5])
    
    
for sehir in sehirler:
    print(sehir + " " + "için kod = " + sehir[0:5])    
    

      
for sehir in sehirler:
    if sehir == "ankara":      #döngüyü sadece ankara ile koşulladım
        print(sehir + " " + "için kod = " + sehir[0:4])
    if sehir == "balıkesir":
        print(sehir + " " +  sehir[0:3] + " " + "gibidir")
            

 
     
















