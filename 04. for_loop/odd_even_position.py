import sys

count_of_numbers = int(input())

even_sum = 0
max_even = - sys.maxsize
min_even = sys.maxsize
odd_sum = 0
max_odd = - sys.maxsize
min_odd = sys.maxsize

for number in range(1, count_of_numbers + 1):
    current_number = float(input())

    if number % 2 != 0:
        odd_sum += current_number

        if current_number > max_odd:
            max_odd = current_number
        if current_number < min_odd:
            min_odd = current_number

    else:
        even_sum += current_number

        if current_number > max_even:
            max_even = current_number
        if current_number < min_even:
            min_even = current_number

print(f"OddSum={odd_sum:.2f},")

if min_odd == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")

if max_odd == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")

print(f"EvenSum={even_sum:.2f},")

if min_even == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")

if max_even == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")
