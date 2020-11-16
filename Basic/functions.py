# -*- coding: utf-8 -*-

#%%
def sayHello(name = "quest"):
    print("Hello",name)

sayHello("Dede")
sayHello()

# default degerli parametreler sonda olmali.

def sayHello2(firstname, lastname = "Quest"):
    """
    Bu method ne is yapar.
    """
    print("Hello " + firstname + " " + lastname)


sayHello2("Mesut")
        
#%%
def calculateRightTriangleArea(a,b):
    return a*b/2

area = calculateRightTriangleArea(4, 5)

print(area)


#%% Labmda functions
calculateRightTriangleArea2 = lambda a,b : a*b/2

print(calculateRightTriangleArea2(3, 6))

x = calculateRightTriangleArea2

print(x(3,4))