# -*- coding: utf-8 -*-

# Aynen set gibi sırasız veri tutar.
# key:value

my_dict = {
        "book": "kitap",
        "table": "masa",
        "computer": "bilgisayar"
    }

print(my_dict)
print(len(my_dict))

my_dict["book"] = "kitap 1" # değer degistir.
my_dict["pencil"] = "kalem" # yeni eleman ekle.

print(my_dict)

my_dict2 = dict(kitap = "book", masa = "table")

print(my_dict2)

del(my_dict["book"]) # item sil
print(my_dict)