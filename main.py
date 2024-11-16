import pygame
from pygame.locals import *
from src.load_image import size
import copy
from src.shared import *
import src.tree as tree
import subprocess

subprocess.run(["python3","src/load_image.py"])

class Box():
    def __init__(self,img,x,y,size_tiles,ssid):
        self.img = img
        self.rect = pygame.Rect(x,y,size_tiles,size_tiles)
        self.id = ssid
    def draw(self,screen,draw_image=True):
        if self.img != None:
            screen.blit(self.img,(self.rect.x,self.rect.y))
        else:
            pygame.draw.rect(screen,(5,5,5),self.rect)

class Button:
    def __init__(self,name,textContent,x,y,w,h,fontsize=30):
        self.name = name
        self.rect = pygame.Rect(x,y,w,h)
        self.textContent = textContent
        self.font = pygame.font.Font(None,fontsize)
        self.text = self.font.render(self.textContent, 1, (200, 200, 200))

    def draw(self,screen,_x=0,_y=0):
        pygame.draw.rect(screen,(150,150,20),self.rect)
        screen.blit(self.text, (self.rect.x+_x,self.rect.y+_y))

def drawBoxes(boxes,screen):
    for i in boxes:
        i.draw(screen)

def updateBoxPosWithMouse(box):
    box.rect.x,box.rect.y = pygame.mouse.get_pos()

def detectMouseOverCollision(mouseBox,boxes):
    for i in boxes:
        if mouseBox.rect.colliderect(i.rect):
            #print("col",i.rect,i.id)
            return True,i
    return False,None

def drawTileGrid(screen):
    global size_tiles
    color = (250,250,250)
    pygame.draw.rect(screen,color,(100,100,size_tiles,size_tiles),2)
    pygame.draw.rect(screen,color,(200,100,size_tiles,size_tiles),2)
    pygame.draw.rect(screen,color,(300,100,size_tiles,size_tiles),2)

    pygame.draw.rect(screen,color,(100,200,size_tiles,size_tiles),2)
    pygame.draw.rect(screen,color,(200,200,size_tiles,size_tiles),2)
    pygame.draw.rect(screen,color,(300,200,size_tiles,size_tiles),2)

    pygame.draw.rect(screen,color,(100,300,size_tiles,size_tiles),2)
    pygame.draw.rect(screen,color,(200,300,size_tiles,size_tiles),2)
    pygame.draw.rect(screen,color,(300,300,size_tiles,size_tiles),2)

def returnBoxesArrWithoutSelected(id_selected,boxes):
    nboxes = []
    for i in boxes:
        if i.id != id_selected:
            nboxes.append(i)
    return nboxes

def detectDraggingBoxWithAnotherBoxCollision(box,nboxes):
    for i in nboxes:
        if box.rect.colliderect(i.rect):
            #print("col",i.rect,i.id)
            return True,i
    return False,None


def updateBoard(board,id1,id2):
    #change the id when dragging was sucessful
    _,i1,j1 = findInBoard(board,id1)
    _,i2,j2 = findInBoard(board,id2)

    board[i1][j1] = id2
    board[i2][j2] = id1

def printBoard():
    global board
    for i in board:
        print(i)

def detectCollisionBetweenBoxAndButton(box,button):
    if box.rect.colliderect(button.rect):
        return True
    return False

def showMessageSolution(screen,x=70,y=540):
    global solutionMsg
    font = pygame.font.Font(None,30)
    text = font.render(solutionMsg, 1, (200, 200, 200))
    screen.blit(text, (x,y))

def changeMessageSolution(screen,boolean,length=0):
    global solutionMsg
    if boolean == True:
        # solutionMsg = "Solution found, you need to make {} steps".format(length)
        solutionMsg = "Solución encontrada, necesitas hacer {} pasos".format(length)
        #text = font.render("Solution found, you need to make {} steps".format(length), 1, (200, 200, 200))
    elif boolean == False:
        solutionMsg = "Solution not found"
    #if message == None:
    #    solutionMsg = "Make a configuration then press click on the button find solution"

