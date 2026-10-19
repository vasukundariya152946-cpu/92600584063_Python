# Write a program to read and write data into a
# # file using different file modes.
f=open("Student.txt","w")
f.write("Name: Vasu\n")
f.write("Cours: MCA\n")
f.close()
f=open("Student.txt","r")
print("File Content:")
print(f.read())
f.close()

f=open("Student.txt","a")
f.write("Collage : Marwadi university\n")
f.close()

f=open("Student.txt","r")
print("Updated content :")
print(f.read())
f.close() 
# output:-
# File Content:
# Name: Vasu
# Cours: MCA

# Updated content :
# Name: Vasu
# Cours: MCA
# Collage : Marwadi university
