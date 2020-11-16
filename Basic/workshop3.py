# -*- coding: utf-8 -*-

# Faktoriyel hesaplama

#%% Factorial
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result = result*i
    
    return result

print(factorial(4))


#%% Matris toplama

x = [[1,3,5],[2,4,1],[1,5,7]]
y = [[3,3,4],[2,4,1],[3,5,4]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]

print(result)


#%% Kelime siralama

sentence = "bugün hava cok güzel"
arr = sentence.split()
arr.sort()
print(arr)