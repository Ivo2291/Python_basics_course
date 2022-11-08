open_tabs = int(input())
salary = int(input())

fine = 0

for sites in range(open_tabs):
    site_name = input()

    if site_name == "Facebook":
        fine = 150
    elif site_name == "Instagram":
        fine = 100
    elif site_name == "Reddit":
        fine = 50
    else:
        fine = 0

    salary -= fine

if salary <= 0:
    print("You have lost your salary.")

else:
    print(salary)
