#Example code:
import tkinter
import os
from tkinter import filedialog
var=filedialog.askdirectory()
print(var)
var1=input("enter the filename:")
print(var1)
var2=os.path.join(var,var1)
with open(var2,"W")as file:
    file.write("afvdvsdvs")


#Example code:    

file = open('hello.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)


#Example code:
    #Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

#Example code:

with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

 import os
 
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)       

    



    
    





