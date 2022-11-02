chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15

number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegan_menus = int(input())

price_of_chicken_menus = number_of_chicken_menus * chicken_menu_price
price_of_fish_menus = number_of_fish_menus * fish_menu_price
price_of_vegan_menus = number_of_vegan_menus * vegan_menu_price
total_price_of_menus = price_of_chicken_menus + price_of_fish_menus + price_of_vegan_menus

price_of_desert = (20 / 100) * total_price_of_menus
total_price_of_the_order = total_price_of_menus + price_of_desert + 2.50

print(total_price_of_the_order)
