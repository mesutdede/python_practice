# -*- coding: utf-8 -*-

# Kullanici tarafindan girilen sayi pozitif mi negatif mi?

number = input("Sayi giriniz: ")
number = int(number)
if number > 0:
    print("POZİTF")
elif number == 0:
    print("SIFIR")
else:
    print("NEGATİF")
    
    
# Kullanicidan girilen sayilardan en buyugu bul.

number1 = int(input("1.sayiyi giriniz: "))
number2 = int(input("2.sayiyi giriniz: "))
number3 = int(input("1.sayiyi giriniz: "))

largest = 0

if (number1 > number2) and (number1 > number3):
    largest = number1
elif (number2 > number3) and (number2 > number1):
    largest = number2
else:
    largest = number3
    
print("En buyuk sayi ",str(largest))