# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:49:21 2020

@author: Armaghan Khan
"""

"""
NOTE: 
    Following dependencies must be installed:
    1-numpy
    2-nltk
    
    To download numpy simply run following command in cmd
    
    pip install numpy
    
    To download nltk simply run following command in cmd
    
    pip install nltk
    
    One last step:
        open python console in cmd by typing python and press enter
        now write following command in console and press enter
        
        >>> nltk.download('words')
        
        wait for download to complete and after that you are good to go
"""

from gameBoard import gameBoard
from player2 import player
from copy import deepcopy as dpy

#players consist of their names and 7 random tiles
#when tiles are selected, tile_bag must be updated accordingly
#each user will be dealt as a list consisting of name, tiles, score
#the maximium number of users can play is 4 and they are kept together in a list.
#the user functionalit is only that he can make word

game = gameBoard(mode = 2)
player1 = player(game.getLetters(7), 'Bob')
player2 = player(game.getLetters(7), 'Alice')
player2.__turn__ = False

counter = 0
counter2 = 0

while True:
    if player1.__turn__ and not player2.__turn__:
        p = player1
    elif player2.__turn__ and not player1.__turn__:
        p = player2
    if counter == 6 or counter2 == 6:
        print('Main:Counter: ', counter)
        print('Main:Counter2: ', counter2)
        if player1.__score__ > player2.__score__:
            print('Winner: ', player1.__name__)
            print('Score:', player1.__score__)
            print('Loser: ', player2.__name__)
            print('Score:', player2.__score__)
        else:
            print('Winner: ', player2.__name__)
            print('Score:', player2.__score__)
            print('Loser: ', player1.__name__)
            print('Score:', player1.__score__)
        print('Total Words Made: ', game.getCreatedWords())
        break
    #Data Structure of word: ['Word', [[Index X, Index Y], 'Direction']]
    word = p.playTurn(game.__game_board__, game.getCreatedWords())
    forbid = dpy(word)
    print('Main:Word: ', word)
    if word == -1:
        p.__unable_counter__ = p.__unable_counter__ + 1
    else:
        #Data Structure of detail: [score, consumed letters]
        detail = game.word_placement(word[0], word[1], word[2])
        if detail != -2:
            print('Final Score: ', detail[0])
            new_words = game.getLetters(len(detail[1]))
            p.updateInfo(new_words, detail[1], detail[0])
        else:
            print('Forbid: ', forbid)
            p.forbidWord([forbid[1], forbid[2]])
            counter2 = counter2 + 1
        game.printGame()
    if player1.__turn__ and not player2.__turn__:
        player1.__turn__, player2.__turn__ = False, True
    elif player2.__turn__ and not player1.__turn__:
        player1.__turn__, player2.__turn__ = True, False
    
    if p.__unable_counter__ == 3:
        print('Updating Tray')
        counter = counter + 1
        game.updateBag(p.updateTray(game.getLetters(7)))
        p.__unable_counter__ = 0