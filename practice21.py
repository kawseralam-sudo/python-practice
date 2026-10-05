student = {
    "name": "Kawsar",
    "math": 80,
    "english": 75,
    "python": 90,
    "physics": 65
}

def analyze_student(student):
    total_marks=0
    total_sub=0
    average=0
    high_marks=0
    for subject,marks in student.items():
        if subject!="name":
            total_marks+=marks

        if subject!="name":
            total_sub+=1

        if subject!="name" :
            if marks>high_marks:
             high_marks=marks

    average=total_marks/total_sub

    return total_marks,total_sub,average,high_marks

total_marks,total_sub,average,high_marks=analyze_student(student)

print("total marks:",total_marks)
print("total sub:",total_sub)
print("average:",average)
print("high marks:",high_marks)