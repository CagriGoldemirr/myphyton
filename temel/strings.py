mesaj = "Merhaba Dünya"




print(mesaj[2]) #böyle yaparak mesaj deðiþkeninde  3. harfi çýktý olarak alýyoruz
print(mesaj[5]) #böyle yaparak 6. karakteri yazdýrýyor

print(mesaj[2:5]) #böyle  yaparak 0dan saymaya baþlayarak 2 dahil ama 5 dahil olmamak üzere arasýndaki karakterleri yazdýrýr



print(mesaj[3:7])
print(mesaj[0:2])
yenimesaj = (mesaj[2:5])


print(yenimesaj)  # böyle yaparak bir  deðeri bir deðiþkene atayabilirz
print(mesaj[2:]) # bu da 2 dahil olmak üzere geri kalan tüm karakterleri yazdýr demek
print(mesaj[:2]) # iki noktadan sonraki dahil deðil(e kadar anlamý var) ve bu yazým da baþtan itibaren 2. karaktere kadar yazdýr anlamýna geliyor
print(mesaj[:5])
print(len(mesaj)) #bu komut mesajýn kaç karakterden oluþtuðunu söylüyor(iki kelime arasýndaki boþluk da dahil) ve saymaya baþlarken 1 den baþladýk
print(mesaj[12:13]) #diyelimki son harfi yazdýrmak bulmak istiyorum o zaman kelime 0 dan baþlayarak saydýðýmda 12 çýkýyor bana en sonuncu yani 12. lazým ama 13 ü boþluk gib düþünüp zaten onu dahil etmiyorum 12:13 yazýp son harfe ulaþabilirm
print(len(mesaj))

print(mesaj[12:13]) #bu ile alttaki iki satýr kod ayný deðeri veriyor


yenimesaj2 = (mesaj[len(mesaj)-1:len(mesaj)])
print(yenimesaj2)



# lower küçült,upper büyüt anlamýna geliyor.metnin tümünün harf büyüklüðünü deðiþtirceðiniz zaman kullanýlýr
print(mesaj.upper()) 
print(mesaj.lower())

#REPLACE   bazen turrkce karakterler sýkýntý çýkardýðýnda bu fonk iþimizi görür
print(mesaj.replace("ü","u"))  #ü yü u yaptý mesajdaki
print(mesaj.replace("Dünya","çaðrý")) # ayný xamanda kelimeyi de deðiþtirebilirm


#split
bilgi = "cagri goldemir 20 balikesir"
print(bilgi.split()) #böyle yazarak bilgi deðiþkenini deðerini kelime kelime parcalaarýn ayiriyor ayrýca içteki parantez içine bir þey boþluk ya da karakter yazmadýðýmýz halde boþluklarýna göre ayýrdý yani splitin defaultu boþluk
print(bilgi.split(" ")) #bu da üstteki gibi ayný aslýnda boþlupu gördðü anda ayýrýyor
bilgi2 = "cagri;goldemir;20;balikesir"
print(bilgi2.split(";")) # bu da deðiþkenin deðerini noktalý virgüle göre ayýr demek
bilgi3 = "cagri;goldemir;20;balýkesir;;;;;"
print(bilgi3.split(";"))
print(bilgi3.split(";")[2])



#ÝNPUT
ad = input("Adýnýz?")
sayý1 = input("sayý1 =? ")
sayý2 = input("sayý2 =? ")
print(sayý1 + sayý2) #böyle yapýnca input veriyi metinsel olarak algýladý o yüzden baþýna int yazma gereði duyduk
print(int(sayý1) + int(sayý2))











