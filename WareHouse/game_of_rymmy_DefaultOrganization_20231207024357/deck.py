'''
This file contains the Deck class which represents a deck of cards in the Rummy game.
'''
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(f"{rank} of {suit}")
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self):
        return self.cards.pop()