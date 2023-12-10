'''
This file contains the Game class which represents the game logic.
'''
import random
from player import Player
class Game:
    def __init__(self):
        self.deck = []
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.opponent = None
    def start(self):
        # Initialize the deck and players
        self.initialize_deck()
        self.initialize_players()
        self.current_player = self.player1
        self.opponent = self.player2
    def initialize_deck(self):
        # Create and shuffle the deck
        suits = ['H', 'D', 'C', 'S']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = [suit + rank for suit in suits for rank in ranks]
        random.shuffle(self.deck)
    def initialize_players(self):
        # Create two players
        player1_name = input("Enter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
    def play_round(self):
        # Play a round of the game
        while True:
            print(f"It's {self.current_player.name}'s turn.")
            print(f"{self.current_player.name}'s hand: {self.current_player.hand}")
            print(f"{self.opponent.name}'s hand: {self.opponent.hand}")
            card_index = int(input("Enter the index of the card you want to discard: "))
            card = self.current_player.discard_card(card_index)
            self.opponent.draw_card(card)
            if len(self.current_player.hand) == 0:
                print(f"{self.current_player.name} wins!")
                break
            self.current_player, self.opponent = self.opponent, self.current_player
    # Implement other game-related methods here