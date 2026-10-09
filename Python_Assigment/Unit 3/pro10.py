# 10.Write a program to extract specific information
# from a text file using regular expressions.
import re
with open("data.txt","w") as f :
    f.write("Name: Vasu\n")
    f.write("Email : vasu12345@gmail.com\n")
    f.write("Phone :9587465621\n")
    f.write("Age : 22\n")
    
with open("data.txt","r") as f:
    text=f.read()
name=re.search(r"Name:\s*(.*)",text)
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
phone = re.search(r"\b\d{10}\b", text)
age = re.search(r"Age:\s*(\d+)", text)
    
print("Extracted Information")

if name:
    print("Name :",name.group(1))
if email :
    print("Email :",email.group())
if phone :
    print("Phone :",phone.group())
if age:
    print("Age :",age.group())
    
#     output :
#         Extracted Information
# Name : Vasu
# Email : vasu12345@gmail.com
# Phone : 9587465621