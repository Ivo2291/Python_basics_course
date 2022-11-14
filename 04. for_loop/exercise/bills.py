months = int(input())

electricity = 0
water = 0
internet = 0
other = 0

for month in range(months):
    electricity_bill = float(input())

    electricity += electricity_bill
    water += 20
    internet += 15
    other_sum = electricity_bill + 20 + 15
    other += other_sum + (other_sum * 0.2)

total_sum_for_bills = electricity + water + internet + other
average_sum_for_month = total_sum_for_bills / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average_sum_for_month:.2f} lv")
