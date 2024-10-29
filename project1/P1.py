import project1.p1_random as p1

rng = p1.P1Random()

user_db = []
number_of_play_wins = 0
number_of_dealer_wins = 0
number_of_ties = 0
game_number = 1


def get_card():
    my_number = rng.next_int(13) + 1
    if my_number == 1:
        print("Your card is a ACE!")
        user_db.append(1)
    elif my_number == 11:
        print("Your card is a JACK!")
        user_db.append(10)
    elif my_number == 12:
        print("Your card is a QUEEN!")
        user_db.append(10)
    elif my_number == 13:
        print("Your card is a KING!")
        user_db.append(10)
    else:
        print(f"Your card is a {my_number}!")
        user_db.append(my_number)

    print(f"Your hand is: {sum(user_db)}\n")

    hand_total = sum(user_db)

    if hand_total > 21:
        print("You exceeded 21! You lose.")
        return False
    elif hand_total == 21:
        print("BLACKJACK! You win!")
        return True
    return None


def give_options():
    global number_of_play_wins, number_of_dealer_wins, number_of_ties, game_number

    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit\n")

    try:
        chosen_option = int(input("Choose an option: "))
    except ValueError:
        chosen_option = -1
    print("")

    if chosen_option == 1:
        result = get_card()
        if result is False:
            number_of_dealer_wins += 1
            start_game()
        elif result is True:
            number_of_play_wins += 1
            start_game()
        else:
            give_options()

    elif chosen_option == 2:
        dealer_number = rng.next_int(11) + 16
        print(f"Dealer's hand: {dealer_number}")
        print(f"Your hand is: {sum(user_db)}\n")

        if dealer_number > 21:
            print("You win!\n")
            number_of_play_wins += 1
        elif dealer_number > sum(user_db):
            print("Dealer wins!")
            number_of_dealer_wins += 1
        elif dealer_number < sum(user_db):
            print("You win!")
            number_of_play_wins += 1
        else:
            print("It's a tie! No one wins!")
            number_of_ties += 1

        start_game()

    elif chosen_option == 3:
        total_games = number_of_play_wins + number_of_dealer_wins + number_of_ties
        win_percentage = (
            (number_of_play_wins / total_games) * 100 if total_games > 0 else 0
        )
        print(f"Number of Player wins: {number_of_play_wins}")
        print(f"Number of Dealer wins: {number_of_dealer_wins}")
        print(f"Number of tie games: {number_of_ties}")
        print(f"Total # of games played is: {total_games}")
        print(f"Percentage of Player wins: {win_percentage:.1f}%\n")
        give_options()

    elif chosen_option == 4:
        exit()

    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.\n")
        give_options()


def start_game():
    global game_number
    user_db.clear()
    print(f"START GAME #{game_number}\n")
    game_number += 1
    get_card()
    give_options()


start_game()
