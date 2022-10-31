mackerel_price_kg = float(input())
sprat_price_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_price_per_kg = mackerel_price_kg + (mackerel_price_kg * 0.60)
bonito_sum = bonito_kg * bonito_price_per_kg
horse_mackerel_price_kg = sprat_price_kg + (sprat_price_kg * 0.80)
horse_mackerel_sum = horse_mackerel_kg * horse_mackerel_price_kg
mussels_price_kg = 7.50
mussels_sum = mussels_kg * mussels_price_kg

total_sum = bonito_sum + horse_mackerel_sum + mussels_sum

print(f"{total_sum:.2f}")
