# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:06:01 2020

@author: Armaghan Khan
"""

import numpy as np
from copy import deepcopy
from random import randrange

class gameBoard:
    def __init__(self):
        #words tile bag
        #BLK represent the blank tile and can be used as any letter as needed
        #game board is 15 x 15 matrix
        #BLK: 2
        self.__game_board__ = np.zeros((15, 15), dtype='int32').tolist()
        self.__tile_bag__ = {'A' : 9, 'B' : 2, 'C' : 2, 'D' : 4, 'E' : 12, 'F' : 2, 'G' : 3, 'H' : 2, 'I' : 9, 'J' : 1, 'K' : 1, 'L' : 4, 'M' : 2, 'N' : 6, 'O' : 8, 'P' : 2, 'Q' : 1, 'R' : 6, 'S' : 4, 'T' : 6, 'U' : 4, 'V' : 2, 'W' : 2, 'X' : 1, 'Y' : 2, 'Z' : 1}
        self.__tile_scores__ = {'A' : 1, 'B' : 3, 'C' : 3, 'D' : 2, 'E' : 1, 'F' : 4, 'G' : 2, 'H' : 2, 'I' : 1, 'J' : 8, 'K' : 5, 'L' : 1, 'M' : 3, 'N' : 1, 'O' : 1, 'P' : 3, 'Q' : 10, 'R' : 1, 'S' : 1, 'T' : 1, 'U' : 1, 'V' : 4, 'W' : 4, 'X' : 8, 'Y' : 4, 'Z' : 10}
        
        self.__dls_tiles__ = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), ()]
        
        self.__first_word__ = True
        
    def printGame(self):
        for x in range(15):
            for y in range(15):
                if self.__game_board__[x][y] != 0:
                    print(self.__game_board__[x][y], end=' ')
                else:
                    print(' ', end=' ')
            print()
            
    def word_placement(self, word, ind, direction):
        if word.islower():
            word = word.upper()
        word = [w for w in word]
        board = deepcopy(self.__game_board__)
        leng = len(word)
        if self.__first_word__:
            #game need to start ny making first word
            ind = [7, 7]
            #dir can be R or D
            if leng < 8:
                if direction == 'R':
                    for i in range(leng):
                        if ind[1] + 1 < 15:
                            board[ind[0]][ind[1]] = word[i]
                            ind[1] = ind[1] + 1
                        else:
                            break
                    self.__game_board__ = deepcopy(board)
                    board = None
                    self.__first_word__ = False
                    #calculating score and return
                    return [self.__caculate_score__(word), word]
                
                elif direction == 'D':
                    for i in range(leng):
                        if ind[0] + 1 < 15:
                            board[ind[0]][ind[1]] = word[i]
                            ind[0] = ind[0] + 1
                        else:
                            break
                    self.__game_board__ = deepcopy(board)
                    board = None
                    self.__first_word__ = False
                    #calculating score and return
                    return [self.__caculate_score__(word), word]
            #if-31 end
        else:
            error_code = None
            #first word is created / game has started
            if leng < 8:
                if direction == 'R':
                    consumed = []
                    fletter = word[0]
                    if fletter == board[ind[0]][ind[1]]:
                        #check if letter is being used in opposite side
                        if board[ind[0]][ind[1] - 1] != 0:
                            ind[1] = 14
                        for i in range(leng):
                            if ind[1] + 1 < 15 and board[ind[0]][ind[1]] == 0 or board[ind[0]][ind[1]] == word[i]:
                                if board[ind[0]][ind[1]] == 0:
                                    consumed.append(word[i])
                                board[ind[0]][ind[1]] = word[i]
                                ind[1] = ind[1] + 1
                            else:
                                error_code = -1
                                break
                        if error_code != -1:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            #calculating score and return
                            return [self.__caculate_score__(word), consumed]
                        else:
                            print('Word Cannot placed Here')
                            #return error code
                    else:
                        print('Word Cannot placed Here')
                        #return error code
                
                elif direction == 'D':
                    fletter = word[0]
                    consumed = []
                    if fletter == board[ind[0]][ind[1]]:
                        #check if letter is being used in opposite side
                        if board[ind[0] - 1][ind[1]] != 0:
                            ind[0] = 14
                        for i in range(leng):
                            if ind[0] + 1 < 15 and board[ind[0]][ind[1]] == 0 or board[ind[0]][ind[1]] == word[i]:
                                if board[ind[0]][ind[1]] == 0:
                                    consumed.append(word[i])
                                board[ind[0]][ind[1]] = word[i]
                                ind[0] = ind[0] + 1
                            else:
                                error_code = -1
                                break
                        if error_code != -1:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            #calculating score and return
                            return [self.__caculate_score__(word), consumed]
                        else:
                            print('Word cannot placed here')
                            #return error code
                    else:
                        print('Word Cannot placed here')
                        #return error code
                
                elif direction == 'L':
                    secind = [0, 0]
                    consumed = []
                    lletter = word[leng - 1]
                    if lletter == board[ind[0]][ind[1]]:
                        #check if letter is being used in opposite side
                        if board[ind[0]][ind[1] + 1] != 0:
                            secind[1] = 15
                        #deriving sec index
                        if ind[1] - (leng - 1) > -1 and secind[1] != 15:
                            secind = [ind[0], ind[1] - (leng - 1)]
                        else:
                            secind[1] = 14
                        for i in range(leng):
                            if secind[1] + 1 < 15 and board[secind[0]][secind[1]] == 0 or board[secind[0]][secind[1]] == word[i]:
                                if board[secind[0]][secind[1]] == 0:
                                    consumed.append(word[i])
                                board[secind[0]][secind[1]] = word[i]
                                secind[1] = secind[1] + 1
                            else:
                                error_code = -1
                                break
                        if error_code != -1:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            #calculating score and return
                            return [self.__caculate_score__(word), consumed]
                        else:
                            print('Word Cannot placed Here 1')
                            #return error code
                    else:
                        print('Word Cannot placed Here 2')
                        #return error code
                
                elif direction == 'U':
                    consumed = []
                    secind = [0, 0]
                    lletter = word[leng - 1]
                    if lletter == board[ind[0]][ind[1]]:
                        #check if letter is being used in opposite side
                        if board[ind[0] + 1][ind[1]] != 0:
                            secind[0] = 15
                        #deriving sec index
                        if ind[0] - (leng - 1) > -1 and secind[0] != 15:
                            secind = [ind[0] - (leng - 1), ind[1]]
                        else:
                            secind[0] = 14
                        for i in range(leng):
                            if secind[0] + 1 < 15 and board[secind[0]][secind[1]] == 0 or board[secind[0]][secind[1]] == word[i]:
                                if board[secind[0]][secind[1]] == 0:
                                    consumed.append(word[i])
                                board[secind[0]][secind[1]] = word[i]
                                secind[0] = secind[0] + 1
                            else:
                                error_code = -1
                                break
                        if error_code != -1:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            #calculating score and return
                            return [self.__caculate_score__(word), consumed]
                        else:
                            print('Word Cannot placed Here 1')
                            #return error code
                    else:
                        print('Word Cannot placed Here 2')
                        #return error code
    
    def __caculate_score__(self, word):
        #score calculation is without bonus
        score = 0
        for letter in word:
            letter_score = self.__tile_scores__.get(letter)
            score = score + letter_score
        return score
    
    def getLetters(self, amount):
        words = []
        amount3 = deepcopy(amount)
        unique = list(dict.fromkeys(self.__tile_bag__))
        while True:
            for x in range(0, amount):
                letter = unique[randrange(0, len(unique))]
                amount2 = self.__tile_bag__.get(letter)
                if amount2 > 0:
                    self.__tile_bag__.update({letter: amount2 - 1})
                    words.append(letter)
            if len(words) == amount3:
                return words
            else:
                amount = amount3 - len(words)
                
    def updateBag(self, words):
        words = [w.upper() for w in words]
        for x in words:
            amount = self.__tile_bag__.get(x)
            self.__tile_bag__.update({x: amount + 1})
    
def caculateScore(word):
        #score calculation is without bonus
        score = 0
        game = gameBoard()
        for letter in word:
            letter_score = game.__tile_scores__.get(letter)
            score = score + letter_score
        return score