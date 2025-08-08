# Defining Helper Functions:

globals()

def take_bet(chips):
    """
    Function to ask The Player How Many Chips they want to Bet.
    Keeps asking until A valid Number is Entered and Bet Amount is lesser than The Chips The Player
    has.

    :param chips: Number of Chips Player wants to bet

    :return: None
    """

    while True:

        try:
            chips.bet = int(input('Enter The Amount of Chips you want to bet: '))

        except:
            print('Please Enter A Valid Number.')

        else:
            if chips.bet > chips.total_chips:
                print(f'You have {chips.total_chips} chips only. Please Put Down A Valid Bet.')
            else:
                break

def take_hit(deck, hand):
    """
    Function to Take a Hit (Add a Card to Their Hand from Deck) by Player / Dealer.

    This function will be called during gameplay anytime a Player requests a hit,
    or a Dealer's hand is less than Player's hand.

    Also Checks and Adjusts for Aces according to Value of The Hand.

    :param deck: Deck of Cards.
    :param hand: Hand of Player / Dealer

    :return: None
    """
    hand.add_card_to_hand(deck.deal_one_card())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    """
    Prompts the Player if They want to Hit or Stand.
    If they decide to Hit, Call the Function above.
    If they Decide to Stand, Set The GLOBAL VARIABLE PLAYING as False.

    :param deck: Deck of Cards.
    :param hand: Hand of The Player.

    :return: Boolean Value referring to Player's choice of Hit(True) or Stand(False)
    """
    while True:
        temp = input('Do you want to Hit or Stand? (Enter h or s): ')

        if temp[0].lower() == 'h':
            take_hit(deck ,hand)
            return True

        elif temp[0].lower() == 's':
            print("Player STANDS! Dealer's Turn.")
            return False

        else:
            print('Please Try Again. Enter h to Hit or s to Stand.')
            continue

def show_some_cards(player_hand, dealer_hand):
    """
    Function to Show All The Player's Cards and All Dealer's Card except one.

    When the game starts, and after each time Player takes a card,
    the dealer's first card is hidden and all of Player's cards are visible.

    Also prints value of Player's Hand.

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.

    :return: None
    """
    print("\nDealer's Hand:")
    print('<First Card Hidden>') # As we don't want to show First Card of The Dealer, Just Printing that The Card is Hidden.
    print(dealer_hand.hand[1])

    print("\nPlayer's Hand:")
    for card in player_hand.hand:
        print(card)
    print(f"Value of Player's Hand: {player_hand.value}")

def show_all_cards(player_hand, dealer_hand):
    """
    At the End Of The Game, All The Cards are Shown, both from Tne Player and The Dealer.
    Also, value of both the Hands are Shown.

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.

    :return: None
    """
    print("\nDealer's Hand:")
    for card in dealer_hand.hand:
        print(card)
    print(f"Value of Dealer's Hand: {dealer_hand.value}")

    print("\nPlayer's Hand:")
    for card in player_hand.hand:
        print(card)
    print(f"Value of Player's Hand: {player_hand.value}")


# Functions To Handle End of The Game Scenario's:

def player_busts(player_hand, dealer_hand, chips):
    """
    Function to Handle The Situation When Player Busts (Value of Player's Hand Equals or Exceed 21).

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.
    :param chips: Number of Chips Currently The Player Has.

    :return: None
    """
    print('\nPlayer BUSTS!!!')
    chips.lose_bet()

def player_wins(player_hand, dealer_hand, chips):
    """
    Function to Handle The Situation When Player Busts (Value of Player's Hand Equals or Exceed 21).

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.
    :param chips: Number of Chips Currently The Player Has.

    :return: None
    """
    print('\nPlayer WINS!!!')
    chips.win_bet()

def dealer_busts(player_hand, dealer_hand, chips):
    """
    Function to Handle The Situation When Player Busts (Value of Player's Hand Equals or Exceed 21).

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.
    :param chips: Number of Chips Currently The Player Has.

    :return: None
    """
    print('\nDealer BUSTS! Player has Won.')
    chips.win_bet()

def dealer_wins(player_hand, dealer_hand, chips):
    """
    Function to Handle The Situation When Player Busts (Value of Player's Hand Equals or Exceed 21).

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.
    :param chips: Number of Chips Currently The Player Has.

    :return: None
    """
    print('\nDealer WINS!!!')
    chips.lose_bet()

def game_ties(player_hand, dealer_hand):
    """
    Function to Handle The Situation When Player Busts (Value of Player's Hand Equals or Exceed 21).

    :param player_hand: Hand of The Player.
    :param dealer_hand: Hand of The Dealer.
    :param chips: Number of Chips Currently The Player Has.

    :return: None
    """
    print("It's a TIE!! PUSH!")

def replay():
    """
    Function to Ask The Player if They want to Continue Playing after Game Concludes.

    :return: None
    """
    while True:
        temp = input('Do you want to Continue Playing? (Enter Y: Yes, N: No)')

        if temp[0].lower() == 'y':
            return True
        elif temp[0].lower() == 'n':
            return False
        else:
            print('Please enter Y: Yes, N: No')
            continue