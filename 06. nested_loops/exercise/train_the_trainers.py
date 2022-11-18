jury_count = int(input())

total_average_grade = 0
presentation_count = 0

command = input()

while command != "Finish":
    presentation_name = command
    presentation_count += 1
    current_grade_sum = 0

    for people in range(jury_count):
        current_grade = float(input())
        current_grade_sum += current_grade

    current_average_grade = current_grade_sum / jury_count

    print(f"{presentation_name} - {current_average_grade:.2f}.")

    total_average_grade += current_average_grade

    command = input()

total_average = total_average_grade / presentation_count

print(f"Student's final assessment is {total_average:.2f}.")
