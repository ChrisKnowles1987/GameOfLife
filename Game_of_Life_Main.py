import pygame as p
import random


BOARD_SIZE = WIDTH, HEIGHT = 1600, 900
CELL = 50
W, H = WIDTH // CELL, HEIGHT // CELL



def main():
    oldWorld = [[random.randint(0, 1) for row in range(W)] for col in range (H)]
    print (oldWorld)
    p.init()
    display = p.display.set_mode((BOARD_SIZE))
    p.display.set_caption('ReflectOS')
    display.fill(p.Color("black"))
    [p.draw.line(display, p.Color("gray"), (x, 0),(x, HEIGHT)) for x in range (0, WIDTH, CELL)]
    [p.draw.line(display, p.Color("gray"), (0, y),(WIDTH, y)) for y in range (0, HEIGHT, CELL)]


    while True:

        for event in p.event.get():
            if event.type == p.QUIT:
                exit()
            #print(event)

            
        
        gg = checkCells(oldWorld)
        
        #checkCells(oldWorld, x, y)
        for x in range(len(oldWorld)):
            for y in range(len(oldWorld[x])):
                if oldWorld[x][y] == 1:
                    #print (oldWorld[x][y])
                    p.draw.rect(display, p.Color("white"), (y * CELL, x * CELL, CELL, CELL) )
                    #oldWorld = checkCells(oldWorld, x ,y)    
        p.display.update()
def checkCells(oldWorld):
    neighbours= [[0, -1],[0, 1],[1, 0],[-1, 0],[1, 1],[-1, -1],[1, -1],[-1, 1]]
    
    for i in range(8):
        print(oldWorld[0+neighbours[i[0]]][0+neighbours[i[1]]])
        
                    
    
   
    
    
            
            
    
    
    pass

if __name__ == "__main__":
    main()