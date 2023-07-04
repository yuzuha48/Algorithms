## Python Activity

# 1. Create a list of dictionaries representing students' grades:

grades = [
    {"name": "Alice", "math": 65, "english": 85, "history": 92},
    {"name": "Bob", "math": 80, "english": 92, "history": 87},
    {"name": "Charlie", "math": 45, "english": 88, "history": 80},
    {"name": "David", "math": 87, "english": 90, "history": 91},
    {"name": "Emma", "math": 82, "english": 95, "history": 89},
]

# 2. Write a function to find the average grade of a student:

def get_average_grade(student):
    sum = student["math"] + student["english"] + student["history"]
    average = sum/3
    return average

for one_student in grades:
    print(get_average_grade(one_student))

# 3. Write a function to find the student with the highest average grade:

def get_highest_average_grade(grades):
    all_averages = []
    highest_average = 0
    student = None

    for student in grades:
        one_average = get_average_grade(student)
        all_averages.append({"name": student["name"], "average": one_average})

    for person in all_averages:
        if person["average"] > highest_average:
            highest_average = person["average"] 
            student = person["name"]
    
    return student

print(f"Student with the highest average grade: {get_highest_average_grade(grades)}")

# 4. Write a function to find the student with the highest grade in a particular subject:

def get_highest_grade_by_subject(grades, subject):
    subject_grades = []
    highest_grade = 0
    student = None

    for one_student in grades:
        for key, value in one_student.items():
            if key == subject:
                subject_grades.append({"name": one_student["name"], "grade": value})

    for one_person in subject_grades:
        if one_person["grade"] > highest_grade:
            highest_grade = one_person["grade"]
            student = one_person["name"]

    return student

print(f"Student with the highest grade in a particular subject: {get_highest_grade_by_subject(grades, 'history')}")


# 5. Write a function to add a new student to the list of grades:

def add_student(grades, name, math, english, history):
    one_student = {
        "name": name,
        "math": math, 
        "english": english, 
        "history": history
    }
    grades.append(one_student)
    return grades

print(add_student(grades, "Yuzuha", 95, 98, 91))

# 6. Write a function to calculate the percentage of students who passed a particular subject:

def get_subject_pass_percentage(grades, subject, passing_grade):
    passing_students = []

    for one_student in grades:
        for key, value in one_student.items():
            if key == subject and value >= passing_grade:
                passing_students.append(one_student["name"])

    percentage = (len(passing_students) / len(grades))*100

    return percentage

print(f"Percentage of students who passed a subject: {get_subject_pass_percentage(grades, 'math', 70)}")



