import random, os, art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the desk"""
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lost, oponent has BlackJack!"
    elif user_score == 0:
        return "You win!"
    elif user_score > 21:
        return "You went over 21!"
    elif computer_score > 21:
        return "Computer went over 21!"
    elif user_score > computer_score:
        return " You win!"
    else: 
        return "You lose."

def play_game():
    print(art.logo)
    print()
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards} and score {user_score}.")
        print(f"Computer's first card {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal = input("Another card (Y/N): ").lower()
            if deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print()
    print(f"Your final hand is: {user_cards}, final score: {user_score}.")
    print(f"Computer's final hand is: {computer_cards}, final score: {computer_score}.")
    print(compare(user_score, computer_score))
    print()

while input("Do you want to play a game of BlackJack (Y/N): ").lower() == "y":
    os.system('clear')
    play_game()
   