# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:11:14 2020

@author: Armaghan Khan

Informed Searches: Greedy Algorithm
"""

from game import game
from copy import deepcopy
from time import time
from node import node

m = [[7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]]

goal = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]


def specialSorting(array):
    length = len(array)
    if length > 1:
        length = length - 1
        latestItem = array.pop()
        for x in range(length):
            if array[x].getCost() > latestItem.getCost():
                array.insert(x, latestItem)
                return array
        array.append(latestItem)
    return array

def calCost(goalMatrix, currentMatrix):
    cost = 0
    for x in range(3):
        for y in range(3):
            for a in range(3):
                for b in range(3):
                    if goalMatrix[x][y] == currentMatrix[a][b]:
                        dis = manhattanDistance([x, a], [y, b])
                        cost = cost + dis
    return cost

def manhattanDistance(xlist, ylist):
    #suppos x_list = [x1, x2] and y_list = [y1, y2]
    x = abs(xlist[1] - xlist[0])
    y = abs(ylist[1] - ylist[0])
    dis = x + y
    return round(dis)
    

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
            cost = calCost(goal, u)
            u_node = node(u, path, cost)
            if not u_node.find(childs) and not u_node.find(visited):
                childs.append(u_node)
                childs = specialSorting(childs)
                possiblities = possiblities + 1
    
        #check for right
        if g.canMoveRight():
            r = g.moveRight()
            #creating r node
            path = deepcopy(game_node.getPath())
            path.append('R')
            cost = calCost(goal, r)
            r_node = node(r, path, cost)
            if not r_node.find(childs) and not r_node.find(visited):
                childs.append(r_node)
                childs = specialSorting(childs)
                possiblities = possiblities + 1
            
        #check for down
        if g.canMoveDown():
            d = g.moveDown()
            #creating d node
            path = deepcopy(game_node.getPath())
            path.append('D')
            cost = calCost(goal, d)
            d_node = node(d, path, cost)
            if not d_node.find(childs) and not d_node.find(visited):
                childs.append(d_node)
                childs = specialSorting(childs)
                possiblities = possiblities + 1
                
        #check for left
        if g.canMoveLeft():
            l = g.moveLeft()
            #creating l node
            path = deepcopy(game_node.getPath())
            path.append('L')
            cost = calCost(goal, l)
            l_node = node(l, path, cost)
            if not l_node.find(childs) and not l_node.find(visited):
                childs.append(l_node)
                childs = specialSorting(childs)
                possiblities = possiblities + 1
                
        while childs:
            #pop first value from childs list
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
                g  = game(n.getMatrix(), 3)
                if (recursion % 1000 == 0):
                    print("#", end="")
                game_node = node(n.getMatrix(), n.getPath())
                break
        if win:
            break
print("---Greedy Algorithm---")    
print("Starting")
starting_time = time()
solving(m)
ending_time = time()
total = round(ending_time - starting_time)
print("Total time elapsed: ", total, " secs")
print("Ending")
print("Solving With Paths")
input()
