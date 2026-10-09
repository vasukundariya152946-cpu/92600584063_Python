# Write a program to perform file and directory
# # operations using os and sys modules.
import os
import sys

print("Current Directory:",os.getcwd())

Folder ="My Folder"

if not os.path.exists("My Folder"):
    os.mkdir("My Folder")
    print("Directory created succesfully ")
else:
    print("Directory already exists")
    
    
file_path =os.path.join("My Folder","demo.txt")

with open(file_path,"w") as f :
    f.write("Hello Python")
    
print("file created successfully")

print("Directory Contents :",os.listdir(Folder))

print("Python version :",sys.version)

new_path = os.path.join(Folder,"newdemo.txt")
os.rename(file_path,new_path)
print("Flie renamed successfully")
# os.rename(file_path,os.path.join("My Folder","newdemo.txt"))
# print(" File renames successfully")

# Output :-
# Current Directory: D:\vasu\python\Unit 3
# Directory already exists
# file created successfully
# Directory Contents : ['demo.txt']
# Python version : 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]
# Flie renamed successfully