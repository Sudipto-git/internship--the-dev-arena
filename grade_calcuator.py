name = input("Enter student name:  ")
score = float(input("Enter student score (0-100): "))
if score >= 90:
    grade = "A"
    comment = "Excellent"
elif score >= 80:
    grade = "B"
    comment = "Very Good"
elif score >= 70:
    grade = "C"
    comment = "Good"
elif score >= 60:
    grade = "D"
    comment = "Pass"
else:
    grade = "F"
    comment = "Fail"
print(f"Result for: {name} \n Marks : {score} \n Grade : ({grade}) \n Message :  {comment}")


