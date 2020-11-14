# -*- coding: utf-8 -*-

# for loop

cities = ["Ankara","İstanbul","Trabzon"]

for city in cities:
    if city == "İstanbul":
        continue
        # break
    print(city[0:3], ":", city)


# while loop

i = 0

while i <= 10:
    i = i + 1
 
print(str(i))


#%% range function

for x in range(10,100,2):
    print(x + 1)