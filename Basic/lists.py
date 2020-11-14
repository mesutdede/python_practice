# -*- coding: utf-8 -*-

students = ["Mesut","Mehmet","Metin"]

print(students)
print(students[1])

for student in students:
    print(student)


students.append("Hakan") # add new item
print(students)

students.remove("Metin") # remove item
print(students)

students[0] = "Veli" # change item value
print(students)

#students[4] = "Cem" # index error

cities = list(("Ankara","Istanbul"))
print(cities)
print(len(cities))


# LIST FUNCTIONS

# cities.clear()
# print(cities)

print("Ankara sayisi: " + str(cities.count("Ankara")))

print("Ankara indexi: " + str(cities.index("Ankara")))

cities.pop(1) # indexteki itemı cikar
print(cities)

cities.insert(0, "Istanbul")
print(cities)

cities.reverse() 

print(cities)

# diziler referans tipdir
cities2 = cities
cities2[0] = "Giresun" # cities de degisir.
print(cities)

#copy list
cities3 = cities.copy()
cities3[0] = "Trabzon"
print(cities3)


cities.extend(cities3)
print(cities)


cities.sort()
cities.reverse()
print(cities)

