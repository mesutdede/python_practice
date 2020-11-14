# -*- coding: utf-8 -*-

# Tuple read-only dir.
# Tuple daha az maliyetlidir. Daha performanslı çalışır.

tupleList = (2,4,6,"Ankara",(7,8,9),[])
lists = [2,4,6,"Ankara",[6,7,8],()]

print(type(tupleList))
print(tupleList)

print(len(tupleList))

lists[0] = 3
print(lists)

# tupleList[0] = 3 # tuple item degistirilemez.
print(tupleList[-2]) # sagdan ikinci item
print(lists[-2]) # sagdan ikinci item

# tek elemanda tuple oldugunu belli etmek icin yanina virgul(,) konur.
tupleValue = ("Mesut",)
print(tupleValue)

print(tupleList[1:2])
print(lists[1:2])