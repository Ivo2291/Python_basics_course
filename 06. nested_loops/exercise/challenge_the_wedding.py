men_count = int(input())
women_count = int(input())
tables_count = int(input())

counter = 0
no_more_tables = False

for m in range(1, men_count + 1):
    for w in range(1, women_count + 1):
        counter += 1

        print(f"({m} <-> {w})", end=" ")

        if counter == tables_count:
            no_more_tables = True
            break

    if no_more_tables:
        break
