'''
Deck class for managing the deck of cards in the 500 Rummy game.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = []  # Initialize the deck of cards
        self.build()
    def build(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self):
        return self.cards.pop()