budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())
video_card_price = 250

video_cards_sum = video_card_price * video_cards_count
processors_sum = (video_cards_sum * 0.35) * processors_count
ram_memory_sum = (video_cards_sum * 0.1) * ram_memory_count
total_sum = video_cards_sum + processors_sum + ram_memory_sum


if video_cards_count > processors_count:
    total_sum = total_sum * 0.85

if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")

else:
    print(f"Not enough money! You need {abs(budget - total_sum):.2f} leva more!")
