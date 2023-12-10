'''
This is the main file for the 2 player game of 500 rummy.
'''
import tkinter as tk
from game import Game
class GameGUI:
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()
        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack()
    def start_game(self):
        self.game.start()
        self.update_canvas()
        self.master.bind("<Button-1>", self.handle_click)
    def update_canvas(self):
        self.canvas.delete("all")
        self.canvas.create_text(400, 50, text=f"It's {self.game.current_player.name}'s turn.")
        self.canvas.create_text(400, 100, text=f"{self.game.current_player.name}'s hand: {self.game.current_player.hand}")
        self.canvas.create_text(400, 150, text=f"{self.game.opponent.name}'s hand: {self.game.opponent.hand}")
    def handle_click(self, event):
        if self.game.current_player == self.game.player1:
            card_index = event.y // 20
            if card_index < len(self.game.player1.hand):
                card = self.game.player1.discard_card(card_index)
                self.game.opponent.draw_card(card)
                self.update_canvas()
                if len(self.game.player1.hand) == 0:
                    self.canvas.create_text(400, 200, text=f"{self.game.player1.name} wins!")
        elif self.game.current_player == self.game.player2:
            card_index = event.y // 20
            if card_index < len(self.game.player2.hand):
                card = self.game.player2.discard_card(card_index)
                self.game.player1.draw_card(card)
                self.update_canvas()
                if len(self.game.player2.hand) == 0:
                    self.canvas.create_text(400, 200, text=f"{self.game.player2.name} wins!")
        self.game.current_player, self.game.opponent = self.game.opponent, self.game.current_player
if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()