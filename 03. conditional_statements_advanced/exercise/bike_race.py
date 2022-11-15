juniors_count = int(input())
seniors_count = int(input())
track_type = input()

juniors_tax = 0
seniors_tax = 0

if track_type == "trail":
    juniors_tax = 5.5
    seniors_tax = 7

elif track_type == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.5

    if juniors_count + seniors_count >= 50:
        juniors_tax -= juniors_tax * 0.25
        seniors_tax -= seniors_tax * 0.25

elif track_type == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75

elif track_type == "road":
    juniors_tax = 20
    seniors_tax = 21.5

money_raised = (juniors_count * juniors_tax) + (seniors_count * seniors_tax)
expenses = money_raised * 0.05
donated_sum = money_raised - expenses

print(f"{donated_sum:.2f}")
