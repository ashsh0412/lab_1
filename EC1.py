# return whether it is before 2 or after 2
def movie_time(movie_choice):
    showtime = int(input("Showtime: 	"))
    if movie_choice == "A":
        if showtime > 4:
            print("Invalid option; please restart app...")
            exit()
        else:
            return "after 2"

    elif movie_choice == "B":
        if showtime == 1:
            return "before 2"
        elif showtime == 2:
            return "after 2"
        else:
            print("Invalid option; please restart app...")
            exit()

    elif movie_choice == "C":
        if showtime > 4:
            print("Invalid option; please restart app...")
            pass
            if showtime == 1:
                return "before 2"
            elif showtime == 2 or 3 or 4:
                return "after 2"

# return amount of adult and children ticket number            
def ticketing():
    adult_ticket = int(input("Adult tickets:	"))
    kid_ticket = int(input("Kid tickets:	"))
    if adult_ticket + kid_ticket > 30:
        print("Invalid option; please restart app...")
        pass
    else:
        return adult_ticket, kid_ticket

def calculate_ticket_price(movietime, adult_ticket_number, kid_ticket_number):
    if movietime == "before 2":
        return adult_ticket_number * 11.17 + kid_ticket_number * 8
    else:
        return adult_ticket_number * 12.45 + kid_ticket_number * 9.68

# adult : 11.17 before 2 12.45 after 2 children : 8 before 2 9.68 after 2
movie_choice = input(
    "Available movies today:\n"
    "A)12 Strong:   1)2:30  2)4:40  3)7:50  4)10:50\n"
    "B)Coco:        1)12:40 2)3:45\n"
    "C)The Post:    1)12:45 2)3:35  3)7:05  4)9:55\n"
    "Movie choice:   "
)
if movie_choice == "A":
    a = movie_time(movie_choice)
    b = ticketing()
    if b != None:
        total_price = calculate_ticket_price(a, b[0], b[1])
        print(f"Total cost: 	${total_price:.2f}")
    else:
        exit()
elif movie_choice == "B":
    a = movie_time(movie_choice)
    b = ticketing()
    if b != None:
        total_price = calculate_ticket_price(a, b[0], b[1])
        print(f"Total cost: 	${total_price:.2f}")
    else:
        exit()
elif movie_choice == "C":
    a = movie_time(movie_choice)
    b = ticketing()
    if b != None:
        total_price = calculate_ticket_price(a, b[0], b[1])
        print(f"Total cost: 	${total_price:.2f}")
    else:
        exit()
else:
    print("Invalid option; please restart app...")
    pass
