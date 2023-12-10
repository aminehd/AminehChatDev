'''
Game class for managing the 500 Rummy game.
'''
from player import Player
from deck import Deck
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.deck = Deck()  # Initialize the deck of cards
    def start(self):
        self.deck.shuffle()
        self.deal_cards()
        while not self.check_winner():
            for player in self.players:
                print(f"\n{player.name}'s turn:")
                print("Current hand:", player.hand)
                player.draw_card(self.deck)
                print("After drawing a card:", player.hand)
                card_index = self.get_valid_card_index(player)
                discarded_card = player.discard_card(card_index)
                print("After discarding a card:", player.hand)
                meld_indices = self.get_valid_meld_indices(player)
                player.meld_cards(meld_indices)
                print("After melding cards:", player.hand)
    def deal_cards(self):
        for _ in range(7):
            for player in self.players:
                card = self.deck.draw_card()
                player.hand.append(card)
    def get_valid_card_index(self, player):
        while True:
            card_index = input("Enter the index of the card to discard (0-6): ")
            try:
                card_index = int(card_index)
                if 0 <= card_index < len(player.hand):
                    break
                else:
                    print("Invalid input. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        return card_index
    def get_valid_meld_indices(self, player):
        while True:
            meld_indices = input("Enter the indices of the cards to meld (separated by spaces): ")
            try:
                meld_indices = [int(index) for index in meld_indices.split()]
                if self.is_valid_meld(player, meld_indices):
                    break
                else:
                    print("Invalid input. Please enter valid indices.")
            except ValueError:
                print("Invalid input. Please enter valid indices.")
        return meld_indices
    def is_valid_meld(self, player, meld_indices):
        melded_cards = [player.hand[index] for index in meld_indices]
        ranks = [card.rank for card in melded_cards]
        ranks.sort()
        if len(set(ranks)) == 1 or all(ranks[i] == ranks[i-1] + 1 for i in range(1, len(ranks))):
            return True
        return False
    def check_winner(self):
        for player in self.players:
            if len(player.hand) == 0 or player.calculate_points() >= 500:
                print(f"\n{player.name} wins!")
                return True
        return False