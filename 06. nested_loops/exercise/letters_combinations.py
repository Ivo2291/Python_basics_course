start_letter = input()
end_letter = input()
exclusive_letter = input()

start = ord(start_letter)
end = ord(end_letter)
valid_combinations = []

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):

            if chr(i) != exclusive_letter and chr(j) != exclusive_letter and chr(k) != exclusive_letter:
                valid_combinations.append(chr(i) + chr(j) + chr(k))

print(' '.join(valid_combinations), end=' ')
print(len(valid_combinations))
