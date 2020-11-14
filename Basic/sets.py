# -*- coding: utf-8 -*-

# sets indexsiz ve sırasız elemanlardan olusur.
# veri tekrari olmaz. butun item lar unique olmali.
# cok hizli calisir.

setList = {"Mesut","Mehmet","Metin","Cem"}

print(type(setList))
print(setList)

for item in setList:
    print(item)

print("Mesut" in setList) # "Mesut" setList de var mı?

if "Mesuta" in setList:
    print("LİSTEDE VAR")
else:
    print("LİSTEDE YOK")
    

# set liste yeni eleman ekle.
setList.add("Murat")
print(setList)

setList.update(["ABC","DEF","HGI"])
print(setList)


print(len(setList))


# listeden eleman sil
setList.remove("HGI") # item yoksa hata verir.
setList.discard("HGI") # item yoksa hata vermez.
print(setList)

# seti temizle
setList.clear()
print(setList)

# seti tamamen sil
# del setList
# print(setList)