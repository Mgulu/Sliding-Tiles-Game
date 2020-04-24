from math import pow, sqrt
from copy import deepcopy


class Node:
    def __init__(self, grid, previous):
        self.grid = grid
        self.previous = previous

    def setGvalue(self, gvalue):
        self.gCost = gvalue

    def setHvalue(self, hValue):
        self.hCost = hValue

    def setFvalue(self, fCost):
        self.fCost = fCost


def findElem(grid, value):
    y = 0
    for sublist in grid:
        x = 0
        for elem in sublist:
            if elem == value:
                return (x, y)
            x += 1
        y += 1


def gridInput():
    grid = [[],[],[]]
    inputted = []
    for i in range(3):
        for x in range(3):
            while(True):
                print("Number left :  " + str([i for i in range(10) if i not in inputted]))
                num= int(input("Input number %s : " % len(inputted)))
                print("Numbers left :")
                if num > -1 and num <9 and (num not in inputted):
                    inputted.append(num)
                    grid[i].append(int(num))
                    break
                else:
                    print("Invallid input")
    return grid

def printGrid(grid):
    for i in grid:
        print(str(i))


def checkSolution(grid, goalGrid):
    if (grid == goalGrid):
        return True
    else:
        return False


def possibleMoves(grid, move):
    (x, y) = findElem(grid, 0)
    if (y > 0 and move == 'UP'):
        # print("UP")
        temp = grid[y - 1][x]
        grid[y - 1][x] = 0
        grid[y][x] = temp
        return 1
    elif (y < 2 and move == "DOWN"):
        # print("DOWN")
        temp = grid[y + 1][x]
        grid[y + 1][x] = 0
        grid[y][x] = temp
        return 1
    elif (x > 0 and move == "LEFT"):
        # print("LEFT")
        temp = grid[y][x - 1]
        grid[y][x - 1] = 0
        grid[y][x] = temp
        return 1
    elif (x < 2 and move == "RIGHT"):
        # print("RIGHT")
        temp = grid[y][x + 1]
        grid[y][x + 1] = 0
        grid[y][x] = temp
        return 1


def manhattan(grid, goalGrid):
    manhattanCost = 0
    for i in range(0, 9):
        (mx, my) = findElem(grid, i)
        (ux, uy) = findElem(goalGrid, i)
        temp = sqrt(pow((mx - ux), 2) + pow((my - uy), 2))
        manhattanCost += temp
    return manhattanCost


def missPlaced(grid, goalGrid):
    counter = 0
    y = 0
    for sublist in grid:
        x = 0
        for elem in sublist:
            if elem != goalGrid[y][x]:
                counter += 1
            x += 1
        y += 1

    return (counter)


def aStar(initialGrid, goalState,hu):
    rootNode = Node(initialGrid, 0)
    rootNode.setGvalue(0)
    rootNode.setHvalue(0)
    rootNode.setFvalue(0)
    openSet = [rootNode]
    gridClosedSet = []
    loop = 0

    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    while len(openSet) > 0 :

        lowestF = 100000;
        for i in openSet:


            if i.fCost <= lowestF:
                lowestF = i.fCost
                currentNode = i


        loop += 1



        gridClosedSet.append(currentNode)


        if (currentNode.grid == goalState):
            print("This is Loop: " + str(loop))
            return currentNode


        for i in moves:
            #print(" This is currentNode :")

            temp = deepcopy(currentNode.grid)
            #printGrid(temp)
            node = Node(temp, currentNode)
            pathCost = possibleMoves(node.grid, i)
            #print(" THIS IS I :" + i)
            #print("THIS IS NODE : ")
            #printGrid(node.grid)

            if pathCost != 1:
                #print("TIS Continuing")
                continue

            # if node.grid in gridClosedSet:
            #  continue

            # tempGscore = gScore[currentNode] + 1

            # if tempGscore >= gScore[node]:
            # continue

            # REMEBER TO ADD SOMETHING FOR WHEN THE G COST IS LESS



            openFlag = False
            for i in openSet:
                if node.grid == i.grid:
                    openFlag = True
                    continue

            closedFlag = False
            for i in gridClosedSet:
                if node.grid == i.grid and i.gCost > currentNode.gCost + 1:
                    #print(" THIS IS IGCOST" + str(i.gCost) + " CUrrent " + str(currentNode.gCost) + " \n")
                    #print(" BEING CHANGED !!!! \n")
                    i.gCost = currentNode.gCost + 1
                    i.previous = currentNode
                    closedFlag = True
                    continue
                elif node.grid == i.grid and i.gCost < currentNode.gCost + 1:
                    #print(" IT HAS CONTINUED \n")
                    closedFlag = True
                    continue




            if openFlag == False and closedFlag == False:
                #print("IN IF STATE: ")
                #printGrid(node.grid)
                node.setGvalue(currentNode.gCost + 1)
                if hu == 't':
                    node.setHvalue(missPlaced(node.grid, goalState))
                else:
                    node.setHvalue(manhattan(node.grid, goalState))

                node.setFvalue(node.gCost + node.hCost)
                node.previous = currentNode
                #print(" THIS IS FCOST : " + str(node.fCost))
                openSet.append(node)

            # if i in closeSet
        openSet.remove(currentNode)



def main():
    #initialGrid = [[7,1,4],[5,0,6],[8,3,2]]
    #initialGrid = [[5, 8, 6], [1, 4, 0], [3, 7, 2]]
    #goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # print("\n "+ "Initial Grid :" + str(initialGrid))
    # print(goalState)
    # possibleMoves(initialGrid,"UP")
    # print(findElem(initialGrid,3))

    # print(missPlaced(initialGrid,goalState))
    # print(manhattan(initialGrid,goalState))

    print("Enter Initial Grid")
    grid = gridInput()
    print("Enter Goal grid")
    goalState = gridInput()



    while(True):
        hu = input("Manhattan(M) or Missplaced Tiles (T)").lower()
        if(hu =='m' or hu == "t"):
            break

    print(grid)

    node = aStar(grid, goalState,hu)
    moves = []
    while node.previous != 0:
        moves.append(node.grid)
        node = node.previous

    moves.reverse()
    for i in moves:
        printGrid(i)
        print("\n")




if __name__ == '__main__':
    main()
