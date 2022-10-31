pens_pack = 5.80
markers_pack = 7.20
detergent = 1.20

number_of_pen_packs = int(input())
number_of_marker_packs = int(input())
liters_of_detergent = int(input())
discount = int(input())

price_of_pen_packs = number_of_pen_packs * pens_pack
price_of_marker_packs = number_of_marker_packs * markers_pack
price_of_detergent = liters_of_detergent * detergent

price_for_all_materials = price_of_pen_packs + price_of_marker_packs + price_of_detergent
price_with_discount = price_for_all_materials - (price_for_all_materials * (discount / 100))

print(price_with_discount)
