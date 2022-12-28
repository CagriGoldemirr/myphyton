# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:28:15 2022

@author: Asus
"""



#sayılar = [2,3,5,7,11,13]
sayi = int(input("Lütfen sayıyı giriniz : "))
asalMı = "evet"
#print(7 % 2) # bu 7 nin 2 ile bölümünden kalanı verir 

for x in range(2,sayi):
    if (sayi % x) == 0:
      print("asal sayı değildir")
      asalMı = "hayır"
      break
if asalMı == "evet":
    print("asal")
else:
    print("asal değil")










    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    

