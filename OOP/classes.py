# -*- coding: utf-8 -*-

# self class ın kendisine referans ediyor.
# self bellekteki Math sınıfı (ipucu, pointer)

#%% Basics
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def addition(self):
        return self.a + self.b
    
    def extraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b

mat = Math(5,9)
print("Sonuc:" + str(mat.addition()))

mat2 = Math(6,7)
print("Sonuc:" + str(mat2.multiplication()))
    
    
#%% Property

class Person:
    def __init__(self,firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    

person = Person("Mesut", "Dede", 32)
print(person.firstName + person.lastName)

#%% Inheritance

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary

class Customer(Person):
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber


worker = Worker()
worker.firstName

customer = Customer()
customer.age