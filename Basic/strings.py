# -*- coding: utf-8 -*-

# substring
message = "Hello world!"
print(message[2:7]) #substring
print(message[2:]) # 2. index ten basla sona kadar.
print(message[:4]) # 0. index ten basla 4.index e kadar.
newMessage = message[2:5]
print(newMessage)

# len
print(message[len(message)-1:len(message)]) # son karakter.



# lower - UPPER
print(message.upper())
print(message.lower())



# replace
print(message.replace("!", "..."))



# split & strip
# strip - sagdan soldan bosluklari temizler
data = "  Mesut;Dede;32;İstanbul  ".strip()
print(data.split())
print(data.split(" "))
print(data.split(";"))
print(data.split(";")[1])



# input
name = input("Your name ?")
num1 = input("Number 1: ")
num2 = input("Number 2: ")

print(num1 + num2) # string concat yapar.
print(int(num1) + int(num2)) # int type casting yapilmali.