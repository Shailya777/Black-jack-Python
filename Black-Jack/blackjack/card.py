# Defining Card Class:
from constants import suits, ranks, values

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.suit + ' of ' + self.rank


# # Testing Card Class:
# if __name__ == '__main__':
#     c1 = Card('Hearts', 'Ace')
#     print(c1)
#     print(c1.value)
#     print(c1.rank)
#     print(c1.suit)