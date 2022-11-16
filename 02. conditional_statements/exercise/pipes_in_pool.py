pool_capacity = int(input())
first_pipe_for_hour = int(input())
second_pipe_for_hour = int(input())
hours_without_worker = float(input())

first_pipe_debit = first_pipe_for_hour * hours_without_worker
second_pipe_debit = second_pipe_for_hour * hours_without_worker
total_filled = first_pipe_debit + second_pipe_debit
percent_first_pipe = first_pipe_debit / total_filled * 100
percent_second_pipe = second_pipe_debit / total_filled * 100
total_percent_filled = total_filled / pool_capacity * 100
difference = abs(total_filled - pool_capacity)

if total_filled <= pool_capacity:
    print(f"The pool is {total_percent_filled:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%./"
          f" Pipe 2: {percent_second_pipe:.2f}%.")
else:
    print(f"For {hours_without_worker:.2f} hours the pool overflows with {difference:.2f} liters.")
