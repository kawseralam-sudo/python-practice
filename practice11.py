students = [
    {
        "name": "Rahim",
        "marks": {
            "math": 80,
            "english": 70,
            "python": 90
        }
    },
    {
        "name": "Karim",
        "marks": {
            "math": 60,
            "english": 75,
            "python": 65
        }
    },
    {
        "name": "Kawsar",
        "marks": {
            "math": 95,
            "english": 85,
            "python": 92
        }
    },
    {
        "name": "Hasan",
        "marks": {
            "math": 45,
            "english": 55,
            "python": 40
        }
    }
]

high_ava=0
high_name=""
for student in students:

    total=sum(student["marks"].values())
    avarege=total/len(student["marks"])

    highest_mark = 0
    highest_subject = ""

    for subject, mark in student["marks"].items():

        if mark>highest_mark:
            highest_mark=mark
            highest_subject=subject

    if avarege>=40:
     status="pass"
    else:
     status="fail"

    print("name:",student["name"])
    print("total:",total)
    print("avarege:",round(avarege,2))
    print("Highest mark subject:",highest_subject)
    print("Higest mark:",highest_mark)
    print("stutas:",status)
    print("---------------student infor-------------")

    if avarege>high_ava:
       high_ava=avarege
       high_name=student["name"]

print("Highest mark name:",high_name)
print("Marks:",round(high_ava,2))


