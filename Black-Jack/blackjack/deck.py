# Defining Deck Class:

from constants import suits, ranks
from card import Card
import random

class Deck:

    def __init__(self):

        self.new_deck = [] # Creating New Deck.

        for suit in suits:
            for rank in ranks:
                self.new_deck.append(Card(suit, rank))

    def __str__(self): # For Printing Contents of The Deck.

        content_of_deck = ''

        for card in self.new_deck:
            content_of_deck += card.__str__() + '\n'

        return 'Deck: ' + '\n' + content_of_deck

    def deal_one_card(self): # For Dealing Card on Top of The Deck to Player or Dealer.
        return self.new_deck.pop(0)

    def deck_shuffle(self):
        random.shuffle(self.new_deck)

# Testing Deck Class:
if __name__ == '__main__':

    d1 = Deck()
    print(d1)
    print('=' * 100)

    d1.deck_shuffle()
    print(d1)
    print('=' * 100)

    print(d1.deal_one_card())