mesaj = "Merhaba D�nya"




print(mesaj[2]) #b�yle yaparak mesaj de�i�keninde  3. harfi ��kt� olarak al�yoruz
print(mesaj[5]) #b�yle yaparak 6. karakteri yazd�r�yor

print(mesaj[2:5]) #b�yle  yaparak 0dan saymaya ba�layarak 2 dahil ama 5 dahil olmamak �zere aras�ndaki karakterleri yazd�r�r



print(mesaj[3:7])
print(mesaj[0:2])
yenimesaj = (mesaj[2:5])


print(yenimesaj)  # b�yle yaparak bir  de�eri bir de�i�kene atayabilirz
print(mesaj[2:]) # bu da 2 dahil olmak �zere geri kalan t�m karakterleri yazd�r demek
print(mesaj[:2]) # iki noktadan sonraki dahil de�il(e kadar anlam� var) ve bu yaz�m da ba�tan itibaren 2. karaktere kadar yazd�r anlam�na geliyor
print(mesaj[:5])
print(len(mesaj)) #bu komut mesaj�n ka� karakterden olu�tu�unu s�yl�yor(iki kelime aras�ndaki bo�luk da dahil) ve saymaya ba�larken 1 den ba�lad�k
print(mesaj[12:13]) #diyelimki son harfi yazd�rmak bulmak istiyorum o zaman kelime 0 dan ba�layarak sayd���mda 12 ��k�yor bana en sonuncu yani 12. laz�m ama 13 � bo�luk gib d���n�p zaten onu dahil etmiyorum 12:13 yaz�p son harfe ula�abilirm
print(len(mesaj))

print(mesaj[12:13]) #bu ile alttaki iki sat�r kod ayn� de�eri veriyor


yenimesaj2 = (mesaj[len(mesaj)-1:len(mesaj)])
print(yenimesaj2)



# lower k���lt,upper b�y�t anlam�na geliyor.metnin t�m�n�n harf b�y�kl���n� de�i�tirce�iniz zaman kullan�l�r
print(mesaj.upper()) 
print(mesaj.lower())

#REPLACE   bazen turrkce karakterler s�k�nt� ��kard���nda bu fonk i�imizi g�r�r
print(mesaj.replace("�","u"))  #� y� u yapt� mesajdaki
print(mesaj.replace("D�nya","�a�r�")) # ayn� xamanda kelimeyi de de�i�tirebilirm


#split
bilgi = "cagri goldemir 20 balikesir"
print(bilgi.split()) #b�yle yazarak bilgi de�i�kenini de�erini kelime kelime parcalaar�n ayiriyor ayr�ca i�teki parantez i�ine bir �ey bo�luk ya da karakter yazmad���m�z halde bo�luklar�na g�re ay�rd� yani splitin defaultu bo�luk
print(bilgi.split(" ")) #bu da �stteki gibi ayn� asl�nda bo�lupu g�rd�� anda ay�r�yor
bilgi2 = "cagri;goldemir;20;balikesir"
print(bilgi2.split(";")) # bu da de�i�kenin de�erini noktal� virg�le g�re ay�r demek
bilgi3 = "cagri;goldemir;20;bal�kesir;;;;;"
print(bilgi3.split(";"))
print(bilgi3.split(";")[2])



#�NPUT
ad = input("Ad�n�z?")
say�1 = input("say�1 =? ")
say�2 = input("say�2 =? ")
print(say�1 + say�2) #b�yle yap�nca input veriyi metinsel olarak alg�lad� o y�zden ba��na int yazma gere�i duyduk
print(int(say�1) + int(say�2))











