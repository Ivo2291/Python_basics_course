meters_that_will_be_landscaped = float(input())
price_for_landscaping_all_areas = meters_that_will_be_landscaped * 7.61
discount = price_for_landscaping_all_areas * 0.18
total_price = price_for_landscaping_all_areas - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
