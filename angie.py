import heapq
import copy
import time
import numpy as np
import pandas as pd

seen = []

class eightprob():
    #madeInitialState = puts
    #initialState = [[7,1,2],[4,8,5],[6,3,0]]
    initialState = 0
    def goaltest(self, state):
        if state == [[1,2,3],[4,5,6],[7,8,0]]:
            return True
        else:
            return False

class Node:
    def __init__(self, problem, cost, depth, hVal):
        self.problem = problem
        self.cost = cost
        self.depth = depth
        self.hVal = hVal
    def __lt__(self, Hval):
        return self.hVal < Hval.hVal

def left(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (i - 1) >= 0:
                    node.problem[i][j], node.problem[i-1][j] = node.problem[i-1][j], node.problem[i][j]
                    return node
    return None

def right(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (i + 1) < len(node.problem[i]):
                    node.problem[i][j], node.problem[i+1][j] = node.problem[i+1][j], node.problem[i][j]
                    return node
    return None

def up(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (j - 1) >= 0:
                    node.problem[i][j], node.problem[i][j-1] = node.problem[i][j-1], node.problem[i][j]
                    return node
    return None

def down(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (j + 1) < len(node.problem[j]):
                    node.problem[i][j], node.problem[i][j+1] = node.problem[i][j+1], node.problem[i][j]
                    return node
    return None

def AstarWMisplaced(node: Node):

    goalState = [[1,2,3],[4,5,6],[7,8,0]]
    graphxy = [[0,0],[0,1],[0,2]]

    #initialState = [[1,2,3],[4,5,6],[0,7,8]]

    misplacedHeuristic = 0
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if node.problem[x][y] != goalState[x][y] and node.problem[x][y] != 0:
                misplacedHeuristic += 1

                # print("changedVal")
    return misplacedHeuristic

def AstarWManhattan(node: Node):


    goalState = [[1,2,3],[4,5,6],[7,8,0]]

    manhat = 0
    #print(manhat)
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if goalState[x][y] == 0:
                cor1 = x
                cor2 = y
    #print(cor1)
    #print(cor2)
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if node.problem[x][y] != goalState[x][y] and node.problem[x][y] != 0:
                manhat += (abs(cor1 - x) + abs(cor2 - y) + 1)
                #print((abs(cor1 - x) + abs(cor2 - y))
                

    #print(manhat)
    return manhat

# function general-search(problem,Queueing-Function)
def generalSearch (problem, QFunc):
    
    #nodes = MAKE-QUEUE(MAKE-NODE(problem, initial state))
    initialNode = Node(problem.initialState, 0, 0, 0)
    
    states = [] #creating the makeQueue called states 
    heapq.heappush(states, initialNode) #putting the first node inside the queue 
    nodeCount = 0 
    #loop do 
    while states:
        
        currentState = states.pop(0) 
        nodeCount += 1

        #if problem.currentstate = problem.goalstate then return node
        if problem.goaltest(currentState.problem):
            print("Solution Found!")
            print('How many nodes expanded = ', nodeCount)
            print('depth: ', currentState.depth)
            print('Max Queue size: ', len(states))
            return currentState
        #nodes = Queueing function(nodes, expand(nodes, problem.Operators))
        states = QueueFunc(currentState, states, QFunc)

    

    else:
        print("fail")
        return None 


def QueueFunc(node: Node, nodes, hx):
    

    global seen


    branchNodeUp = copy.deepcopy(node)
    branchNodeUp = up(copy.deepcopy(branchNodeUp))
    if branchNodeUp is not None:
        branchNodeUp.depth += 1
        if (hx == 1):

            branchNodeUp.cost += 1
            branchNodeUp.hVal += 1

        if (hx == 2):
            #print("A*")
            branchNodeUp.cost = AstarWMisplaced(branchNodeUp) + branchNodeUp.cost

        if (hx == 3):
            branchNodeUp.cost = AstarWManhattan(branchNodeUp) + branchNodeUp.cost

        if (branchNodeUp.problem) not in seen: 
            heapq.heappush(nodes, branchNodeUp)
            seen.append(branchNodeUp.problem)

    branchNodeDown = copy.deepcopy(node)
    branchNodeDown = down(copy.deepcopy(branchNodeDown))
    if branchNodeDown is not None:
        branchNodeDown.depth += 1
        if (hx == 1):

            branchNodeDown.cost += 1
            branchNodeDown.hVal += 1
        if (hx == 2):
            branchNodeDown.cost = AstarWMisplaced(branchNodeDown) + branchNodeDown.cost

        if (hx == 3):
            branchNodeDown.cost = AstarWManhattan(branchNodeDown) + branchNodeDown.cost
        if (branchNodeDown.problem) not in seen: 
            heapq.heappush(nodes, branchNodeDown)
            seen.append(branchNodeDown.problem)
    
         

    branchNodeLeft = copy.deepcopy(node)
    branchNodeLeft = left(copy.deepcopy(branchNodeLeft))
    if branchNodeLeft is not None:
        branchNodeLeft.depth += 1
        if (hx == 1):
            branchNodeLeft.cost += 1
            branchNodeLeft.hVal += 1
        if (hx == 2):
           branchNodeLeft.cost = AstarWMisplaced(branchNodeLeft) + branchNodeLeft.cost

        if (hx == 3):
            branchNodeLeft.cost = AstarWManhattan(branchNodeLeft) + branchNodeLeft.cost
        if (branchNodeLeft.problem) not in seen: 
            heapq.heappush(nodes, branchNodeLeft)
            seen.append(branchNodeLeft.problem)
         
        
    branchNodeRight = copy.deepcopy(node)
    branchNodeRight = right(copy.deepcopy(branchNodeRight))
    if branchNodeRight is not None:
        branchNodeRight.depth += 1
        if (hx == 1):
            branchNodeRight.cost += 1
            branchNodeRight.hVal += 1
        if (hx == 2):
            branchNodeRight.cost = AstarWMisplaced(branchNodeRight) + branchNodeRight.cost
           
        if (hx == 3):
            branchNodeRight.cost = AstarWManhattan(branchNodeRight) + branchNodeRight.cost
        if (branchNodeRight.problem) not in seen: 
            heapq.heappush(nodes, branchNodeRight)
            seen.append(branchNodeRight.problem)
    
    nodes = sorted(nodes, key=lambda n: (n.cost, n.depth))
    return nodes


def main():
    prob = eightprob()
    puts = []
    print("Samarth's Angelika puzzle solver!")
    print("This Puzzle is dedicated to Angie, one of the best and kindest people I know.")
    choice = input("Press 1 if you want to input a puzzle, Press 2 for to check set depth puzzles from 0 - 24 depth" + '\n')
    
    char_to_num = {'A': 1, 'n': 2, 'g': 3, 'e': 4, 'l': 5, 'i': 6, 'k': 7, 'X': 0, 'a': 8}  # Adjusted character to number mapping, also differentiated between A and a to make sure I could do this correctly LOLOLOLOLOL 
    
    if choice == "1":
        print("Enter your puzzle, using 'X' to represent the blank and 'A' for the first position. Please only enter valid characters from 'AngelikaX'." + '\n')
        puzzle_row_one = input("Enter the first row (with spaces in between the characters): ")
        puzzle_row_two = input("Enter the second row (with spaces in between the characters): ")
        puzzle_row_three = input("Enter the third row (with spaces in between the characters): ")
    
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        puzzle_row_one = [char_to_num[char] for char in puzzle_row_one]
        puzzle_row_two = [char_to_num[char] for char in puzzle_row_two]
        puzzle_row_three = [char_to_num[char] for char in puzzle_row_three]
        puts = [puzzle_row_one, puzzle_row_two, puzzle_row_three]


        print(puts)
        prob.initialState = puts

        choice2 = input("If you want to run Uniform Cost search, press 1, if you want to run Misplaced Tile Heuristic search, press 2, and if you want to run the Manhattan Heuristic search, press 3" + '\n')

        if choice2 == "1":
            generalSearch(prob, 1)
        if choice2 == "2":
            generalSearch(prob, 2)
        if choice2 == "3":
            generalSearch(prob, 3)
    if choice == "2":
        depthNum = input("Enter a depth: 0,2,4,8,13,16,20 or 24\n")
        depthNum = int(depthNum) 
        
        depth_states = {
            0: [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
            2: [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
            4: [[1, 2, 3], [5, 0, 6], [4, 7, 8]],
            8: [[1, 3, 6], [5, 0, 2], [4, 7, 8]],
            13: [[1, 3, 6], [5, 0, 7], [4, 8, 2]],
            16: [[1, 6, 7], [5, 0, 3], [4, 8, 2]],
            20: [[7, 1, 2], [4, 8, 5], [6, 3, 0]],
            24: [[0, 7, 2], [4, 6, 1], [3, 5, 8]],
            31: [[8, 6, 7], [2, 5, 4], [3, 0, 1]]
        }

        if depthNum in depth_states:
            prob.initialState = depth_states[depthNum]
        else:
            print("Invalid depth entered. Please try again.")
            return

        heuristic_choice = input("If you want to run Uniform Cost search, press 1, if you want to run Misplaced Tile Heuristic search, press 2, and if you want to run the Manhattan Heuristic search, press 3" + '\n')
        heuristic_choice = int(heuristic_choice)
        generalSearch(prob, heuristic_choice)

main()


