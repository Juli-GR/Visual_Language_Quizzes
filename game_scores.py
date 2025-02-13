import tkinter as tk
from tkinter import ttk

class Scores(tk.Frame):
    def __init__(self, parent, menu, strvar):
        super().__init__(parent)

        menu.entryconfig("Scores", state="disabled")

        for widget in parent.winfo_children():
            if isinstance(widget, tk.Frame):
                if(widget != self):
                    widget.destroy()

        self.pack(expand=True, fill="both")

        date = ""
        time = ""
        score = ""
        try:
            file_name = "score_" + strvar.get() + ".txt"
            with open(file_name, 'r') as f:
                for line in f:
                    data = line.split()
                    date = data[0] + " " + data[1] + "\n" + date
                    time = data[2] + "\n" + time
                    score = data[3] + "\n" + score
            if date!="":
                date = "DATE\n" + date[:-1]
                score = "SCORE\n" + score[:-1]
                time = "TIME\n" + time[:-1]
        except FileNotFoundError:
            l = ttk.Label(self, text = "It seems like you haven't\nplayed this game yet", \
                font = '12', anchor="center", justify="center")
            l.pack(expand=True, fill="both")
            return
            
        font2 = ("Noto Sans Mono CJK SC", 12)
        
        fr = tk.Frame(self)
        l0 = tk.Label(fr, text=strvar.get().upper(), font = ('Helvetica', 18), anchor="center", justify="center")
        l1 = tk.Label(fr, text = date, font = font2, anchor="center", justify="center")
        l2 = tk.Label(fr, text = time, font = font2, anchor="center", justify="center")
        l3 = tk.Label(fr, text = score, font = font2, anchor="center", justify="center")
        l0.pack(expand=True, fill="both", pady=10)
        l1.pack(expand=True, fill="both", side=tk.LEFT, pady=10)
        l2.pack(expand=True, fill="both", side=tk.LEFT, pady=10)
        l3.pack(expand=True, fill="both", side=tk.LEFT, pady=10)
        fr.pack(expand=True, fill="x")
