# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:22:47 2020

@author: Armaghan Khan

solve with path but slower
BFS
"""

from game import game
from copy import deepcopy
from time import time
from node import node

m = [[1, 0, 3],
    [5, 6, 7],
    [8, 4, 2]]

goal = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

def solving(game_matrix):
    childs = []
    visited = []
    possiblities = 0
    recursion = 0
    g = game(game_matrix, 3)
    #creating initial node with empty path
    game_node = node(g.getValue(), [])
    win = False
    while True:
        visited.append(game_node)
        #check for up
        if g.canMoveUp():
            u = g.moveUp()
            #creating u node
            path = deepcopy(game_node.getPath())
            path.append('U')
            u_node = node(u, path)
            if not u_node.find(childs) and not u_node.find(visited):
                childs.append(u_node)
                possiblities = possiblities + 1
    
        #check for right
        if g.canMoveRight():
            r = g.moveRight()
            #creating r node
            path = deepcopy(game_node.getPath())
            path.append('R')
            r_node = node(r, path)
            if not r_node.find(childs) and not r_node.find(visited):
                childs.append(r_node)
                possiblities = possiblities + 1
            
        #check for down
        if g.canMoveDown():
            d = g.moveDown()
            #creating d node
            path = deepcopy(game_node.getPath())
            path.append('D')
            d_node = node(d, path)
            if not d_node.find(childs) and not d_node.find(visited):
                childs.append(d_node)
                possiblities = possiblities + 1
                
        #check for left
        if g.canMoveLeft():
            l = g.moveLeft()
            #creating l node
            path = deepcopy(game_node.getPath())
            path.append('L')
            l_node = node(l, path)
            if not l_node.find(childs) and not l_node.find(visited):
                childs.append(l_node)
                possiblities = possiblities + 1
                
        while childs:
            #pop first value from childs list
            #pop(0) BFS and pop() DFS
            #BFS works Better
            n = childs.pop(0)
            if n.getMatrix() == goal:
                childs.clear()
                msg = " ---INFO START--- \n Childs Lenght: {} \n Data: {} \n Possiblites: {} \n Recursion Depth: {} \n Visited Length: {} \n Path: {} \n ---INFO END---\n".format(len(childs), n.getMatrix(), possiblities, recursion, len(visited), n.getPath())
                print(msg)
                print("won")
                win = True
                break
            elif not n.find(visited):
                recursion = recursion + 1
#                print(recursion)
                g  = game(n.getMatrix(), 3)
#                msg = " ---INFO START--- \n Childs Lenght: {} \n Data: {} \n Possiblites: {} \n Recursion Depth: {} \n Visited Length: {} \n Path: {} \n ---INFO END---\n".format(len(childs), n.getMatrix(), possiblities, recursion, len(visited), n.getPath())
#                print(msg)
                if (recursion % 1000 == 0):
                    print("#", end="")
                game_node = node(n.getMatrix(), n.getPath())
                break
        if win:
            break
print("Solving With Paths")    
print("Starting")
starting_time = time()
solving(m)
ending_time = time()
total = round(ending_time - starting_time)
print("Total time elapsed: ", total, " secs")
print("Ending")
print("Solving With Paths")
input()