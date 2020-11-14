# -*- coding: utf-8 -*-

setA = {1, 2, 3, 4, 5}
setB = {1, 3, 4, 6, 7, 8}

print(setA | setB) # union
print(setA.union(setB))
print(setB.union(setA))


# intersection
print(setA & setB) # intersection
print(setA.intersection(setB))
print(setB.intersection(setA))



# difference
print(setA - setB) # difference
print(setA.difference(setB))
print(setB.difference(setA))


# symmetric difference
# farkların birleşimi

print(setA ^ setB) # symmetric difference
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))


