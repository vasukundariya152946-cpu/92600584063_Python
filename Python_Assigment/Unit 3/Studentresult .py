import result_utils
name=input("Enter Your Name =")
marks=[]
for i in range(5):
    marks.append(int(input("Enter marks")))
total = result_utils.calculate_total(marks)
per= result_utils.calculate_per(marks)
grade = result_utils.calculate_grade(per)
print("/n ------------- Student Result -------")
print("Name : ",name)
print("Total :",total)
print("Percentage :",per,"%")
print("Grade :",grade)
