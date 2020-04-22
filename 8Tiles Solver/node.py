# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:33:26 2020

@author: Armaghan Khan
"""

class node:
    def __init__(self, *args):
        lenargs = len(args)
        if lenargs < 2 and lenargs > 3:
            raise TypeError("Requires 2 or 3 arguments")
        elif lenargs == 2:
            self.__matrix__ = args[0]
            self.__path__ = args[1]
            self.__cost__ = None
        elif lenargs == 3:
            self.__matrix__ = args[0]
            self.__path__ = args[1]
            self.__cost__ = args[2]
        
    def getMatrix(self):
        return self.__matrix__
    
    def getPath(self):
        return self.__path__
    
    def getCost(self):
        if self.__cost__ is not None:
            return self.__cost__
        else:
            raise TypeError("Cost Not Defined")
    
    def find(self, array):
        #array must be list of node datatype
        for x in array:
            if self.getMatrix() == x.getMatrix():
                return True
        return False
    
    def printNode(self):
        print()
        print("Node Matrix: ", self.getMatrix())
#        print("Node Path: ", self.getPath())
        print("Node Cost: ", self.getCost())
        print()
        return ("\n Node Matrix: {} \n Node Cost: {} \n Node Path: {} \n".format(self.getMatrix(), self.getCost(), self.getPath()))