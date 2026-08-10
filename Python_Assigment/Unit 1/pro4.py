# 4. Write a program to demonstrate string operations including slicing formatting and built-in string functions.
Text = "My name is vasu"
print("Original string =", Text)
print("length = ",len(Text))
print("Addition ",Text+"  From Rajkot")
print("Ripition ", Text*2)
print("-----Slicing----------")
print("First 5 character =", Text[:5])
print("Last 5 character =", Text[6:])
print("character 1 to 7 =", Text[1:7])
print("Revese ",Text[::-1])
print("--------Formatting----------")
name="vasu"
age=21
print("My name is {} and I am {} years old.".format(name,age))
print(f"My name is {name} I am {age} year old.")

print("-------- built-in string functions----------")
print("Uppercase =",Text.upper())
print("Lowercase =",Text.lower())
print("Replace =",Text.replace("vasu","Meet"))
print("Count",Text.count("o"))
print("find =",Text.find("vasu"))

'''output :
    original string = My name is vasu
length =  15
Addition  My name is vasu  From Rajkot
Ripition  My name is vasuMy name is vasu
-----Slicing----------
First 5 character = My na
Last 5 character = e is vasu
character 1 to 7 = y name
Revese  usav si eman yM
--------Formatting----------
My name is vasu and I am 21 years old.
My name is vasu I am 21 year old.
-------- built-in string functions----------
Uppercase = MY NAME IS VASU
Lowercase = my name is vasu
Replace = My name is Meet
Count 0
find = 11'''