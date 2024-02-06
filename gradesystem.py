def determine_grade(score):
    if score >= 70 and score <= 100:
        return 'A'
    elif score >= 60 and score < 70:
        return 'B'
    elif score >= 50 and score < 60:
        return 'C'
    elif score >= 40 and score < 50:
        return 'D'
    else:
        return 'Fail'

subjects = ['Subject 1', 'Subject 2', 'Subject 3']
grades = []

for subject in subjects:
    while True:
        grade = input(f"Enter the mark for {subject} (1-100): ")
        try:
            grade = int(grade)
            if 0 < grade <= 100:
                break
            else:
                print("Please enter a valid mark between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    grades.append(grade)

average = sum(grades) / len(grades)

print(f"The average score is: {average}")
print(f"The grade based on the average score is: {determine_grade(average)}")
