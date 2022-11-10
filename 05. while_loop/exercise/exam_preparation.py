max_bad_grades = int(input())

total_problems_counter = 0
bad_grades_counter = 0
average_grade = 0
last_problem = ""
he_has_failed = False

problem_name = input()

while problem_name != "Enough":
    current_grade = int(input())

    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == max_bad_grades:
            he_has_failed = True
            break

    average_grade += current_grade
    total_problems_counter += 1
    last_problem = problem_name

    problem_name = input()

if he_has_failed:
    print(f"You need a break, {max_bad_grades} poor grades.")

else:
    average_grade /= total_problems_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems_counter}")
    print(f"Last problem: {last_problem}")
