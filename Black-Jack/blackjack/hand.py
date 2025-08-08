# Defining Class Hand:

from constants import ranks, suits, values
from card import Card
from deck import Deck

class Hand:

    def __init__(self):

        self.hand = []  # Cards Player or Dealer is holding.
        self.value = 0  # Value of Player or Dealer's Hand.
        self.aces = 0   # Number of Aces Player or Dealer's Holding.

    def add_card_to_hand(self, card):

        self.hand.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self): # Aces are valued at either 1 or 11 based on current value of Hand.

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1



# Testing Hand Class:
# if __name__ == '__main__':
#
#     d1 = Deck()
#     d1.deck_shuffle()
#
#     h1 = Hand()
#     print(h1.value)
#     print(h1.aces)
#
#     # Adding A Card to Hand:
#     h1.add_card_to_hand(d1.deal_one_card())
#     print(h1.value)
#     print(h1.aces)