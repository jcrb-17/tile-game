"""
initial board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

final board example, there can be others = [
    [1,2,9],
    [6,5,4],
    [7,8,3]
]

9 is the black tile

it performs the movements to get to the initial board

"""
from src.shared import *
import copy
from collections import deque 

class Node:
    def __init__(self,board,parent=None):
        self.parent = parent
        self.children = []
        self.board = board

#needs more testing
def move(board,i,j):
    movements_boards = []
    
    #move to the left
    if j-1>=0:
        #swap with the left
        boardAux = copy.deepcopy(board)
        boardAux[i][j] = boardAux[i][j-1]
        boardAux[i][j-1] = 9
        movements_boards.append(boardAux)
    #move down
    if i+1<=2:
        #swap with down
        boardAux = copy.deepcopy(board)
        boardAux[i][j] = boardAux[i+1][j]
        boardAux[i+1][j] = 9
        movements_boards.append(boardAux)
    #move to the right
    if j+1<=2:
        #swap with the right
        boardAux = copy.deepcopy(board)
        boardAux[i][j] = boardAux[i][j+1]
        boardAux[i][j+1] = 9
        movements_boards.append(boardAux)
    #move up
    if i-1>=0:
        #swap with up
        boardAux = copy.deepcopy(board)
        boardAux[i][j] = boardAux[i-1][j]
        boardAux[i-1][j] = 9
        movements_boards.append(boardAux)
    return movements_boards

def returnRoute(node):
    route = []
    while node.parent != None:
        route.append(node.board)
        node = node.parent
    route.append(node.board)
    return route[::-1]

def printRoute(route):
    for i in route:
        for j in i:
            print(j)
        print("---------")

def startSearch(board):
    
    #this is the end result, that the search will find
    boardToSearch = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    #the max number of moves is 4, if the black tile is in the center
        
    rootNode = Node(board)
    queue = deque([rootNode])
    visited = {}
    times = 0

    while True:
        #times += 1

        """
        if times >= 1000000:
            print("time out, solution not found")
            return False
        """
        try:
            node = queue.popleft()
        except:
            print("time out, solution not found")
            return False
        visited[str(node.board)] = 0
        if str(node.board) == str(boardToSearch):
            #print("Found",node.board)
            print("solution found")
            route = returnRoute(node)
            #printRoute(route)
            return route
            break
        #9 is the black tile, find the position
        
        _,i,j = findInBoard(node.board,9)
        movements_boards = move(node.board,i,j)
        for i in movements_boards:
            
            if str(i) not in visited:
                queue.append(Node(i,parent=node))

    #print(movements_boards)

if __name__=="__main__":
    #this is the board that the user enters, the search result is on startSearch
    board = [
        [1,2,3],
        [4,8,5],
        [6,7,9]
    ]

    board = [
        [2, 3, 6],
        [5, 9, 8],
        [1, 4, 7]
    ]

    #it can return False, or an array containing routes[]
    startSearch(board)

