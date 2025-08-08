from blackjack.deck import Deck
from blackjack.chips import Chips
from blackjack.hand import Hand
from blackjack.utils import *

# To Control the Main Game Loop:
playing = True

# Setting up Player's Chips:
while True:
    try:
        chips = int(input('Enter Number of Chips You Want to Play With: '))

    except ValueError:
        print('Please Enter a Valid Number.')

    else:
        if chips > 500:
            print('Gambling is Bad!!! Please Gamble with a bit lesser chips.')
            continue
        else:
            player_chips = Chips(chips)
            break

# Main Game Loop:
while True:

    # Opening Statement:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until they reach 21. Aces count as 1 or 11.')

    # Creating and Shuffling The Deck.
    deck = Deck()
    deck.deck_shuffle()

    # Dealing Two Cards to Player and Dealer:
    player_hand = Hand()
    player_hand.add_card_to_hand(deck.deal_one_card())
    player_hand.add_card_to_hand(deck.deal_one_card())

    dealer_hand = Hand()
    dealer_hand.add_card_to_hand(deck.deal_one_card())
    dealer_hand.add_card_to_hand(deck.deal_one_card())

    # Asking Player for Their Bet:
    take_bet(player_chips)

    # Showing Cards (All of Player's, All except one of Dealer's)
    show_some_cards(player_hand, dealer_hand)

    while playing:

        # Asking Player to Hit or Stand:
        playing = hit_or_stand(deck, player_hand)

        # Showing Cards: (All of Player's, All except one of Dealer's)
        show_some_cards(player_hand, dealer_hand)

        # If Player's Hand value Exceeds 21, Player Busts, Break out of Loop:
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't Busted, Play Dealer's Hand until Dealer's Hand Value Exceeds Player's.
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            take_hit(deck, dealer_hand)

        # Show All Cards:
        show_all_cards(player_hand, dealer_hand)

        # Different Game Ending Scenarios:
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            game_ties(player_hand, dealer_hand)


    # Informing Player of Their Chips Amount after Game Concludes:
    print(f'\nPlayer has {player_chips.total_chips} chips.')

    # Asking Player If They Want to Play Again:
    if player_chips.total_chips <= 0:
        print('You have No Chips Left! GAME OVER!!')
        break

    else:
        if replay():
            playing = True
            continue
        else:
            print('Thanks for Playing.')
            break