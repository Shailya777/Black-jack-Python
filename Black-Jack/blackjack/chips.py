# Chips Class to maintain and keep track of Player's Chips and bets placed by Player:

class Chips:

    def __init__(self, total_chips= 100):

        self.total_chips = total_chips
        self.bet = 0

    def win_bet(self):
        self.total_chips += self.bet

    def lose_bet(self):
        self.total_chips -= self.bet

# Testing Chips Class:
if __name__== '__main__':

    c1 = Chips(1000)
    c1.bet = 200
    c1.win_bet()

    c1.bet = 500
    c1.lose_bet()

    print(c1.total_chips)