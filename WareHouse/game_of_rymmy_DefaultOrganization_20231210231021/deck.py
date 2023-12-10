'''
This file contains the Deck class which represents a deck of cards.
'''
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [(rank, suit) for suit in suits for rank in ranks]
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]