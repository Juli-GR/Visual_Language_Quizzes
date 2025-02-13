import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import random
import os
import time
from game_data import *

class Kitchen(tk.Frame):
    def __init__(self, parent, menu, strvar):
        super().__init__(parent)

        self.strvar = strvar

        menu.entryconfig("Scores", state="normal")
        self.strvar.set("kitchen")

        for widget in parent.winfo_children():
            if isinstance(widget, tk.Frame):
                if(widget != self):
                    widget.destroy()
        
        self.pack(expand=True, fill="both")

        self.start_time = time.time()

        # image with data
        self.im_mask = Image.open(r"Media/kitchen_mask.png")
        px = self.im_mask.load()
        px[4, 4] = (0, 0, 0)
        
        # label
        self.j = 0
        self.count = 0
        random.shuffle(kitchen_pixels)
        self.label = tk.Label(self, text = kitchen_pixels[self.j][1])
        self.label.pack()

        # image
        self.im_original = Image.open('Media/kitchen.png')
        self.im_tk = ImageTk.PhotoImage(self.im_original)
        self.im = ttk.Label(self, text = 'kitchen', image = self.im_tk)
        self.im.pack()
        self.im.bind("<Button 1>", self.click)

        self.done = []

    def click(self, event):
        x = event.x
        y = event.y
        coor = self.im_mask.getpixel( (x,y) )

        # esta parte esta fea
        # se pueden mejorar/sacar los if y for mepa
        # esta todo a la mitad!

        self.lenght = len(kitchen_pixels)
        if (coor[0]==0 and coor[1]==0 and coor[3]==255 and coor[2]<=255 and coor[2]> 255-self.lenght \
            and coor not in self.done):  # color valido
            for j in kitchen_pixels:
                if j[0] == coor:
                    i = j

            self.done.append(kitchen_pixels[self.j][0])

            if (i[1]==kitchen_pixels[self.j][1]):
                self.count += 1

            png = Image.open("Media/" + str(kitchen_pixels[self.j][0][2]) + ".png")
            new = Image.new('RGBA', (400, 400), (0,0,0,255))
            new.paste(self.im_original,(0,0))
            new.alpha_composite(png,(0,0))
            self.im_original = new

            self.im_tk = ImageTk.PhotoImage(new)
            self.im.configure(image=self.im_tk)
            self.im.image = self.im_tk
            self.j += 1
            
            if(self.j< self.lenght):
                self.label.configure(text = kitchen_pixels[self.j][1])
            else:
                self.show_score()
    
    def show_score(self):

        # display score
        self.im.destroy()
        self.label.destroy()
        self.pack_forget()
        self.pack(expand=True)
        score = 100*self.count/self.lenght
        l1 = ttk.Label(self, text = "Score:", font = 'Helvetica 20', anchor="center")
        l2 = ttk.Label(self, text = str(int(score)) + "%", font = 'Helvetica 40 bold', anchor="center")
        l1.pack(expand=True, fill="both")
        l2.pack(expand=True, fill="both")

        # save score
        file_name = "score_" + self.strvar.get() + ".txt"
        h = int(time.time()-self.start_time)
        h1 = str(h//60)
        h2 = str(int(h%60))
        if(len(h1)==1):
            h1 = '0' + h1
        if(len(h2)==1):
            h2 = '0' + h2
        h = h1 + ':' + h2
        score_txt = datetime.now().strftime('%Y-%m-%d %H:%M ') + h + " " + str(int(score)) + "%\n"
        with open(file_name, 'a') as f:
            f.write(score_txt)

        # remove a line if there are more than 10
        if(os.path.getsize(file_name) >= 27*11):
            with open(file_name, 'r') as f:
                data = f.read().splitlines(True)
            with open(file_name, 'w') as f:
                f.writelines(data[1:])



""" Superponer imagenes:
chan = Image.open(r'chandler.png')
bart = Image.open(r'bart.png')
bg = Image.new('RGBA', (400, 400), (0,0,0,255))
bg.paste(chan,(0,0))
bg.alpha_composite(bart,(0,0))
bg.save('c.png')

https://stackoverflow.com/questions/3482081/how-to-update-the-image-of-a-tkinter-label-widget
"""
