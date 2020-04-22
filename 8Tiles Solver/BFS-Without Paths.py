# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:22:47 2020

@author: Armaghan Khan

Solve but  without path slightly faster
BFS
"""

from game import game
import sys, time
f = open("output.txt", "w")
sys.setrecursionlimit(7000)

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
    win = False
    #crate game object from input
    while True:
        visited.append(g.getValue())
        #check for up
        if g.canMoveUp():
            u = g.moveUp()
            if u not in childs and u not in visited:
                childs.append(u)
                possiblities = possiblities + 1
    
        #check for right
        if g.canMoveRight():
            r = g.moveRight()
            if r not in childs and r not in visited:
                childs.append(r)
                possiblities = possiblities + 1
            
        #check for down
        if g.canMoveDown():
            d = g.moveDown()
            if d not in childs and d not in visited:
                childs.append(d)
                possiblities = possiblities + 1
                
        #check for left
        if g.canMoveLeft():
            l = g.moveLeft()
            if l not in childs and l not in visited:
                childs.append(l)
                possiblities = possiblities + 1
                
        while childs:
            #pop first value from childs list
            n = childs.pop(0)
            if n == goal:
                childs.clear()
                msg = " ---INFO START--- \n Childs Lenght: {} \n Data: {} \n Possiblites: {} \n Recursion Depth: {} \n Visited Length: {} \n ---INFO END---\n".format(len(childs), n, possiblities, recursion, len(visited))
                print(msg)
                print("won")
                win = True
                break
            elif n not in visited:
                recursion = recursion + 1
                print(recursion)
                g  = game(n, 3)
#                msg = " ---INFO START--- \n Childs Lenght: {} \n Data: {} \n Possiblites: {} \n Recursion Depth: {} \n Visited Length: {} \n ---INFO END---\n".format(len(childs), n, possiblities, recursion, len(visited))
#                print(msg)
#                if (recursion % 1000 == 0):
#                    print("#", end="")
                #f.write(msg)
                break
        if win:
            break
    
print("Solving Without Path and Without HashTable")
print("Starting")
starting_time = time.time()
solving(m)
ending_time = time.time()
total = round(ending_time - starting_time)
print("Total time elapsed: ", total, " secs")
print("Ending")
print("Solving Without Path and Without HashTable")
input()