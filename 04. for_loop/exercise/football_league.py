stadium_capacity = int(input())
fans_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(fans_count):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

sector_a_percents = sector_a / fans_count * 100
sector_b_percents = sector_b / fans_count * 100
sector_v_percents = sector_v / fans_count * 100
sector_g_percents = sector_g / fans_count * 100

all_fans_sum = sector_a + sector_b + sector_v + sector_g
all_fans_percent = all_fans_sum / stadium_capacity * 100

print(f"{sector_a_percents:.2f}%")
print(f"{sector_b_percents:.2f}%")
print(f"{sector_v_percents:.2f}%")
print(f"{sector_g_percents:.2f}%")
print(f"{all_fans_percent:.2f}%")
