# 8. Write a program to demonstrate basic regular
# expression pattern matching.
import re
text = "My Phone Number is 9875278965"

pattern = r"\d+"
result = re.search(pattern,text)
if result:
    print("Pattern Found :",result.group())
else:
    print("pattern Not Found")
if re.match(r"My",text):
    print("Text Starts  with My ")
else:
    print("Text does not start with My")
    
# output :-
# Pattern Found : 9875278965
# Text Starts  with My
# PS D:\vasu\python\Unit 3> 