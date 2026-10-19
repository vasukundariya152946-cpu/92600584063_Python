f=open("demo.txt","w")
f.write("Python Programming")
f.close()

f=open("demo.txt","r")

print("Initial position :",f.tell())
data=f.read(6)
print("Read data:",data)

print("Current after seek:",f.tell())

f.seek(0)
print("position after seek:",f.tell())

data=f.read(6)
print("Read again :",data)

f.close()
