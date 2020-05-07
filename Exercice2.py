from Exercice1  import *
class BinaryTree :

    def __init__(self, root) :
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        if node == self.__root :
            return True
        else :
            return False

    def size(self, Node):
        if Node is None :
            return 0
        else :
            return self.size(Node.getL()) +1+self.size(Node.getR())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return str(self.printValues(node.getL())) + str(self.printValues(node.getR())) + " " + str(node.getVal())

    def SumValues(self, node):
        if node is None:
            return 0
        else:
            return self.SumValues(node.getL()) + self.SumValues(node.getR()) + (node.getVal())

    def NumberLeaves(self, node) :

        if node is None :
            return 0
        elif node.getL() == None and node.getR() == None :
            return 1
        else :
            return self.NumberLeaves(node.getL()) + self.NumberLeaves(node.getR())

    def NumberInternalNodes(self, node) :
        if node is None or (node.getL() == 0 and node.getR==0):
            return 0
        else :
            return self.NumberInternalNodes(node.getL()) + self.NumberInternalNodes(node.getR()) + 1




Arbre = BinaryTree(Node(12,None,None))
Arbre.getRoot().setL(Node(5,None,None))
Arbre.getRoot().getL().setL(Node(4,None,None))
Arbre.getRoot().getL().setR(Node(6,None,None))
Arbre.getRoot().getL().getL().setL(Node(3,None,None))

Arbre.getRoot().setR(Node(17,None,None))
Arbre.getRoot().getR().setR(Node(19,None,None))
Arbre.getRoot().getR().getR().setL(Node(18,None,None))
Arbre.getRoot().getR().getR().setR(Node(21,None,None))
print("taille = ",(Arbre.size(Arbre.getRoot())))
print("Valeurs = ",Arbre.printValues(Arbre.getRoot()))
print("Somme = ",(Arbre.SumValues(Arbre.getRoot())))
print("Feuilles = ",Arbre.NumberLeaves(Arbre.getRoot()))
print("Internes = ",Arbre.NumberInternalNodes(Arbre.getRoot()))
