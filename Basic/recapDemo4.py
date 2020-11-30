# -*- coding: utf-8 -*-

# listeyi dosyaya yazdir.
students = ["Mehmet", "Ali", "Cem", "Hakan", "Murat"]

fileToAppend = open("students.txt","a")

for student in students:
    fileToAppend.write(student + "\n")

fileToAppend.close()

fileToRead = open("students.txt")

print(fileToRead.read())

fileToRead.close()