hall_rent = int(input())

oscars_fig = hall_rent - (hall_rent * 0.3)
catering = oscars_fig - (oscars_fig * 0.15)
sound = catering / 2

total_expenses = hall_rent + oscars_fig + catering + sound

print(f"{total_expenses:.2f}")
