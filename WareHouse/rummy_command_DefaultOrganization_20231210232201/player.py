'''
Player class for managing a player in the 500 Rummy game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # Initialize the player's hand
    def draw_card(self, deck):
        card = deck.draw_card()
        self.hand.append(card)
    def discard_card(self, card_index):
        card = self.hand.pop(card_index)
        return card
    def meld_cards(self, meld_indices):
        melded_cards = [self.hand.pop(index) for index in sorted(meld_indices, reverse=True)]
        self.hand.extend(melded_cards)
    def calculate_points(self):
        points = 0
        for card in self.hand:
            if card.rank in ["J", "Q", "K"]:
                points += 10
            elif card.rank == "A":
                points += 15
            else:
                points += int(card.rank)
        return points