students_count = int(input())

top_students = 0
under_5 = 0
under_4 = 0
fail = 0
all_grades = 0

for student in range(students_count):
    exam_grade = float(input())

    if exam_grade < 3:
        fail += 1
    elif exam_grade < 4:
        under_4 += 1
    elif exam_grade < 5:
        under_5 += 1
    else:
        top_students += 1

    all_grades += exam_grade

top_students_percent = top_students / students_count * 100
under_5_in_percent = under_5 / students_count * 100
under_4_in_percent = under_4 / students_count * 100
fail_percent = fail / students_count * 100
average_grade = all_grades / students_count

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {under_5_in_percent:.2f}%")
print(f"Between 3.00 and 3.99: {under_4_in_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
