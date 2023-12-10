'''
Main file for the 500 Rummy game.
'''
from game import Game
from player import Player
from deck import Deck
def main():
    print("Welcome to 500 Rummy!")
    game = Game()
    game.start()
if __name__ == "__main__":
    main()