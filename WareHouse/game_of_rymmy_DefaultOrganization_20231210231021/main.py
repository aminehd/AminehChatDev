'''
This is the main file that runs the 2 player game of 500 rummy.
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
        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.quit_button.pack()
    def start_game(self):
        self.game.start()
        self.draw_cards_on_canvas()
    def quit_game(self):
        self.master.destroy()
    def draw_cards_on_canvas(self):
        self.canvas.delete("all")  # Clear the canvas
        x = 50
        y = 50
        card_width = 50
        card_height = 80
        for player in self.game.players:
            for card in player.hand:
                self.canvas.create_rectangle(x, y, x + card_width, y + card_height, fill="white")
                self.canvas.create_text(x + 5, y + 5, text=card, anchor=tk.NW)
                x += card_width + 10
            y += card_height + 10
            x = 50
if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()