student_name = input()

bad_grades_counter = 0
current_class = 1
is_excluded = False
grade = 0

while current_class <= 12:
    current_grade = float(input())

    if current_grade < 4:
        bad_grades_counter += 1

        if bad_grades_counter == 2:
            is_excluded = True
            break

        continue

    current_class += 1
    grade += current_grade

if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")

else:
    average_grade = grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
