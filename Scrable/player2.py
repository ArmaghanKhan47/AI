# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:27:55 2020

@author: Armaghan Khan

it is smart version of player.py
"""

from nltk.corpus import words
from copy import deepcopy as dcpy
from gameBoard import caculateScore, calculateScoreWithBonus
from random import randrange

class player:
    def __init__(self, letters, name):
        self.__score__ = 0
        self.__letter_tray__ = [w.lower() for w in letters ]
        self.__vocab__ = [w for w in words.words() if len(w) > 2 and len(w) < 8]
        self.__turn__ = True
        self.__name__ = name
        self.__unable_counter__ = 0
        self.__forbidden_word_with_details__ = []
        
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
    
    #function to find word can be made from player's letter tray
    def __findWord__(self, vocab, player):
        words = []
        for word in vocab:
            clonech = dcpy(player)
            req = 0
            for x in word:
                if x in clonech:
                    clonech.remove(x)
                    req = req + 1
                    
            if req == len(word):
                words.append(word)
        return words
    def __findLargestWord__(self, wordlist):
        words = []
        recorded_length = 0
        for x in wordlist:
            if len(x) >= recorded_length:
                recorded_length = len(x)
                words.append(x)
        return words

    def __findHighestScoreWord__(self, wordlist):
        recorded_score = 0
        words = []
        for x in wordlist:
            j = x.upper()
            if caculateScore(j) >= recorded_score:
                recorded_score = caculateScore(j)
                words.append(x)
        return words
    
    #function to find words starting and ending with specified letter list
    def __findWordWithSpecificStarting__(self, wordlist, starting):
        words = []
        for y in starting:
            for x in wordlist:
                if x[0] == y and x not in words:
                    words.append(x)
                elif x[-1] == y and x not in words:
                    words.append(x)
        return words
        
    #function to find openning
    def __perceptBoard__(self, board):
        openWords = []
        toVisitIndex = []
        visitedIndex = []
        index = [7, 7]
        visitedIndex.append(index)
        while True:
            vertical_direction, horizontal_direction = True, True
            #check that selected index contain word
            if board[index[0]][index[1]] != 0:
                #contains word
                #check vertical
                secindex1 = self.__moveDown__(index)
                secindex2 = self.__moveUp__(index)
                if (secindex1 == None or board[secindex1[0]][secindex1[1]] == 0) and (secindex2 == None or board[secindex2[0]][secindex2[1]] == 0):
                    #letter is open to make word from up/down or vertically
                    if secindex1 != None:
                        openWords.append([board[index[0]][index[1]], [index, 'D']])
                    if secindex2 != None:
                        openWords.append([board[index[0]][index[1]], [index, 'U']])
                    vertical_direction = False
                #check horizontal
                secindex1 = self.__moveLeft__(index)
                secindex2 = self.__moveRight__(index)
                if (secindex1 == None or board[secindex1[0]][secindex1[1]] == 0) and (secindex2 == None or board[secindex2[0]][secindex2[1]] == 0):
                    #letter is open to make word from left/right or horizontally
                    if secindex1 != None:
                        openWords.append([board[index[0]][index[1]], [index, 'L']])
                    if secindex2 != None:
                        openWords.append([board[index[0]][index[1]], [index, 'R']])
                    horizontal_direction = False
            else:
                #doesnot contains word
                openWords.append([0, [index, 'R']])
                openWords.append([0, [index, 'D']])
                break
            
            #direction in which to move
            if vertical_direction:
                secindex = self.__moveDown__(index)
                if secindex != None and board[secindex[0]][secindex[1]] != 0 and secindex not in visitedIndex:
                    toVisitIndex.append(secindex)
                secindex = self.__moveUp__(index)
                if secindex != None and board[secindex[0]][secindex[1]] != 0 and secindex not in visitedIndex:
                    toVisitIndex.append(secindex)
                
            if horizontal_direction:
                secindex = self.__moveRight__(index)
                if secindex != None and board[secindex[0]][secindex[1]] != 0 and secindex not in visitedIndex:
                    toVisitIndex.append(secindex)
                secindex = self.__moveLeft__(index)
                if secindex != None and board[secindex[0]][secindex[1]] != 0 and secindex not in visitedIndex:
                    toVisitIndex.append(secindex)
    
            if len(toVisitIndex) == 0:
                break
            #pop item from list        
            while toVisitIndex:
                index = toVisitIndex.pop(0)
                if index in visitedIndex:
                    continue
                else:
                    break
                
            #reset values
            vertical_direction, horizontal_direction = True, True
            visitedIndex.append(index)
            
        return openWords
    
    #function to play
    def playTurn(self, board, word_created):
        board_empty = False
        opennings_details = self.__perceptBoard__(board)
        #getting unique opennigs from openning_details
        try:
            unique_opennings = [x.lower() for x in list(dict.fromkeys(dict(opennings_details)))]
        except AttributeError:
            unique_opennings = [x for x in list(dict.fromkeys(dict(opennings_details)))]
        #finding words consisting of letters from letter_tray
        words = []
        if len(self.__letter_tray__) > 0:
            words = self.__findWord__(self.__vocab__, self.__letter_tray__)
        else:
            #letter tray is empty
            return -1
        if len(unique_opennings) == 1 and unique_opennings[0] == 0:
            #means board is empty
            words = list(set.intersection(set(self.__findHighestScoreWord__(words)), set(self.__findLargestWord__(words))))
            words = self.__findHighestScoreWord__(words)
            board_empty = True
        else:
            words = self.__findWordWithSpecificStarting__(words, unique_opennings)
            words = self.__findHighestScoreWord__(words)
        #selecting word which is not used before
        while True:
            popD = False
            if len(words) > 0:
                #words contain some words
                for x in range(len(words)):
#                    print('For loop executed: ', x)
                    selected_word = dcpy(words[x])
                    if selected_word.upper() in word_created:
                        #removing the word from list
                        words.pop(x)
                        popD = True
                        print('Word removed')
                        break
                    else:
                        words.pop(x)
                        break
                
                if popD:
                    continue
            else:
                #words doesnot contain words
                return -1
            if board_empty:
                #Here Param is different it only get these values values [0, [[7, 7], 'R']] and [0, [[7, 7], 'D']]
                param = opennings_details[randrange(0, len(opennings_details))]
                break
            else:
                #Data Structure of x: ['Start/End Letter', [[ Index X, Index Y], 'Direction']]
                seclist = [x for x in opennings_details if x[0] == selected_word[0].upper() and (x[1][1] == 'R' or x[1][1] == 'D')]
                if len(seclist) == 0:
                    seclist = [x for x in opennings_details if x[0] == selected_word[-1].upper() and (x[1][1] == 'L' or x[1][1] == 'U')]
                #Data Structure of param: [Score, [[Index X, Index Y], 'Direction']]
                param = self.__findSweetSpot__(selected_word, seclist)
                if param == -3:
                    #spot not found & find next word
                    continue
                else:
                    break
        return [selected_word, param[1][0], param[1][1]]
    
    def __findSweetSpot__(self, word, allowable_places):
        spots = []
        #calculating score against each allowable place
        for x in allowable_places:
            score = calculateScoreWithBonus(word.upper(), x[1][0], x[1][1])
            x[0] = score
            spots.append(x)
        
        #sorting in descending order
        for x in range(len(spots)):
            for y in range(len(spots)):
                if spots[x][0] > spots[y][0]:
                    spots[x], spots[y] = spots[y], spots[x]
        #selecting spot which is not forbidden and by forbidden means no word can be places here 
        for x in spots:
            if x[1] in self.__forbidden_word_with_details__:
                continue
            else:
                return x
        #spot not found
        return -3
    
    def updateInfo(self, new_words, consumed_words, score):
        new_words = [w.lower() for w in new_words]
        consumed_words = [w.lower() for w in consumed_words]
        #assumes that len of new_words and consumed_words is same
        for x in range(len(consumed_words)):
            self.__letter_tray__.remove(consumed_words[x])
        for x in range(len(new_words)):
            self.__letter_tray__.append(new_words[x])
        self.__score__ = self.__score__ + score
        
    def updateTray(self, new_words):
        new_words = [w.lower() for w in new_words]
        new_words, self.__letter_tray__ = dcpy(self.__letter_tray__), dcpy(new_words)
        return new_words
    
    def forbidWord(self, word_details):
        if word_details not in self.__forbidden_word_with_details__:
            self.__forbidden_word_with_details__.append(word_details)