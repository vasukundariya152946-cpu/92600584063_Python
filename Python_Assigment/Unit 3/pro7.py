# 7. Write a program to copy move and delete files
# using shutil module.\
import os
import shutil

os.makedirs("Source",exist_ok =True)

with open("Source/demo.txt","w")as f:
    f.write("This is a simple file.")
    
shutil.copy("Source/demo.txt","copy.txt")
print("File Copied successfully")

shutil.move("copy.txt","Source/move.txt")
print("File moved Successfully")

os.remove("Source/move.txt")
print("File Deleted successfully")

os.remove("Source/demo.txt")

os.rmdir("Source")
print("Directory Deleted successfully")
#  output :
#      PS D:\vasu\python\Unit 3> python -u "d:\vasu\python\Unit 3\pro7.py"
# File Copied successfully
# File moved Successfully
# File Deleted successfully
# Directory Deleted successfully
# PS D:\vasu\python\Unit 3> 