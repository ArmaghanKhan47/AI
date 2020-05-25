# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:06:01 2020

@author: Armaghan Khan
"""

import numpy as np
from copy import deepcopy
from random import randrange

class gameBoard:
    def __init__(self, mode = 1):
        #words tile bag
        #BLK represent the blank tile and can be used as any letter as needed
        #game board is 15 x 15 matrix
        #BLK: 2
        #mode 1 -> score calculation without bonus (default)
        #mode 2 -> score calculation with bonus
        self.__game_board__ = np.zeros((15, 15), dtype='int32').tolist()
        self.__tile_bag__ = {'A' : 9, 'B' : 2, 'C' : 2, 'D' : 4, 'E' : 12, 'F' : 2, 'G' : 3, 'H' : 2, 'I' : 9, 'J' : 1, 'K' : 1, 'L' : 4, 'M' : 2, 'N' : 6, 'O' : 8, 'P' : 2, 'Q' : 1, 'R' : 6, 'S' : 4, 'T' : 6, 'U' : 4, 'V' : 2, 'W' : 2, 'X' : 1, 'Y' : 2, 'Z' : 1}
        self.__tile_scores__ = {'A' : 1, 'B' : 3, 'C' : 3, 'D' : 2, 'E' : 1, 'F' : 4, 'G' : 2, 'H' : 2, 'I' : 1, 'J' : 8, 'K' : 5, 'L' : 1, 'M' : 3, 'N' : 1, 'O' : 1, 'P' : 3, 'Q' : 10, 'R' : 1, 'S' : 1, 'T' : 1, 'U' : 1, 'V' : 4, 'W' : 4, 'X' : 8, 'Y' : 4, 'Z' : 10}
        
        self.__words_created__ = []
        
        self.__first_word__ = True
        
        self.__mode__ = mode
        
    #function for up
    def __moveUp__(self, index):
        if index[0] - 1 > -1:
            return [index[0] - 1, index[1]]
        else:
            return None
    
    #function for down
    def __moveDown__(self, index):
        if index[0] + 1 < 15:
            return [index[0] + 1, index[1]]
        else:
            return None
    
    #function for left
    def __moveLeft__(self, index):
        if index[1] - 1 > -1:
            return [index[0], index[1] - 1]
        else:
            return None
    
    #function for right
    def __moveRight__(self, index):
        if index[1] + 1 < 15:
            return [index[0], index[1] + 1]
        else:
            return None
    
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
            if self.__mode__ == 2:
                score_ind = deepcopy(ind)
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
                    self.__words_created__.append(''.join(word))
                    #calculating score and return
                    if self.__mode__ == 1:
                        score = self.__caculate_score__(word)
                    elif self.__mode__ == 2:
                        score = self.__calculateScoreWithBonus__(word, score_ind, 'R')
                    return [score, word]
                
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
                    self.__words_created__.append(''.join(word))
                    #calculating score and return
                    if self.__mode__ == 1:
                        score = self.__caculate_score__(word)
                    elif self.__mode__ == 2:
                        score = self.__calculateScoreWithBonus__(word, score_ind, 'D')
                    return [score, word]
            #if-31 end
        else:
            error_code = None
            #first word is created / game has started
            if leng < 8:
                if direction == 'R':
                    if self.__mode__ == 2:
                        score_ind = deepcopy(ind)
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
                                error_code = -2
                                break
                        if error_code != -2:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            self.__words_created__.append(''.join(word))
                            #calculating score and return
                            if self.__mode__ == 1:
                                score = self.__caculate_score__(word)
                            elif self.__mode__ == 2:
                                score = self.__calculateScoreWithBonus__(word, score_ind, 'R')
                            return [score, consumed]
                        else:
                            print('Word Cannot placed Here 1')
                            return -2
                    else:
                        print('Word Cannot placed Here 2')
                        return -2
                
                elif direction == 'D':
                    if self.__mode__ == 2:
                        score_ind = deepcopy(ind)
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
                                error_code = -2
                                break
                        if error_code != -2:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            self.__words_created__.append(''.join(word))
                            #calculating score and return
                            if self.__mode__ == 1:
                                score = self.__caculate_score__(word)
                            elif self.__mode__ == 2:
                                score = self.__calculateScoreWithBonus__(word, score_ind, 'D')
                            return [score, consumed]
                        else:
                            print('Word cannot placed here 1')
                            return -2
                    else:
                        print('Word Cannot placed here 2')
                        return -2
                
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
                            if self.__mode__ == 2:
                                score_ind = deepcopy(secind)
                        else:
                            secind[1] = 14
                        for i in range(leng):
                            if secind[1] + 1 < 15 and board[secind[0]][secind[1]] == 0 or board[secind[0]][secind[1]] == word[i]:
                                if board[secind[0]][secind[1]] == 0:
                                    consumed.append(word[i])
                                board[secind[0]][secind[1]] = word[i]
                                secind[1] = secind[1] + 1
                            else:
                                error_code = -2
                                break
                        if error_code != -2:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            self.__words_created__.append(''.join(word))
                            #calculating score and return
                            if self.__mode__ == 1:
                                score = self.__caculate_score__(word)
                            elif self.__mode__ == 2:
                                score = self.__calculateScoreWithBonus__(word, score_ind, 'L')
                            return [score, consumed]
                        else:
                            print('Word Cannot placed Here 1')
                            return -2
                    else:
                        print('Word Cannot placed Here 2')
                        return -2
                
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
                            if self.__mode__ == 2:
                                score_ind = deepcopy(secind)
                        else:
                            secind[0] = 14
                        for i in range(leng):
                            if secind[0] + 1 < 15 and board[secind[0]][secind[1]] == 0 or board[secind[0]][secind[1]] == word[i]:
                                if board[secind[0]][secind[1]] == 0:
                                    consumed.append(word[i])
                                board[secind[0]][secind[1]] = word[i]
                                secind[0] = secind[0] + 1
                            else:
                                error_code = -2
                                break
                        if error_code != -2:
                            self.__game_board__ = deepcopy(board)
                            board = None
                            self.__words_created__.append(''.join(word))
                            #calculating score and return
                            if self.__mode__ == 1:
                                score = self.__caculate_score__(word)
                            elif self.__mode__ == 2:
                                score = self.__calculateScoreWithBonus__(word, score_ind, 'U')
                            return [score, consumed]
                        else:
                            print('Word Cannot placed Here 1')
                            return -2
                    else:
                        print('Word Cannot placed Here 2')
                        return -2
    
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
    
    def getCreatedWords(self):
        return self.__words_created__
    
    def __plantBonusTiles__(self, ind):
        tws = [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]
        tls = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
        dws = [(1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4), (4, 10), (10, 4), (10, 10), (11, 3), (11, 11), (12, 2), (12, 12), (13, 1), (13, 13)]
        dls = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 3), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8,2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]
        
        ind = tuple(ind)
        if ind in tws:
            return 'TWS'
        elif ind in tls:
            return 'TLS'
        elif ind in dws:
            return 'DWS'
        elif ind in dls:
            return 'DLS'
        else:
            return None
    
    def __calculateScoreWithBonus__(self, word, ind, direction):
        word = [w for w in word]
        wordl = len(word)
        cur = ind
        if direction == 'R':
            total = 0
            for x in range(wordl):
                tws_count, dws_count = 0, 0
                score = self.__tile_scores__.get(word[x])
                tile = self.__plantBonusTiles__(cur)
                if tile == 'TWS':
                    tws_count = tws_count + 1
                elif tile == 'TLS':
                    total = total + (score * 3)
                elif tile == 'DWS':
                    dws_count = dws_count + 1
                elif tile == 'DLS':
                    total = total + (score * 2)
                else:
                    total = total + score
                cur = self.__moveRight__(cur)
                if cur is None:
                    break
            if tws_count == 0 and dws_count > 0:
                return total * (2 * dws_count)
            elif dws_count == 0 and tws_count > 0:
                return total * (3 * tws_count)
            elif tws_count == 0 and dws_count == 0:
                return total
            else:
                return total * (3 * tws_count) * (2 * dws_count)
        
        if direction == 'L':
            total = 0
            for x in range(wordl):
                tws_count, dws_count = 0, 0
                score = self.__tile_scores__.get(word[x])
                tile = self.__plantBonusTiles__(cur)
                if tile == 'TWS':
                    tws_count = tws_count + 1
                elif tile == 'TLS':
                    total = total + (score * 3)
                elif tile == 'DWS':
                    dws_count = dws_count + 1
                elif tile == 'DLS':
                    total = total + (score * 2)
                else:
                    total = total + score
                cur = self.__moveLeft__(cur)
                if cur is None:
                    break
            if tws_count == 0 and dws_count > 0:
                return total * (2 * dws_count)
            elif dws_count == 0 and tws_count > 0:
                return total * (3 * tws_count)
            elif tws_count == 0 and dws_count == 0:
                return total
            else:
                return total * (3 * tws_count) * (2 * dws_count)
                
        if direction == 'U':
            total = 0
            for x in range(wordl):
                tws_count, dws_count = 0, 0
                score = self.__tile_scores__.get(word[x])
                tile = self.__plantBonusTiles__(cur)
                if tile == 'TWS':
                    tws_count = tws_count + 1
                elif tile == 'TLS':
                    total = total + (score * 3)
                elif tile == 'DWS':
                    dws_count = dws_count + 1
                elif tile == 'DLS':
                    total = total + (score * 2)
                else:
                    total = total + score
                cur = self.__moveUp__(cur)
                if cur is None:
                    break
            if tws_count == 0 and dws_count > 0:
                return total * (2 * dws_count)
            elif dws_count == 0 and tws_count > 0:
                return total * (3 * tws_count)
            elif tws_count == 0 and dws_count == 0:
                return total
            else:
                return total * (3 * tws_count) * (2 * dws_count)
                
        if direction == 'D':
            total = 0
            for x in range(wordl):
                tws_count, dws_count = 0, 0
                score = self.__tile_scores__.get(word[x])
                tile = self.__plantBonusTiles__(cur)
                if tile == 'TWS':
                    tws_count = tws_count + 1
                elif tile == 'TLS':
                    total = total + (score * 3)
                elif tile == 'DWS':
                    dws_count = dws_count + 1
                elif tile == 'DLS':
                    total = total + (score * 2)
                else:
                    total = total + score
                cur = self.__moveDown__(cur)
                if cur is None:
                    break
            if tws_count == 0 and dws_count > 0:
                return total * (2 * dws_count)
            elif dws_count == 0 and tws_count > 0:
                return total * (3 * tws_count)
            elif tws_count == 0 and dws_count == 0:
                return total
            else:
                return total * (3 * tws_count) * (2 * dws_count)
    
def caculateScore(word):
        #score calculation is without bonus
        score = 0
        game = gameBoard()
        for letter in word:
            letter_score = game.__tile_scores__.get(letter)
            score = score + letter_score
        return score
    
def calculateScoreWithBonus(word, index, direction):
    game = gameBoard()
    score = game.__calculateScoreWithBonus__(word, index, direction)
    return score
    
