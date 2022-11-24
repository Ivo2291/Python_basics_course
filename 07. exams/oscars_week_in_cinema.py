film_name = input()
hall_type = input()
purchased_tickets = int(input())

ticket_price = 0

if hall_type == "normal":
    if film_name == "A Star Is Born":
        ticket_price = 7.5

    elif film_name == "Bohemian Rhapsody":
        ticket_price = 7.35

    elif film_name == "Green Book":
        ticket_price = 8.15

    elif film_name == "The Favourite":
        ticket_price = 8.75

elif hall_type == "luxury":
    if film_name == "A Star Is Born":
        ticket_price = 10.5

    elif film_name == "Bohemian Rhapsody":
        ticket_price = 9.45

    elif film_name == "Green Book":
        ticket_price = 10.25

    elif film_name == "The Favourite":
        ticket_price = 11.55

elif hall_type == "ultra luxury":
    if film_name == "A Star Is Born":
        ticket_price = 13.5

    elif film_name == "Bohemian Rhapsody":
        ticket_price = 12.75

    elif film_name == "Green Book":
        ticket_price = 13.25

    elif film_name == "The Favourite":
        ticket_price = 13.95

income = ticket_price * purchased_tickets

print(f"{film_name} -> {income:.2f} lv.")
