text = input()
sum_of_letters = 0

for letter in range(len(text)):
    if text[letter] == 'a':
        sum_of_letters += 1

    elif text[letter] == 'e':
        sum_of_letters += 2

    elif text[letter] == 'i':
        sum_of_letters += 3

    elif text[letter] == 'o':
        sum_of_letters += 4

    elif text[letter] == 'u':
        sum_of_letters += 5

print(sum_of_letters)
