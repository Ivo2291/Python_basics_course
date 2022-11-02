deposited_amount = float(input())
term_of_the_deposit = int(input())
annual_interest_rate_in_moths = float(input())

accrued_interest = deposited_amount * (annual_interest_rate_in_moths / 100)
interest_for_month = accrued_interest / 12
total_price = deposited_amount + term_of_the_deposit * interest_for_month

print(total_price)
