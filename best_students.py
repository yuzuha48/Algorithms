# Write a program that takes in a dictionary of student names and their corresponding test scores, and returns the 2 student names with the highest score.

students = {
    "Jax": 8,
    "Janna": 7.5,
    "Ahri": 9,
    "Oriana": 9.5,
    "Caitlyn": 8.7
}


def bestScore(students):
    best_score = max(students.values())
    for key, value in students.items():
        if value == best_score:
            best_student = key

    second_score = 0
    for key, value in students.items():
        if value > second_score and value != best_score:
            second_student = key
            second_score = value
    
    return best_student, second_student

print(bestScore(students))


