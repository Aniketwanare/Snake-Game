import pygame
import time
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.update()

img_snakehead = pygame.image.load('snakehead.png')
img_apple = pygame.image.load('apple.png')
img_snakebody = pygame.image.load('snakebody.png')
clock = pygame.time.Clock()

block_size = 20
apple_size = 20
FPS = 10

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 45)
largefont = pygame.font.SysFont("comicsansms", 75)

direction = "RIGHT"

def pause():
    paused = True
    message_to_screen("PAUSED",black,-100,size="large")
    message_to_screen("Press C to continue or Q to quit",black,25)
    pygame.display.update()
    while paused :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gamedisplay.fill(white)
        
        clock.tick(5)
        
    
def score(score):
    text = smallfont.render("Score : " +str(score), True ,black)
    gamedisplay.blit(text, [0,0])
    
def randAppleGen():
    randApple_x = round(random.randrange(0,display_width-apple_size)) #/block_size)*block_size
    randApple_y = round(random.randrange(0,display_height-apple_size)) #/block_size)*block_size  
    return randApple_x ,randApple_y

    
def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_c:
                    direction = "RIGHT"
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gamedisplay.fill(white)
        message_to_screen("Welcome to /n Snake game", green, -100, "medium")
        message_to_screen("Game Rules :" ,blue ,0 ,"medium")
        message_to_screen(" Eat apples to grow the snake                  " ,black ,50 ,"small")
        message_to_screen(" Don't touch yourself as well as side of wall " ,black ,80 ,"small")
        message_to_screen(" Press C to play or Q to quit " ,green ,200 ,"small")

        pygame.display.update()
        clock.tick(15)

def snake(block_size,snakeList):
    
    if direction == "RIGHT" :
        head = pygame.transform.rotate(img_snakehead , 270)
    if direction == "LEFT" :
        head = pygame.transform.rotate(img_snakehead , 90)
    if direction == "UP" :
        head = pygame.transform.rotate(img_snakehead , 0)
    if direction == "DOWN" :
        head = pygame.transform.rotate(img_snakehead , 180)
    gamedisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
##        pygame.draw.rect(gamedisplay,green,[XnY[0],XnY[1],block_size,block_size])
        gamedisplay.blit(img_snakebody,(XnY[0],XnY[1]))
                         
def text_objects(text,color,size):
    if size == "small" :
        textSurface = smallfont.render(text ,True ,color)
    elif size == "medium" :
        textSurface = medfont.render(text ,True ,color)
    elif size == "large" :
        textSurface = largefont.render(text ,True ,color)
        
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color,y_displace = 0 , size = "small"):
    textSurf, textRect = text_objects(msg ,color ,size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gamedisplay.blit(textSurf, textRect)
    
def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randApple_x,randApple_y = randAppleGen()
    
    while not gameExit:

        if gameOver == True:
            gamedisplay.fill(white)
            message_to_screen("Game over",red,-50,size = "large")
            message_to_screen("Press C to play or again or Q to exit",black,10,size = "medium")
            pygame.display.update()
        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    gameExit=True
                    gameOver = False
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        direction = "RIGHT"
                        gameLoop()
            
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "LEFT"
                    
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "RIGHT"
                    
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "UP"
                    
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "DOWN"

                elif event.key == pygame.K_p:
                    pause()
                    
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gamedisplay.fill(white)

##        gamedisplay.fill(red, rect = [randApple_x,randApple_y,apple_size,apple_size])
        gamedisplay.blit(img_apple,(randApple_x,randApple_y))
        pygame.display.update()
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        snake(block_size, snakeList)

        if len(snakeList) > snakeLength :
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        
        snake(block_size,snakeList)

        score((snakeLength-1)*10)
        
        pygame.display.update()
        
##        if lead_x == randApple_x and lead_y == randApple_y:
##            randApple_x = round(random.randrange(0,display_width-block_size)) ##/block_size)*block_size
##            randApple_y = round(random.randrange(0,display_height-block_size)) ##/block_size)*block_size  
##            snakeLength +=1
        
##        if (lead_x >= randApple_x and lead_x <= randApple_x + apple_size - block_size) and (lead_y >= randApple_y and lead_y <= randApple_y + apple_size - block_size):
##            randApple_x = round(random.randrange(0,display_width-block_size)) #/block_size)*block_size
##            randApple_y = round(random.randrange(0,display_height-block_size)) #/block_size)*block_size  
##            snakeLength +=1
        
        if (lead_x >= randApple_x and lead_x <= randApple_x + apple_size) or (lead_x + block_size >= randApple_x and lead_x + block_size <= randApple_x + apple_size) :
            if (lead_y >= randApple_y and lead_y <= randApple_y + apple_size) :
                randApple_x,randApple_y = randAppleGen()
                snakeLength +=1
            elif (lead_y + block_size >= randApple_y and lead_y + block_size <= randApple_y + apple_size) :
                randApple_x,randApple_y = randAppleGen()
                snakeLength +=1

        
   


        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
