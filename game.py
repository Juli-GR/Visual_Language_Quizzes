import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from game_kitchen import *
from game_data import *
from game_scores import *

class App(tk.Tk):
    def __init__(self):

        # main setup
        super().__init__()
        self.title('Seterra but for languages')
        self.geometry('400x400')
        self.resizable(0, 0)

        # variable: which game is open
        strvar = tk.StringVar(self, "N")

        # menu
        menu = tk.Menu(self)
        games = tk.Menu(menu, tearoff = False)
        scores = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = "Games", menu = games)
        menu.add_command(label = "Scores", command = lambda: Scores(self, menu, strvar))
        self.configure(menu = menu)
        menu.entryconfig("Scores", state="disabled")

        # games
        games.add_command(label = "kitchen", command = lambda: Kitchen(self, menu, strvar))
        games.add_command(label = "body", command = lambda: print("body"))

        # main frame
        # frame = tk.Frame(self).pack(expand=True, fill="both")

        #run
        self.mainloop()

App()


"""
for widget in frame.winfo_children():
    widget.destroy()
"""


"""
# notebook
nb = ttk.Notebook(self)
games = ttk.Notebook(nb)
score = tk.Frame(nb)
games.add(tk.Label(games,text="kitchen"), text="kit")
nb.add(games, text="Games")
nb.add(score, text="Score")
nb.pack(expand=True, fill="both")
tk.Label(score,text="Scores here").pack(expand=True, fill="both")
"""