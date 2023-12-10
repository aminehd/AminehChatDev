'''
This file contains the Game class which represents the Rummy game.
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
        self.play()
    def deal_cards(self):
        for _ in range(7):
            for player in self.players:
                card = self.deck.draw_card()
                player.add_card(card)
    def play(self):
        while True:
            for player in self.players:
                self.display_game_state()
                self.take_turn(player)
                if self.check_win(player):
                    self.display_winner(player)
                    return
    def display_game_state(self):
        print("----- Game State -----")
        for player in self.players:
            print(f"{player.name}: {player.hand}")
    def take_turn(self, player):
        print(f"\n{player.name}'s turn:")
        print(f"Your hand: {player.hand}")
        while True:
            try:
                card_index = int(input("Choose a card to discard: "))
                if card_index < 0 or card_index >= len(player.hand):
                    print("Invalid card index. Please choose a valid index.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid card index.")
        discarded_card = player.discard_card(card_index)
        print(f"{player.name} discarded {discarded_card}")
    def check_win(self, player):
        return len(player.hand) == 0
    def display_winner(self, player):
        print(f"\n{player.name} wins!")