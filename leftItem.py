import time
import tkinter as tk
from tkinter import messagebox as mb

import xy
from parentItem import defaultItem
from xy import *

class leftItem(defaultItem):
    def __init__(self, root, player):
        super().__init__(root, player)
        self.xy = xy.xyClass(1, 1, 10)

    def doSomething(self, i):
        try:
            temp = self.count
            print(temp)
            print("left")

            for i in range(temp):
                self.del_rect()
                self.xy.setX(self.xy.getX() - self.xy.getSize())
                self.draw_rect()
                time.sleep(0.3)
        except:
            print("exeption")







