import sys

number_pairs = int(input())

max_diff = -sys.maxsize
pairs_are_equal = True
pairs = []

numbers = [int(input()) for num in range(number_pairs * 2)]

for i in range(0, len(numbers) - 1, 2):
    first_num = numbers[i]
    second_num = numbers[i + 1]
    result = first_num + second_num
    pairs.append(result)

for n in range(len(pairs) - 1):
    if pairs[n] != pairs[n + 1]:

        if pairs[n] + pairs[n + 1] > max_diff:
            max_diff = abs(pairs[n] - pairs[n + 1])
        pairs_are_equal = False

if pairs_are_equal:
    print(f"Yes, value={pairs[0]}")
else:
    print(f"No, maxdiff={max_diff}")
