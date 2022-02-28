from threading import Thread
from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

import xy
from scrolledFrame import VerticalScrolledFrame

from leftItem import leftItem
from rightItem import rightItem
from upItem import upItem
from downItem import downItem
from xy import *


class AppMainWindow:
    def __init__(self):
        print("[INFO]: init start...")
        self.__count = 0
        self.tempCount = 1


        self.colorOne = "#FFFFFF"
        self.colorTwo = "#E1E5ED"
        self.colorText = "#4D7992"
        self.colorGreen = "#00ED60"
        self.colorYellow = "#FFB106"
        self.colorRed = "#FF194B"

        self.initWindow()
        #self.insertCount()

        self.itemsList = []

        print("[INFO]: init ending...")


    def initWindow(self):
        self.__width = 1000
        self.__height = 600

        self.startWindow()
        self.createWidgets()
        self.place()

        self.xy = xy.xyClass(1, 1, 10)


        self.player = self.playgroundCanvas.create_rectangle

        self.player((self.xy.getX(), self.xy.getY(), self.xy.getX() + self.xy.getSize(), self.xy.getY() + self.xy.getSize()))



    def getCount(self):
        return self.__count

    def setCount(self, count):
        self.__count = count

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height


    def createWidgets(self):


        self.playIMG = (Image.open("sprites/play.png"))
        self.stopIMG = (Image.open("sprites/stop.png"))

        self.rotateIMG = (Image.open("sprites/left.png"))
        self.upIMG = (Image.open("sprites/up.png"))
        self.downIMG = (Image.open("sprites/down.png"))
        self.openIMG = (Image.open("sprites/right.png"))

        self.rotateResize = self.rotateIMG.resize((50, 50), Image.ANTIALIAS)
        self.rotate50x50 = ImageTk.PhotoImage(self.rotateResize)

        self.upResize = self.upIMG.resize((50, 50), Image.ANTIALIAS)
        self.up50x50 = ImageTk.PhotoImage(self.upResize)

        self.downResize = self.downIMG.resize((50, 50), Image.ANTIALIAS)
        self.down50x50 = ImageTk.PhotoImage(self.downResize)

        self.openResize = self.openIMG.resize((50, 50), Image.ANTIALIAS)
        self.open50x50 = ImageTk.PhotoImage(self.openResize)

        self.playResize = self.playIMG.resize((50, 50), Image.ANTIALIAS)
        self.play50x50 = ImageTk.PhotoImage(self.playResize)

        self.stopResize = self.stopIMG.resize((50, 50), Image.ANTIALIAS)
        self.stop50x50 = ImageTk.PhotoImage(self.stopResize)

        self.allCanvas = tk.Canvas(self.window, bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)

        self.canvas = tk.Canvas(self.window, bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)

        self.playgroundCanvas =tk.Canvas(self.window, bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)

        self.canvasFooter = tk.Canvas(self.canvas, bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)

        self.canvasHeader = tk.Canvas(self.canvas, bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)


        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", relief=tk.FLAT, foreground="#4D7992",
                             background=self.colorTwo, fieldbackground="#27292D",
                             darkcolor="#27292D", lightcolor="#27292D", selectbackground="#27292D",
                             selectforeground="#27292D", bordercolor="#27292D", insertcolor="#27292D",
                             insertwidth="#27292D", arrowsize="#27292D", arrowcolor="#4D7992")

        self.scrallCanvas = tk.Canvas(self.canvas, relief=tk.FLAT, bg=self.colorTwo)
        self.scframe = VerticalScrolledFrame(self.scrallCanvas)

        self.createLeftItemButton = tk.Button(self.canvasHeader, relief=tk.FLAT, bg=self.colorTwo, image=self.rotate50x50, command=self.createLeftItem)

        self.createRightItemButton = tk.Button(self.canvasHeader, relief=tk.FLAT, bg=self.colorTwo, image=self.open50x50, command=self.createRightItem)

        self.createForwardItemButton = tk.Button(self.canvasHeader, relief=tk.FLAT, bg=self.colorTwo, image=self.up50x50, command=self.createForwardItem)

        self.createBackItemButton = tk.Button(self.canvasHeader, relief=tk.FLAT, bg=self.colorTwo, image=self.down50x50, command=self.createBackItem)

        self.playButton = tk.Button(self.canvasFooter, relief=tk.FLAT, bg=self.colorTwo, image=self.play50x50, command=self.playBtn)

        self.clearePlaygroundButton = tk.Button(self.playgroundCanvas, relief=tk.FLAT, bg=self.colorTwo, image=self.down50x50,)

    def place(self):
        self.canvas.pack(expand=0, fill=BOTH, side=LEFT)

        self.canvasFooter.pack(side=BOTTOM)
        self.canvasHeader.pack()

        self.scrallCanvas.pack(expand=1, fill=BOTH)
        self.scframe.pack(fill=BOTH, side=TOP, expand=1)

        self.playgroundCanvas.pack(expand=1, fill=BOTH)

        self.playButton.pack()
        self.createLeftItemButton.pack(side=LEFT, padx=(20, 10))
        self.createRightItemButton.pack(side=LEFT, padx=(10, 10))
        self.createForwardItemButton.pack(side=LEFT, padx=(10, 10))
        self.createBackItemButton.pack(side=LEFT, padx=(10, 20))
        self.clearePlaygroundButton.pack(anchor=E, padx=(0, 5), pady=(0, 5), side=BOTTOM)

    def startWindow(self):
        self.window = tk.Tk()
        self.window.geometry(str(self.getWidth()) + "x" + str(self.getHeight()))
        self.window.title("test")
        #self.window.resizable(False, False)
        self.window["bg"] = self.colorTwo
        self.window.bind('<Escape>', lambda e: self.window.quit())





    def playCommand(self):
        if len(self.itemsList) > 0:
            for item in self.itemsList:
                item.clear()
                del item
            self.playButton.configure(image=self.stop50x50)

            i = 0
            for item in self.itemsList:
                i = i+1
                item.doSomething(i)
                print(self.xy.getX())
                print(self.xy.getY())

            self.playButton.configure(image=self.play50x50)


        else:
            print("test")

    def playBtn(self):
        self.thread = Thread(target=self.playCommand)
        self.thread.start()



    def createLeftItem(self):
        temp = leftItem(self.scframe.interior, self.player)
        self.itemsList.append(temp)
        print(self.itemsList)


    def createRightItem(self):
        temp = rightItem(self.scframe.interior, self.player)
        self.itemsList.append(temp)
        print(self.itemsList)


    def createForwardItem(self):
        temp = upItem(self.scframe.interior, self.player)
        self.itemsList.append(temp)
        print(self.itemsList)


    def createBackItem(self):
        temp = downItem(self.scframe.interior, self.player)
        self.itemsList.append(temp)
        print(self.itemsList)
