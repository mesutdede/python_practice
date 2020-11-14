# Girilen sayi asal mi degil mi?

number = int(input("Bir sayi giriniz: "))
isAsal = True
for x in range(2,number):
    if number % x == 0:
        isAsal = False
        break

if isAsal:
    print("SAYI ASALDIR")
else:
    print("ASAL DEGIl")