def givenIdReturnImage(idx):
    global s1,s2,s3,s4,s5,s6,s7,s8
    if idx == 1:
        return s1
    elif idx == 2:
        return s2
    elif idx == 3:
        return s3
    elif idx == 4:
        return s4
    elif idx == 5:
        return s5
    elif idx == 6:
        return s6
    elif idx == 7:
        return s7
    elif idx == 8:
        return s8
    elif idx == 9:
        return None

#for use in the second grid
def givenIJReturnPositionXY(i,j,x,y):
    #x = 600
    #y = 100
    z = 100
    if i == 0 and j == 0:
        return x,y
    elif i == 0 and j == 1:
        return x+z,y
    elif i == 0 and j == 2:
        return x+z+z,y

    elif i == 1 and j == 0:
        return x,y+z
    elif i == 1 and j == 1:
        return x+z,y+z
    elif i == 1 and j == 2:
        return x+z+z,y+z

    elif i == 2 and j == 0:
        return x,y+z+z
    elif i == 2 and j == 1:
        return x+z,y+z+z
    elif i == 2 and j == 2:
        return x+z+z,y+z+z

    else:
        print("error")
        pygame.quit()

def drawRouteTiles(screen,board,x=700,y=100):
    """
    board = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            img = givenIdReturnImage(board[i][j])
            _x,_y = givenIJReturnPositionXY(i,j,x,y)
            #print(_x,_y)
            if img != None:
                screen.blit(img,(_x,_y))
            else:
                #its the 9 tile
                pygame.draw.rect(screen,(0,0,0),(_x,_y,100,100))

            pygame.draw.rect(screen,(250,250,250),(_x,_y,100,100),2)
    #pygame.quit()

#textGame


size_tiles = size//3
# print(size_tiles)

pygame.init()

s1 = pygame.image.load("imgs/1.png")
s2 = pygame.image.load("imgs/2.png")
s3 = pygame.image.load("imgs/3.png")
s4 = pygame.image.load("imgs/4.png")
s5 = pygame.image.load("imgs/5.png")
s6 = pygame.image.load("imgs/6.png")
s7 = pygame.image.load("imgs/7.png")
s8 = pygame.image.load("imgs/8.png")

boxes = []
boxes.append(Box(s1,100,100,size_tiles,1))
boxes.append(Box(s2,200,100,size_tiles,2))
boxes.append(Box(s3,300,100,size_tiles,3))
boxes.append(Box(s4,100,200,size_tiles,4))
boxes.append(Box(s5,200,200,size_tiles,5))
boxes.append(Box(s6,300,200,size_tiles,6))
boxes.append(Box(s7,100,300,size_tiles,7))
boxes.append(Box(s8,200,300,size_tiles,8))
boxes.append(Box(None,300,300,size_tiles,9))#the last tile, doesnt have an image

mouseBox = Box(None,100,100,1,0)#when it says none is that it doesn have an image

display_flags = SHOWN
width, height = 1100, 600
#width, height = 600, 800

pygame.display.set_caption("3x3 Slide Game")
if pygame.display.mode_ok((width, height), display_flags ):
    screen = pygame.display.set_mode((width, height), display_flags)
run = 1
clock = pygame.time.Clock()

dragginState = False
normalState = True

firstSelected = None
firstSelectedCacheRect = None #used for snapping to previous position when user press esc

nboxes = []

secondSelected = 0

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# searchBtn = Button("search","Find solution",180,470,160,40)
searchBtn = Button("search","Encontrar solución",140,470,220,40)

leftBtn = Button("left","<-",810,470,30,40)
rightBtn = Button("right","->",850,470,30,40)

#down this variables are updated, according to user input
solutionMsg = ""
route = []
routeSelectedIndex = 0

while run:

    screen.fill((50,50,50))

    showMessageSolution(screen)

    if route != False:
        if len(route) > 0:
            #draw routes grid
            """
            route[index] = []
                        [1,2,9],
                        [6,5,4],
                        [7,8,3]
                    ]
            """
            drawRouteTiles(screen,route[routeSelectedIndex])

    searchBtn.draw(screen,17,10)
    leftBtn.draw(screen,6,9)
    rightBtn.draw(screen,6,9)

    updateBoxPosWithMouse(mouseBox)
    #print(mouseBox.rect)
    drawBoxes(boxes,screen)

    drawTileGrid(screen)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == KEYDOWN and event.key in [K_q]):
                # set run to 0 makes the game quit.
                run = 0

        #normalState
        if normalState == True and dragginState == False:



            searchBtnCollision = detectCollisionBetweenBoxAndButton(mouseBox,searchBtn)
            rightBtnCollision = detectCollisionBetweenBoxAndButton(mouseBox,rightBtn)
            leftBtnCollision = detectCollisionBetweenBoxAndButton(mouseBox,leftBtn)

            firstSelected = detectMouseOverCollision(mouseBox,boxes)#for dragging
            #normalState to dragginState
            if event.type == MOUSEBUTTONDOWN and firstSelected[0]== True:
                firstSelectedCacheRect = copy.deepcopy(firstSelected[1].rect)
                #print(event)
                dragginState = True
                normalState = False
                #print(normalState,dragginState)
                nboxes = returnBoxesArrWithoutSelected(firstSelected[1].id,boxes)
                #for i in nboxes:
                #    print(i.id)
                continue

            #generate solution
            ##if event.type == KEYDOWN and event.key in [K_e]:
            if event.type == MOUSEBUTTONDOWN and searchBtnCollision == True:
                """
                destination board = [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                ]

                user board example, there can be others = [
                    [1,2,9],
                    [6,5,4],
                    [7,8,3]
                ]

                9 is the black tile

                it performs the movements to get to the destination board

                """
                route = tree.startSearch(board)
                if route == False:
                    changeMessageSolution(screen,False)
                    #print("solution not found")
                else:
                    changeMessageSolution(screen,True,length=len(route))
                    #print(route)

            #iterate through solutions

            #move to the <-
            if event.type == MOUSEBUTTONDOWN and leftBtnCollision == True:
            #if event.type == KEYDOWN and event.key in [K_k]:
                routeSelectedIndex -= 1
                if routeSelectedIndex<0:
                    routeSelectedIndex = 0
            #move to the ->
            if event.type == MOUSEBUTTONDOWN and rightBtnCollision == True:
            #if event.type == KEYDOWN and event.key in [K_l]:
                routeSelectedIndex += 1
                if routeSelectedIndex>len(route)-1:
                    routeSelectedIndex = len(route)-1


        #dragginState
        elif dragginState == True and normalState == False:
            #print("You are in dragginState")
            #print(firstSelected[1].rect,firstSelectedCacheRect)
            updateBoxPosWithMouse(firstSelected[1])

            #dragginState to normalState, user press ESC
            if event.type == KEYDOWN and event.key in [K_ESCAPE]:
                dragginState = False
                normalState = True
                #print(normalState,dragginState)
                firstSelected[1].rect = copy.deepcopy(firstSelectedCacheRect)
                continue

            #dragginState to normalState, user change tile
            secondSelected = detectDraggingBoxWithAnotherBoxCollision(mouseBox,nboxes)
            #if secondSelected[1] != None:
            #    print(secondSelected[1].id)
            if event.type == MOUSEBUTTONDOWN and secondSelected[0] == True:
                #switch tiles
                firstSelected[1].rect = copy.deepcopy(secondSelected[1].rect)
                secondSelected[1].rect = copy.deepcopy(firstSelectedCacheRect)
                dragginState = False
                normalState = True

                updateBoard(board,firstSelected[1].id,secondSelected[1].id)
                #printBoard()
                #print("col")
                continue
    # add the game play in here later.

    pygame.display.flip()

    # limit the game t
    clock.tick(40)

pygame.quit()
