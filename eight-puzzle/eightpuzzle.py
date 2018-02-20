#Lauren Phan and Chun Tseng
from random import *
from collections import deque
import copy

class puzzleBoard:
    #make list with coordinate positions - ordered triplet
    current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    children = []
    parent = []
    inv = 0
    def get_parent(self):
        return self.parent
    def set_parent(self, state):
        self.parent = state

def generate():
    board = puzzleBoard()
    #make list with coordinate positions - ordered triplet
    nums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in range(0,9):
        while True:
            rand = randint(0,8)
            if nums[rand] == 0:
                #unused random value found, update dict value and add to array
                board.current_state[i]= rand
                nums[rand] += 1
                break
    print "Randomly generated 8-puzzle (0 = blank): "
    #print randomly generated puzzle
    for x in range(0,9):
        print board.current_state[x],
        if (x+1) % 3 == 0:
            print("")
    return board

def isSolvable(puzzle_state):
    inv_count = 0
    goal =  [0, 1, 2, 3, 5, 8, 7, 6, 4]

    for i in range(0,8):
        for j in range( i+1, 9):
            if(puzzle_state[i] != 0 and puzzle_state[j] != 0):
                order = puzzle_state[i]
                cmp = puzzle_state[j]
                if (goal[order] > goal[cmp]):
                    inv_count += 1

    if(inv_count % 2 == 0):
        return True
    else:
        return False
    '''
    if test(puzzle_state) == True:
        return True

    [position = []
    #checks to see if current puzzle state can be solved
    #checks if total # of inversions are odd/even
    #sources https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    inv_count = 0
    isSolvable = False
    for i in range(0,len(puzzle_state)):
        for j in range(i+1,len(puzzle_state)):
            if puzzle_state[j][0] and puzzle_state[i][0] and puzzle_state[i][0] < puzzle_state[j][0]:
                inv_count += 1
    #print inv_count
    if inv_count % 2 == 0:
        isSolvable = True'''

# tests to see if current puzzle state matches the goal state
def test(puzzle_state):
    #match = True
    #instantiates a 2d array with goal instantiates
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    for i in range(0, 9):
        if (puzzle_state[i] != goal_state[i]):
        #returns true if goal state matches current puzzle state
            return False
    return True

def NumInv(board):
    inv_count = 0
    goal =  [0, 1, 2, 3, 5, 8, 7, 6, 4]

    for i in range(0,8):
        for j in range( i+1, 9):
            if(board.current_state[i] != 0 and board.current_state[j] != 0):
                order = board.current_state[i]
                cmp = board.current_state[j]
                if (goal[order] > goal[cmp]):
                    inv_count += 1

    return inv_count

def inv(s):
    return s.inv

def moveR(state, location):
    #switching locations of num and node to its right
    tempNum = state[location + 1]
    state[location + 1] = state[location]
    state[location] = tempNum
    return state

#function to move left
def moveL(state, location):
    #switching locations of num and node to its right
    tempNum = state[location - 1]
    state[location - 1] = state[location]
    state[location] = tempNum
    return state

#function to move down
def moveD(state, location):
    #switching locations of num and the tile below it
    tempNum = state[location + 3]
    state[location + 3] = state[location]
    state[location] = tempNum
    return state

#function to move up
def moveU(state, location):
    #switching locations of num and node to its right
    tempNum = state[location - 3]
    state[location - 3] = state[location]
    state[location] = tempNum
    return state

