sayi = 10 #bu bir integer
kelime = "burak"
tc = "10987654321" #bu bir string  bunun sayısal olarak hiçbir hükmü yok çünkü ben onu metinsel bir veri olarak depoladım
soyisim = "goldemir"
telefonnumarası = 12345
sınavdanAldığımNot = "100"
boyum = 12.4
#iki veriyi toplmak istiyorsak bunların ikiside aynı veri tipi olmak zorunda int-int float-float sting-string gibi eğer stringdeki sayıyla integerdaki sayıyı toplamak istiyorsam aşşağıdaki gibi başına int,float,str ifadesi getirerek  onu diğer veriye dönüştürüp toplayabilirm

print(soyisim + tc) 
print(int(tc) + 10) #burada tc başına int koyarak onu bir integera dönüştürdüm ve toplayabildim bu sayede

print(type(12.4)) # başına type koyarak o veririnin türünü öğrenebilirm
print(type(boyum))
print(type(sayi))