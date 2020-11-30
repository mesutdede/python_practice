# -*- coding: utf-8 -*-

# r-Read, a-Append, w-Write, x-Create

f = open("demo.txt","r")
# print(f.read())
# print(f.read(5))

print(f.readline())

for line in f:
    print(line)

f.close() # dosyayi kapat

fileToAppend = open("students.txt","w")
fileToAppend.write("\n") # ENTER
fileToAppend.write("Mede")
fileToAppend.writelines("Mesut")
fileToAppend.close()


#%%
# dosya silmek icin
import os
if os.path.exists("students.txt"):
    os.remove("students.txt")
else:
    print("DOSYA ZATEN YOK")
    
os.rmdir("empty") # empty klasorunu siler.