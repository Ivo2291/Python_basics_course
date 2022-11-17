number = int(input())

counter = 0

for firs_number in range(0, number + 1):
    for second_number in range(0, number + 1):
        for third_number in range(0, number + 1):
            if firs_number + second_number + third_number == number:
                counter += 1

print(counter)
