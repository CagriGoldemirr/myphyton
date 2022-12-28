# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:07:29 2022

@author: Asus
"""

#DİCTİONARY

# bir değişken  veya bir sembole karşılık olarak verilen anlamlar x : çağrınınn hayatı,K:Jack
# 1:[2,3,4,5] 


sozluk = {
    "book" : "kitap",
    "table" : "masa",
    "pencil" : "kalem"
    
    
    }


print(sozluk)

#print(sozluk[])  sözlükte herhangi bir elemana gitmek veya sadece o elemaı yazdırmak istiyorsak köşeli paratezin içine sayı değil key i yanı değişkeni yazdırmalıyız
print(sozluk["book"])
print(sozluk["pencil"])

sozluk["table"] = "nice masa" # bunu kullanrak ddeğişkenin değerini değiştirebilirm
print(sozluk)
print(sozluk["table"])


sozluk["god"] = "Allah" # eğer yeni eleman eklemek istiyorsam böyle yeni eleman ekleyebilirm
print(sozluk)


sozluk2 = dict(one = "bir", best = "en iyi")
print(sozluk2)


del(sozluk["book"]) # eğer bir değişkeni silmek istiyorsam bunu kullanıyorum
print(sozluk)



#del(sozluk["masa"])  # ama böyle key in karşılığını silmeye çalışırsam hata verir ve yanlış olur

print(sozluk) 
print(len(sozluk)) # böyle yaparak da sozlukte kaç key,anahtar kelime kullandım öğrenebilirm
 











