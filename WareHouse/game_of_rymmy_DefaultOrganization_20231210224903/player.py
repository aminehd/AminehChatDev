'''
This file contains the Player class which represents a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw_card(self, deck):
        # Draw a card from the deck and add it to the player's hand
        card = deck.pop()
        self.hand.append(card)
    def discard_card(self, card_index):
        # Remove a card from the player's hand and return it
        card = self.hand.pop(card_index)
        return card
    # Implement other player-related methods here