from math import pow , sqrt 


class Node:
  def __innit__(self,grid,previous):
    self.grid = grid
    self.previous = previous

  def setGvalue(self,gvalue):
    self.gValue = gvalue;

  def setHvalue(self,hValue):
    self.hValue = hValue;
  
  def setFvalue(self,fCost):
    self.fCost = fCost;

def findElem(grid,value):
  y =0
  for sublist in grid:
    x=0
    for elem in sublist:
      if elem == value:
        return (x,y)
      x+=1
    y+=1

def checkSolution(grid,goalGrid):
  if(grid == goalGrid):
    return True
  else:
    return False

def possibleMoves(grid,move):
  (x,y) = findElem(grid,0)
  if(y > 0 and move == 'UP'):
    temp = grid[y-1][x]
    grid[y-1][x] = 0
    grid[y][x] = temp
    return 1
  else:
    return 100
  if(y < 2 and move =="DOWN"):
    temp = grid[y+1][x]
    grid[y+1][x] = 0
    grid[y][x] = temp
    return 1
  else: 
    return 100
  if(x > 0 and move == "LEFT"):
    temp = grid[y][x-1]
    grid[y][x-1] = 0
    grid[y][x] = temp  
    return 1
  else:
    return 100
  if(x < 2 and move == "RIGHT"):
    temp = grid[y][x+1]
    grid[y][x+1] = 0
    grid[y][x] = temp   
    return 1
  else:
    return 100
  




def manhattan(grid,goalGrid):
  manhattanCost = 0
  for i in range(0,9):
    (mx,my) = findElem(grid,i)
    (ux,uy) = findElem(goalGrid,i)
    temp = sqrt(pow((mx-ux),2) + pow((my-uy),2))
    manhattanCost += temp
  return manhattanCost

  

def missPlaced(grid,goalGrid):
  counter = 0
  y =0
  for sublist in grid:
    x=0
    for elem in sublist:
      if elem != goalGrid[y][x]:
        counter +=1
      x+=1
    y+=1
  return(counter)



def aStar(initialGrid,goalState):
  Node( )
  rootNode = Node(initialGrid,0)
  openSet = [rootNode]
  closedSet = []
  moves = ["UP","DOWN","LEFT","RIGHT"]
  while len(openSet) > 0:
    currentNode = min([x for x in openSet if x.Fcost < 10000])
    openSet.remove(currentNode)
    closedSet.append(currentNode)

    if(checkSolution(currentNode.grid,goalState) == True):
      return currentNode
    

    for i in moves:
      node = Node(currentNode.grid,currentNode)
      pathCost = possibleMoves(node.grid, i)
      if node in closedSet:
        continue
      # REMEBER TO ADD SOMETHING FOR WHEN THE G COST IS LESS
      if node in closedSet and node not in openSet:
        node.gCost = currentNode.gCost + 1 + pathCost
        node.hCost = missPlaced(node.grid,goalState)
        node.previous = currentNode
        if node not in openSet:
          openSet.append(node)

      #if i in closeSet







def main():
    initialGrid = [[7,1,4],[5,0,6],[8,3,2]]
    goalState = [[0,1,2],[3,4,5],[6,7,8]]
    print(initialGrid)
    print(goalState)
    #possibleMoves(initialGrid,(1,1),"UP")    
    #print(findElem(initialGrid,3))
    goalState = [[0,1,2],[3,4,5],[6,7,8]]
    #print(missPlaced(initialGrid,goalState))
    print(manhattan(initialGrid,goalState))
    aStar(initialGrid,goalState)


    
    


if __name__ == '__main__':
    main()
