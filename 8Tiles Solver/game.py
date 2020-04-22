# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:58:55 2020

@author: Armaghan Khan
"""

from copy import deepcopy

class game:
    def __init__(self, matrix, size):
        #0 represent blank space
#        self.__game__ = [[1, 2, 4],
#                         [3, 0, 6],
#                         [7, 8, 5]]
#
#        self.__blankSpace__ = [1, 1]
#        #represent size of game matrix size * size
#        self.__size__ = 3
        self.__game__ = deepcopy(matrix)
        self.__size__ = deepcopy(size)
        self.__blankSpace__ = deepcopy(self.findBlankPivot(matrix, size))
        
        
    def findBlankPivot(self, matrix, size):
        try:
            index = []
            for x in range(size):
                for y in range(size):
                    if matrix[x][y] == 0:
                        index = [x, y]
                        break
            if index != []:
                return index
            return None
        except:
            print("invalid size")
            return None

    def printGame(self):
        for x in self.__game__:
            for y in x:
                print(y, end="     ")
            print()

    def moveUp(self):
        blankSpace = deepcopy(self.__blankSpace__)
        game = deepcopy(self.__game__)
        sec = None
        possible = False
        moved = blankSpace[0] - 1
        if moved < self.__size__ and moved > -1:
            sec = [moved, blankSpace[1]]
            possible = True
            
        if possible:
            #swap the values
            game[sec[0]][sec[1]], game[blankSpace[0]][blankSpace[1]] = game[blankSpace[0]][blankSpace[1]], game[sec[0]][sec[1]]
            return game
        return None

    def moveDown(self):
        blankSpace = deepcopy(self.__blankSpace__)
        game = deepcopy(self.__game__)
        sec = None
        possible = False
        moved = blankSpace[0] + 1
        if moved < self.__size__ and moved > -1:
            sec = [moved, blankSpace[1]]
            possible = True
            
        if possible:
            #swap the values
            game[sec[0]][sec[1]], game[blankSpace[0]][blankSpace[1]] = game[blankSpace[0]][blankSpace[1]], game[sec[0]][sec[1]]
#            self.__blankSpace__ = sec
            return game
        return None

    def moveRight(self):
        blankSpace = deepcopy(self.__blankSpace__)
        game = deepcopy(self.__game__)
        sec = None
        possible = False
        moved = blankSpace[1] + 1
        if moved < self.__size__ and moved > -1:
            sec = [blankSpace[0], moved]
            possible = True
            
        if possible:
            #swap the values
            game[sec[0]][sec[1]], game[blankSpace[0]][blankSpace[1]] = game[blankSpace[0]][blankSpace[1]], game[sec[0]][sec[1]]
            #self.__blankSpace__ = sec
            return game
        return None

    def moveLeft(self):
        blankSpace = deepcopy(self.__blankSpace__)
        game = deepcopy(self.__game__)
        sec = None
        possible = False
        moved = blankSpace[1] - 1
        if moved < self.__size__ and moved > -1:
            sec = [blankSpace[0], moved]
            possible = True
            
        if possible:
            #swap the values
            game[sec[0]][sec[1]], game[blankSpace[0]][blankSpace[1]] = game[blankSpace[0]][blankSpace[1]], game[sec[0]][sec[1]]
#            self.__blankSpace__ = sec
            return game
        return None
    
    def canMoveUp(self):
        possible = False
        moved = self.__blankSpace__[0] - 1
        if moved < self.__size__ and moved > -1:
            possible = True
        return possible
    
    def canMoveDown(self):
        possible = False
        moved = self.__blankSpace__[0] + 1
        if moved < self.__size__ and moved > -1:
            possible = True
        return possible
    
    def canMoveLeft(self):
        possible = False
        moved = self.__blankSpace__[1] - 1
        if moved < self.__size__ and moved > -1:
            possible = True
        return possible
    
    def canMoveRight(self):
        possible = False
        moved = self.__blankSpace__[1] + 1
        if moved < self.__size__ and moved > -1:
            possible = True
        return possible
    
    def getValue(self):
        return self.__game__