def findChildren(board):
    #finding blank space on board
    for i in range(0, len(board.current_state)):
        if board.current_state[i] == 0:
            loc = i

    #determine if position of blank space allows for each of the four possible children
    if loc < 6:
        lower_board = puzzleBoard()
        lower_board.current_state = copy.deepcopy(board.current_state)
        lower_board.current_state = moveD(lower_board.current_state,loc)
        lower_board.inv = NumInv(lower_board)
        board.children.append(lower_board)
        lower_board.set_parent(board)

    if loc > 2:
        #has an upper child
        upper_board = puzzleBoard()
        upper_board.current_state = copy.deepcopy(board.current_state)
        upper_board.current_state = moveU(upper_board.current_state,loc)
        upper_board.inv = NumInv(upper_board)
        board.children.append(upper_board)
        upper_board.set_parent(board)

    if (loc != 2 and loc != 5 and loc != 8):
        #has a right child
        right_board = puzzleBoard()
        right_board.current_state = copy.deepcopy(board.current_state)
        right_board.current_state = moveR(right_board.current_state, loc)
        right_board.inv = NumInv(right_board)
        board.children.append(right_board)
        right_board.set_parent(board)

    if (loc != 0 and loc != 3 and loc != 6):
        #has a left
        left_board = puzzleBoard()
        left_board.current_state = copy.deepcopy(board.current_state)
        left_board.current_state = moveL(left_board.current_state,loc)
        left_board.inv = NumInv(left_board)
        board.children.append(left_board)
        left_board.set_parent(board)

    board.children.sort(key=inv)
    return board.children
    #assigning existing children to list

def printGrid(grid):
    for x in range(0,9):
        print grid[x],
        if (x+1) % 3 == 0:
            print("")

def solve(p1,p2,p3,p4,p5,p6,p7,p8,p9):

    board =  puzzleBoard()
    grid = board.current_state
    solved = puzzleBoard()

    #initializing points in grid to param vals
    grid[0] = p1
    grid[1] = p2
    grid[2] = p3
    grid[3] = p4
    grid[4] = p5
    grid[5] = p6
    grid[6] = p7
    grid[7] = p8
    grid[8] = p9

    print("Grid to solve: ")
    printGrid(grid)
    print("")
    #quit if grid is not solvable
    if isSolvable(grid) == False:
        print "unsolvable"
        return
    if test(grid) == True:
        print "puzzle already in goal state"
        return

    stateSpace = []
    stateSpace.append(board)
    stop = False
    PtoPrint = []

    while stop == False:
        board = stateSpace[0]
        findChildren(board)
        for i in range(0, len(board.children)):
            if test(board.children[i].current_state) == True:
                solved = board.children[i]
                stop = True;
            else:
                stateSpace.append(board.children[i])

        stateSpace.pop(0)
    print "SOLVED"
    print "path to goal state:"
    print " "
    PtoPrint.append(solved)

    while(solved.get_parent() != []):
        PtoPrint.append(solved.get_parent())
        solved = solved.parent

    PtoPrint.reverse()
    for state in PtoPrint:
        printGrid(state.current_state)
        print " "



def main():

    # START commenting out here if testing custom board
    '''test_board = generate()
    print("")
    grid = test_board.current_state
    # initializing random board to parameter vals
    p1 = grid[0][0]
    p2 = grid[1][0]
    p3 = grid[2][0]
    p4 = grid[3][0]
    p5 = grid[4][0]
    p6 = grid[5][0]
    p7 = grid[6][0]
    p8 = grid[7][0]
    p9 = grid[8][0]'''
    #END commenting out here if testing custom board
    #test_board = puzzleBoard()
    #test_state = [[4,0,0],[1,0,1],[2,0,2],[7,1,0],[5,1,1],[3,1,2],[0,2,0],[8,2,1],[6,2,2]]
    #test_board.current_state = test_state
    #findChildren(test_board)
    #solving randomly-generated boards
    #solve(0, 1, 2, 4, 5, 3, 7, 8, 6)
    #solve(1, 3, 4, 8, 2, 5, 7, 6, 0)
    solve(1, 3, 0, 8, 2, 4, 7, 6, 5)
    #solve(1,2,3,6,7,4,0,8,5)
    #solve(p1,p2,p3,p4,p5,p6,p7,p8,p9)
    #solve(1,2,3,8,4,0,7,6,5)
    #goal_state = [[,0,0],[2,0,1], [3,0,2], [8,1,0], [0,1,1], [4,1,2], [7,2,0], [6,2,1], [5,2,2]]
    #print isSolvable(goal_state)
    #solve(1,3,4,5,6,0,8,2,7)
    #solve(grid[0][0], grid[1][0], grid[2][0], grid[3][0], grid[4][0], grid[5][0], grid[6][0], grid[7][0], grid[8][0])
if __name__ == "__main__":
    main()
