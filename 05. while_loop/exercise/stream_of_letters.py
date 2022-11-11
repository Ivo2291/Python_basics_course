c_counter = 0
o_counter = 0
n_counter = 0
word = ""

digit = input()

while digit != "End":
    if 64 < ord(digit) < 91 or 96 < ord(digit) < 123:

        if digit == "c":
            c_counter += 1
            if c_counter > 1:
                word += digit

        elif digit == "o":
            o_counter += 1
            if o_counter > 1:
                word += digit

        elif digit == "n":
            n_counter += 1
            if n_counter > 1:
                word += digit

        else:
            word += digit

        if c_counter > 0 and o_counter > 0 and n_counter > 0:
            print(word, end=" ")

            c_counter = 0
            o_counter = 0
            n_counter = 0
            word = ""

    digit = input()
