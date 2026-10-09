def calculate_total(marks):
    return sum(marks)
def calculate_per(marks):
    total=calculate_total(marks)
    return total/len(marks)
def calculate_grade(per):
    if per >= 90:
        return "A+"
    elif per >=80:
        return "A"
    elif per >=70:
        return "B"
    elif per >= 60:
        return"C"
    elif per >= 50:
        return "D"
    elif per >=35:
        return "E"
    else :
        return "Fail"
    