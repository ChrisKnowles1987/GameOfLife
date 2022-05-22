import pygame as p
import random


BOARD_SIZE = WIDTH, HEIGHT = 900, 900
CELL = 10
W, H = WIDTH // CELL, HEIGHT // CELL
MAX_FPS = 5



def main():
    
    
   
    p.init()
    display = p.display.set_mode((BOARD_SIZE))
    p.display.update()
    clock =p.time.Clock()
    p.display.set_caption('ReflectOS')
    display.fill(p.Color("black"))
    [p.draw.line(display, p.Color("gray"), (x, 0),(x, HEIGHT)) for x in range (0, WIDTH, CELL)]
    [p.draw.line(display, p.Color("gray"), (0, y),(WIDTH, y)) for y in range (0, HEIGHT, CELL)]
    
    startWorld = [[random.randint(0, 1) for row in range(W)] for col in range(H)]
    for x in range(len(startWorld)):
            for y in range(len(startWorld[x])):
                
                if startWorld[x][y] == 1:
                    #print (oldWorld[x][y])
                    p.draw.rect(display, p.Color("white"), (y * CELL, x * CELL, CELL, CELL) )
    oldWorld = startWorld


    while True:

        for event in p.event.get():
            if event.type == p.QUIT:
                exit()
            #print(event)

            
        
        
        
        newWorld=checkCells(oldWorld)
        
        #print(newWorld)
        for x in range(len(newWorld)):
            for y in range(len(newWorld[x])):
                
                if newWorld[x][y] == 1:
                    #print (oldWorld[x][y])
                    if newWorld[x][y] == oldWorld[x][y]:
                        p.draw.rect(display, p.Color("orange"), (y * CELL, x * CELL, CELL, CELL) )
                    else:
                        p.draw.rect(display, p.Color("white"), (y * CELL, x * CELL, CELL, CELL) )
                        
                    #oldWorld = checkCells(oldWorld, x ,y)  
                if newWorld[x][y] == 0:
                    #print (oldWorld[x][y])
                    p.draw.rect(display, p.Color("black"), (y * CELL, x * CELL, CELL, CELL) )
                    #oldWorld = checkCells(oldWorld, x ,y)
        oldWorld = newWorld
        clock.tick(MAX_FPS)
        p.display.flip()          
        



        
            
def checkCells(oldWorld):
    neighbourCount = 0
    neighbours = []
    newWorld = [[0 for row in range(W)] for col in range(H)]
    for x in range(len(oldWorld)):
            for y in range(len(oldWorld[x])):
   
                neighbourCount = 0
                neighbours = getValidNeighbours(oldWorld, x ,y, neighbours)
                #print( x,y, neighbours)
                for i in neighbours:
                    if oldWorld[i[0]][i[1]] == 1:
                        neighbourCount += 1
                        #print( x, y, neighbourCount)
            
            
#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

                
                if oldWorld[x][y] ==1:
                    if neighbourCount < 2 or neighbourCount >3:
                        newWorld[x][y] = 0
                    else:
                        newWorld[x][y] = 1
                else:
                    if neighbourCount == 3:
                        newWorld[x][y] = 1
                    
                    
               
    
    return newWorld
    
                    
    
                            
    
def getValidNeighbours(oldWorld, x ,y, neighbours):
    neighbours = []
    neighbourList= [[0, -1],[0, 1],[1, 0],[-1, 0],[1, 1],[-1, -1],[1, -1],[-1, 1]]
    maxCol = len(oldWorld[0])-1
    maxRow = len(oldWorld[1])-1
    for i in neighbourList:
        
        if (0 <= x +i[0]  <= (maxCol)) and (0 <= y + i[1]  <= (maxRow)):
            neighbours.append([x+i[0], y+i[1]])
            #neighbours.append(y+i[1])
            #print(x, y, i, newWorld[x][y], neighbours)
    return neighbours                      
                    
   
   
        
    
  
        
                    
    
   
    
    
            
            
    
    
    pass

if __name__ == "__main__":
    main()