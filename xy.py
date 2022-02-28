class singleton:
    __instance = None

    def __new__(cls, x, y, size, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(singleton, cls).__new__(cls)
            cls.__instance.x = x
            cls.__instance.y = y
            cls.__instance.size = size

        return cls.__instance


class xyClass(singleton):

    def __init__(self, x, y, size):
        self.__x = x
        self.__y = y
        self.__size = size


    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, value):
        self.__x = value

    def setY(self, value):
        self.__y = value



    def getSize(self):
        return self.__size

    def setSize(self, value):
        self.__size = value
