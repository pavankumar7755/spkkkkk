#text=open("python.txt",'r')
"""text.write("end of the note")

for lines in text:
    print(lines)"""

"""create = open("pythonlife.txt","w")
create.write("i am learning fil handling today")"""

"""saturday = open("file_handling.txt","w")
saturday.write("saturday is thebest day")"""

"""
append = open("append.txt","a")
append.write("surya sir is good boy")
append.close()"""


#python_dream = open("python.txt","r")
#print(python_dream.read(9))

"""text=python.readlines()
for lines in text:
    word = lines.split()"""

import csv 

with open('data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)