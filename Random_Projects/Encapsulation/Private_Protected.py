class Protected_Private:
    def __init__(self):
        self._protectedVar = 24 #Protected variables have one prefixed underscore
        self.__privateVar = 27 #Private variables have two prefixed underscores
    def getPrivate(self):
        print(self.__privateVar)

obj = Protected_Private()
obj.getPrivate()
print(obj._protectedVar)

