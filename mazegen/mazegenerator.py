#Chun Tseng (ct5na)
#Lauren Phan (lmp3cn)
#source: http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm

from random import randint

class cell:
    #each cell with 4 edges: 1 = walled, 0 = not walled
    #in the order of [top, right, down left]
    index = 0;
    walls = [1, 1, 1, 1]
    visited = False

def findNeighbor(cell_index, maze):
    #keep the indices of the neighbors
    neighbors = []
    #not upper edge: has upper neighbor
    if cell_index > 19:
        #low, if not visited
        if not maze[cell_index - 20].visited:
            neighbors.append(cell_index - 20)
    #not lower edge: has lower neighbor
    if cell_index < 180:
        #upper, if not visited
        if not maze[cell_index + 20].visited:
            neighbors.append(cell_index + 20)
    #not right edge: has right neighbor
    if cell_index % 20 != 9:
        if not maze[cell_index + 1].visited:
            neighbors.append(cell_index + 1)
    #not left edge: has left neighbor
    if cell_index % 20 != 0:
        if not maze[cell_index - 1].visited:
            neighbors.append(cell_index - 1)

    return neighbors

#given a cell_index, find a visited neighbors, randomly pick one and carve a passage
def carve(cell_index, maze):
    neighbors = []
    if (cell_index > 19):
        #low, if not visited
        if maze[cell_index - 20].visited:
            neighbors.append(cell_index + 20)
    #not lower edge: has lower neighbor
    if (cell_index < 180):
        #upper, if not visited
        if maze[cell.index + 20].visited:
            neighbors.append(cell_index + 20)
    #not right edge: has right neighbor
    if (cell_index % 20 != 9):
        if maze[cell.index + 1].visited:
            neighbors.append(cell_index + 1)
    #not left edge: has left neighbor
    if (cell_index % 20 != 0):
        if maze[cell.index - 1].visited:
            neighbors.append(cell_index - 1)

    #pick a random neighbors
    if len(neighbors) == 0:
        rand_i = 0
    else:
        rand_i = randint(0, len(neighbors)-1)
        num = neighbors[rand_i] - cell.index

    #determine which neighbor it is
    #delete the wall inbetween these cells
    #recall that cell.wall is an array that represnets wall [top, right, down, left]
    #left
        if(num == -1):
            maze[neighbors[rand_i]].walls[3]=0
        if(num == 1):
            maze[neighbors[rand_i]].walls[1]=0
        if(num == 20):
            maze[neighbors[rand_i]].walls[0]=0
        if(num == -20):
            maze[neighbors[rand_i]].walls[2]=0

    #mark the cell as visited (in the maze)
    maze[cell_index] = True

def generateMaze():
    #first create a 20 by 20 mazy represented by a list with 400 cells
    maze = [cell() for i in range(400)]
    #set the indices of the cells
    for i in range(0, 400):
        maze[i].index = i

    #a list of the indeces of neighboring unvisited neighboring cells
    unvis_n = []

    index = randint(0,400)
    #randomly pick a cell to begin with
    curCell = maze[index]
    #mark as visited
    curCell.visited = True

    #push the unvisited neighboring cell onto unvis_n
    neighbors = findNeighbor(curCell.index, maze)
    unvis_n.extend(neighbors)
    print unvis_n

    #pick a random neighbor from unvis_n
    while len(neighbors) != 0:
        #randomly pick a neighbor
        r = randint(0, len(unvis_n)-1)
        randN = unvis_n[r]

        #carve a passage to a random cell that is already part of the maze
        carve(randN, maze)
        unvis_n.extend(findNeighbor(randN, maze))

        #remove the randN from list neighbors
        unvis_n.pop(r)

    return maze

#test
genMaze = generateMaze()
'''
genMaze = generateMaze()
for i in range(0, len(genMaze)):
    print genMaze[i].walls'''
