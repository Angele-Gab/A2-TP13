class Node :

    def __init__(self, val, right, left) :
        self.__val = val
        self.__R = right
        self.__L = left

    def getVal(self):
        return self.__val

    def getR(self):
        return self.__R

    def getL(self):
        return self.__L

    def setVal(self,a):
        self.__val = a

    def setR(self,a) :
        self.__R = a

    def setL(self,a):
        self.__L = a


    def __str__(self):
        return str(self.__val)

New = Node(3,7,10)
#print(New.getVal())
New.setL(3)
New.setR(10)
#print(New)


