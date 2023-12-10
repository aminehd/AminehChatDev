'''
This file contains the Player class which represents a player in the Rummy game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def add_card(self, card):
        self.hand.append(card)
    def discard_card(self, index):
        return self.hand.pop(index)