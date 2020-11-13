# -*- coding: utf-8 -*-

# sayilarin yerini degistir.

x = 10
y = 20

print("x: " + str(x))
print("y:" + str(y))

# Solution 1
# temp = x
# x = y
# y = temp

# Solution 2
x,y = y,x

print("x: " + str(x))
print("y:" + str(y))





# kac km kac mil eder.
# kullanicinin girecegi degeri mile cevir.

kmValue = input("Km value: ")

result = float(kmValue) * 0.62

print(str(result) + " mil eder")
