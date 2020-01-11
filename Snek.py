import numpy as np 
import time


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getPosition(self):
        return(self.x,self.y)
    
    def updatePosition(self, vector):
        self.x += vector.x 
        self.y += vector.y 






class Snake():

    def __init__(self, point):
        self.score = 0
        self.positions = [point]
        self.currentDirection = ""
        self.direction =  {
        'RIGHT' : (1,0),
        'LEFT' : (-1,0),
        'UP' : (0,-1),
        'DOWN' : (0,1)
        }
    
   def move_snake(self, position):
        lastPosition = self.positions.pop(-1)
        self.positions.insert(0, position)
    


class Board:

    def __init__(self), height = 30, width = 50:
        self.height = height
        self.width = width
        self.snake 
        self.fruit


    def paint_board(breite, hoehe, slange, fruechte):
        board_list = []
        for j in range(hoehe):
            row = ""
            for i in range(breite):
                if(j == 0 or i == 0 or j == hoehe-1 or i == breite-1):
                    row+= "#"
                elif(slange.__contains__((j,i))):
                    row += "x"
                elif(fruechte.__contains__((j,i))):
                    row += "*"
                else:
                    row += "."
                
            print(row)

        nparray = np.array(board_list)
        output = ""
        for i in nparray:
            output += i

        print(output)



    

breite = 50
hoehe = 25
slange = [(2,3)]
fruechte = [(7,8)]



def update():
    while(True):
        time.sleep(1)
        paint_board(breite, hoehe, slange, fruechte)

if __name__ == "__main__":
    update()








