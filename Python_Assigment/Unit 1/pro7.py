#  7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.\
print("-----Dictionary----------")
student = {
    "name":"vasu",
    "age":21,
    "course":"Python"
}
print(student)
print("Name",student["name"])
print("Age",student["age"])
print("Course",student["course"])

print("-------dictionary method--------")
print("Keys :",student.keys())
print("Values :",student.values())
print("Item :",student.items())

student["city"] = "Rajkot"
print("After addind city :",student)

student["age"] = "22"
print("After Upadating Age:",student)

student.pop("city")
print("After removing city",student)

for key,valuse in student.items():
    print(key,":",valuse)
    
    
'''
output:-
-----Dictionary----------
{'name': 'vasu', 'age': 21, 'course': 'Python'}
Name vasu
Age 21
Course Python
-------dictionary method--------
Keys : dict_keys(['name', 'age', 'course'])
Values : dict_values(['vasu', 21, 'Python'])
Item : dict_items([('name', 'vasu'), ('age', 21), ('course', 'Python')])
After addind city : {'name': 'vasu', 'age': 21, 'course': 'Python', 'city': 'Rajkot'}
After Upadating Age: {'name': 'vasu', 'age': '22', 'course': 'Python', 'city': 'Rajkot'}
After removing city {'name': 'vasu', 'age': '22', 'course': 'Python'}
name : vasu
age : 22
course : Python'''