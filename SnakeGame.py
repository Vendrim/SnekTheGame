import random
import pygame

#objectSize defines the cell space on the field. Includes the size of snake and fruits
objectSize = 15
MAX_WIDTH , MAX_HEIGHT = 450 , 450

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getPosition(self):
        return(self.x,self.y)
    

    def __str__(self):
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

class Fruit():

    def __init__(self, boardWidth, boardHeight):
        x = random.randint(0, int(boardWidth / objectSize)) * objectSize
        y = random.randint(0, int(boardHeight / objectSize)) * objectSize
        if x == MAX_WIDTH:
            x -= objectSize
        if y == MAX_HEIGHT:
            y -= objectSize
        self.pos = Point(x, y)

    def __str__(self):
        return "Fruit(" + str(self.pos) + ")"

class Snake():

    def __init__(self, point):
        self.isGrowing = False
        self.score = 0
        self.positions = [point, Point(point.x-objectSize, point.y), Point(point.x-objectSize, point.y)]
        self.currentDirection = "RIGHT"
        self.directions =  {
        'RIGHT' : (objectSize,0),
        'LEFT' : (-objectSize,0),
        'UP' : (0,-objectSize),
        'DOWN' : (0,objectSize)
        }
    
    # removes the last element in position list and inserts the next position in front of the first element
    def move_snake(self):
        dirVector = self.directions.get(self.currentDirection)
        newHeadX = self.positions[0].x + dirVector[0]
        newHeadY = self.positions[0].y + dirVector[1]
        self.positions.insert(0, Point(newHeadX, newHeadY))
        if self.isGrowing:
            self.isGrowing = False
        else:
            self.positions.pop()

class Board():

    def __init__(self, height = 300, width = 300):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.height = height
        self.width = width
        self.score = 0
        self.gameSpeed = 300
        snakeSpawn = Point(3*objectSize + objectSize,3*objectSize)
        self.snake = Snake(snakeSpawn) 
        self.fruit = Fruit(width, height)
        self.fruitList = []
        self.fruitList.append(self.fruit)


    def spawn_next_fruit(self, eatenFruit):

        for i in range(len(self.fruitList)):
            if self.fruitList[i].pos.x == eatenFruit.pos.x and self.fruitList[i].pos.y == eatenFruit.pos.y:
                self.fruitList.pop(i)

        spawnFound = False
        f = 0
        while not spawnFound:
            f = Fruit(self.width, self.height)
            for x in self.snake.positions:
                if not (x.x == f.pos.x and x.y == f.pos.y):
                    spawnFound = True
        
        self.fruitList.append(f)

    # calculates the new board
    def check_board(self):
        done = False
        # check for fruit
        for x in self.fruitList:
            if self.snake.positions[0].x == x.pos.x and self.snake.positions[0].y == x.pos.y:
                self.score += 1
                if(self.score % 3 == 0):
                    self.gameSpeed = int(self.gameSpeed * 0.9)
                    print("New GameSpeed:" , self.gameSpeed)
                    self.snake.positions.append(self.snake.positions[-1])
                    self.snake.isGrowing = True
                self.spawn_next_fruit(x)
                done = True

        # check for body
        for x in self.snake.positions[1:]:
            if self.snake.positions[0].x == x.x and self.snake.positions[0].y == x.y:
                print("Ate my own Butt - Outch.")
                done = True
                self.stop_game(self.score)
                return False

        # check for wall
        if self.snake.positions[0].x < 0 or self.snake.positions[0].x == MAX_WIDTH or self.snake.positions[0].y < 0 or self.snake.positions[0].y == MAX_HEIGHT:
            print("Walls hurt.")
            self.stop_game(self.score)
            return False

        return True

    # creates a window with pygame
    def paint_board_pygame(self, win):
        win.fill((0,0,0))

        for x in self.fruitList:
            pygame.draw.rect(win, (214, 140, 19), (x.pos.x, x.pos.y, objectSize, objectSize))

        for x in self.snake.positions:
            pygame.draw.rect(win, (72, 173, 205), (x.x, x.y, objectSize, objectSize))

        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render('Score: ' + str(self.score), 1 , (255,0,240))
        win.blit(text, (MAX_WIDTH-130, 10))

        pygame.display.update()

    # prints the game in the console
    def paint_board_console(self):
        board_list = []
        for j in range(self.height):
            row = ""
            for i in range(self.width):
                if(j == 0 or i == 0 or j == self.height-1 or i == self.width-1):
                    row += "#"
                    continue

                isFruit = False
                for x in self.fruitList:
                    if(x.pos.x == i and x.pos.y == j):
                        row += "+"
                        isFruit = True
                        break
                if(isFruit):
                    continue
                
                isSnake = False
                for x in self.snake.positions:
                    if(x.x == i and x.y == j):
                        row += "X"
                        isSnake = True
                        break
                if(isSnake):
                    continue
                row += " "
                
            print(row)

    def stop_game(self, score):
        win.fill((0,0,0))

        for x in self.fruitList:
            pygame.draw.rect(win, (214, 140, 19), (x.pos.x, x.pos.y, objectSize, objectSize))

        for x in self.snake.positions:
            pygame.draw.rect(win, (72, 173, 205), (x.x, x.y, objectSize, objectSize))

        font = pygame.font.SysFont('comicsans', 65, True)
        font2 = pygame.font.SysFont('comicsans', 30, True)
        text = font.render('Score: ' + str(self.score), 1 , (255,0,240))
        text2 = font2.render('Press "Escape" to Exit', 1 , (255,0,240))
        text3 = font2.render('Press "Space" to play again', 1 , (255,0,240))
        win.blit(text, (90, 140))
        win.blit(text2, (90, 220))
        win.blit(text3, (90, 260))

        pygame.display.update()
        print("GAME OVER. You reached " , score , " Points.")

    def showHighscore():
        
    
    def start_game(self):
        return 0

def game_loop():
    global run
    run = True
    while run:       
        pygame.time.delay(board.gameSpeed)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False            

        if keys[pygame.K_LEFT]:
            if board.snake.currentDirection is not "RIGHT":
                board.snake.currentDirection = "LEFT"
        if keys[pygame.K_RIGHT]:
            if board.snake.currentDirection is not "LEFT":
                board.snake.currentDirection = "RIGHT"
        if keys[pygame.K_UP]:
            if board.snake.currentDirection is not "DOWN":
                board.snake.currentDirection = "UP"
        if keys[pygame.K_DOWN]:
            if board.snake.currentDirection is not "UP":
                board.snake.currentDirection = "DOWN"
        if keys[pygame.K_ESCAPE]:
            run = False

        board.paint_board_pygame(win)   #paint
        board.snake.move_snake()        #move
        run = board.check_board()   #calculate moves


if __name__ == "__main__":
    board = Board(MAX_WIDTH, MAX_HEIGHT)
    win = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    continue_game = True

    # Continue Game loop
    while continue_game:
        # Main game loop
        game_loop()
             
        # Menu Loop
        runMenu = True
        while runMenu:
            keys = pygame.key.get_pressed()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False     

            if keys[pygame.K_ESCAPE]:
                runMenu = False
                continue_game = False
            if keys[pygame.K_SPACE]:
                runMenu = False
                board.paint_board_console()

    pygame.quit()











