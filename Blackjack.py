import random
#from replit import clear
from art import logo

#Function that deals random cards from the list
def deal_card():
    """Returns a random card from the deck"""
    # Define the card values
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """Take a list of cards and return the score calculated form the cards"""
    #Checking if a Blackjack was achieved
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    #The ace gets a value of 1 instead of 11 if the total score is above 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#Win conditions
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"

    elif computer_score == 0:
        return "You lose, opponent has Blackjack!"

    elif user_score == 0:
        return "You win with a Blackjack!"

    elif user_score > 21:
        return "You went over 21, you lose!"

    elif computer_score > 21:
        return "Your opponent went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

#The gameplay happens here
def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    # Condition that ends the game
    game_end = False

    #This loop runs twice to give two cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #The game runs until the user decides to stop
    while not game_end:

        #Calculates the sum of the cards per player
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"     Your cards: {user_cards}, current score: {user_score}")
        print(f"     Computer's first card: {computer_cards[0]}")

        #If someone gets a score of 0 or a score higher than 21, the game ends
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True

        #If the score is still valid, the user is given the choice to draw another card.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            #Draw another card
            if user_should_deal == "y":
                user_cards.append(deal_card())

            #End the game
            else:
                game_end = True

    #The computer will draw cards depending on their score
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #The final scores are displayed
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#User can continue playing the game if they type 'y'
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    #clear()
    play_game()