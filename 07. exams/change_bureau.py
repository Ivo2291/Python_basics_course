count_of_bitcoins = int(input())
count_of_yans = float(input())
commission = float(input())

bitcoin_price_in_lv = 1168
yan_price_in_usd = 0.15
usd_price_in_lv = 1.76
euro_price_in_lv = 1.95

bitcoins_sum = count_of_bitcoins * bitcoin_price_in_lv
yans_sum = (count_of_yans * yan_price_in_usd) * usd_price_in_lv
euro_sum = (bitcoins_sum + yans_sum) / euro_price_in_lv
euro_with_commission = (euro_sum * commission) / 100
total_euro = euro_sum - euro_with_commission

print(f"{total_euro:.2f}")
