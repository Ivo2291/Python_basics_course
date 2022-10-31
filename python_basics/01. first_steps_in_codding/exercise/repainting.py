protective_nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

needed_quantity_of_nylon = int(input())
needed_quantity_of_paint = int(input())
quantity_of_paint_thinner = int(input())
needed_time_for_work = int(input())

nylon_amount = (needed_quantity_of_nylon + 2) * protective_nylon_price
paint_amount = (needed_quantity_of_paint + (needed_quantity_of_paint * 10 / 100)) * paint_price
paint_thinner_amount = quantity_of_paint_thinner * paint_thinner_price

total_amount_for_materials = nylon_amount + paint_amount + paint_thinner_amount + 0.40
workers_amount = (total_amount_for_materials * (30 / 100)) * needed_time_for_work

total_amount = total_amount_for_materials + workers_amount

print(total_amount)
