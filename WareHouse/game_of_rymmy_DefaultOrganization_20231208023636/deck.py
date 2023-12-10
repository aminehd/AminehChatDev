import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    def draw_card(self):
        return self.cards.pop()
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)