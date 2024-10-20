#importing the library
import os

write = 1
while write == 1:
    write = int(input("Do you want to use this code to make a file(0 for no 1 for yes)?: "))
    if write != 1:
        print("Exiting loop")
        break
    path = input("Please enter the path where you want to create the file: ")
    if len(path) == 0:
        print("We will be making the file in the folder where this python file is.")
    name = str(input("What do you want to name your python file?: "))
    if len(name) == 0:
        continue
    text = input(f"What do you want to write {name}?: ")
    with open(name+".txt","w") as file:
        file.write(text)