import time
import tkinter as tk
from tkinter import messagebox as mb

import xy
from xy import *

class defaultItem:
    def __init__(self, root, player):
        self.__root = root
        self.xy = xy.xyClass(1, 1, 10)

        self.player = player
        self.text = "item"

        self.count = 1

        self.colorOne = "#FFFFFF"
        self.colorTwo = "#E1E5ED"
        self.colorText = "#4D7992"
        self.colorGreen = "#00ED60"
        self.colorYellow = "#FFB106"
        self.colorRed = "#FF194B"

        self.tick1 = r"C:\Users\Dell\Desktop\sound1.mp3"
        self.tick2 = r"C:\Users\Dell\Desktop\sound2.mp3"



        self.createWidjets()
        self.place()


    def getRoot(self):
        return self.__root

    def setRoot(self, value):
        self.__root = value



    def createWidjets(self):
        self.canvas = tk.Canvas(self.getRoot(), bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0, height=3, width=20)
        #self.nameLable = tk.Label(self.canvas, text=self.text, height=2, width=30)
        self.lable = tk.Label(self.canvas, text=str(self.count), height=2, width=10)
        self.plusButton = tk.Button(self.canvas, text="+", command=self.plusButtonCommand, height=2, width=5)
        self.minusButton = tk.Button(self.canvas, text="-", command=self.minusButtonCommand, height=2, width=5)

    def place(self):
        self.canvas.pack(padx=10, pady=5)
        self.plusButton.pack(side=tk.LEFT)
        self.lable.pack(side=tk.LEFT)
        self.minusButton.pack(side=tk.LEFT)

    def checkClear(self):
        answer = mb.askyesno(title="answer", message="do you want to delete " + self.text + " ?")
        if answer:
            self.clear()


    def clear(self):
        self.canvas.destroy()

    def draw_rect(self):
        self.player((self.xy.getX(), self.xy.getY(), self.xy.getX() + self.xy.getSize(), self.xy.getY() + self.xy.getSize()), fill="#4D7992")

    def del_rect(self):
        self.player(self.xy.getX(), self.xy.getY(), self.xy.getX() + self.xy.getSize(), self.xy.getY() + self.xy.getSize(), fill="#FFFFFF")

    def plusButtonCommand(self):
        self.count += 1
        self.lable.config(text=str(self.count))

    def minusButtonCommand(self):
        if self.count > 1:
            self.count -= 1
            self.lable.config(text=str(self.count))






