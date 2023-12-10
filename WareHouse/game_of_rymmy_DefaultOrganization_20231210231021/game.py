'''
This file contains the Game class which manages the game logic.
'''
from player import Player
from deck import Deck
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.deck = Deck()
    def start(self):
        self.deck.shuffle()
        self.deal_cards()
    def deal_cards(self):
        for player in self.players:
            player.hand = self.deck.draw(7)