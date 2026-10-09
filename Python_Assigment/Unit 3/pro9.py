# 9. Write a program to use re module functions
# such as match search and findall.
import re
text = "Python is  easy . Python is Powerful."
result1=re.match(r"Python",text)
print("Match:",result1.group()if result1 else " Not Found")

result2=re.search(r"easy",text)
print("Search:",result2.group()if result2 else "Not Found")

result3=re.findall(r"Python",text)
print("Find All :",result3)
#  output :
#      t 3\pro9.py"
# Match: Python
# Search: easy
# Find All : ['Python', 'Python']
# PS D:\vasu\python\Unit 3> 