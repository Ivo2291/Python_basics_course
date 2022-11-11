days_count = int(input())

doctors_count = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, days_count + 1):
    patients_count = int(input())

    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors_count += 1

    if patients_count <= doctors_count:
        treated_patients += patients_count

    else:
        untreated_patients += patients_count - doctors_count
        treated_patients += doctors_count

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
