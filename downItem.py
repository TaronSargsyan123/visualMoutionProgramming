import time

import xy
from parentItem import defaultItem
import tkinter as tk
from xy import *

class downItem(defaultItem):
    def __init__(self, root, player):
        super().__init__(root, player)
        self.xy = xy.xyClass(1, 1, 10)


    def doSomething(self, i):
        try:
            temp = self.count
            print(temp)
            print("down")

            for i in range(temp):
                self.del_rect()
                self.xy.setY(self.xy.getY() + self.xy.getSize())
                self.draw_rect()
                time.sleep(0.3)
        except:
            print("exeption")









