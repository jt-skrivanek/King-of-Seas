import pygame
import os

pygame.init()
pygame.key.set_repeat(1,5)
screen = pygame.display.set_mode((1000, 800))
icon = pygame.image.load(os.path.join("img", "icon.png"))
pygame.display.set_icon(icon)
pygame.display.set_caption("King of Seas")
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

red = pygame.Color(255, 0 , 0)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
background = pygame.image.load(os.path.join("img", "sea-pic.png"))
frontPic = pygame.image.load(os.path.join("img", "front-pic.png"))
shipPic = pygame.image.load(os.path.join("img", "ship-pic.png"))
shipRect = shipPic.get_rect()
targetPic = pygame.image.load(os.path.join("img", "target-pic.png"))
enemyPic = pygame.image.load(os.path.join("img", "enemy-pic.png"))
enemyRect1 = enemyPic.get_rect()
enemyRect2 = enemyPic.get_rect()
enemyRect3 = enemyPic.get_rect()
enemyRect4 = enemyPic.get_rect()
enemyRect5 = enemyPic.get_rect()
enemyRect6 = enemyPic.get_rect()
ballPic = pygame.image.load(os.path.join("img", "cannon-pic.png"))
shipX = 450
shipY = 350
ballX = 2000
ballY = 0
enemy1X = 60
enemy1Y = 60
enemy2X = 500
enemy2Y = 200
enemy3X = 800
enemy3Y = 600
enemy4X = 400
enemy4Y = 30
enemy5X = 100
enemy5Y = 600
enemy6X = 900
enemy6Y = 350
shoot = False
canShoot = True
mouseCannon = 0,0
font = pygame.font.SysFont('Seaford', 50)
running = True
intro = True
mainLoop = False

def ship(x,y):
    screen.blit(shipPic,(x,y))

def enemy(x,y):
    screen.blit(enemyPic,(x,y))

def ball(x,y):
    screen.blit(ballPic,(x,y))

while intro == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            intro = False
            mainLoop = True

    mousePos = pygame.mouse.get_pos()

    screen.blit(background,(0,0))
    screen.blit(frontPic,(330,100))
    textSurface2 = font.render("King of Seas", False, (0, 0, 0))
    screen.blit(textSurface2,(370,600))
    screen.blit(targetPic,(mousePos))
    pygame.display.flip()

while mainLoop == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            shipX += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            shipX -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            shipY += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            shipY -= 1               
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = True
        if event.type == pygame.MOUSEBUTTONDOWN and canShoot:
            canShoot = False
            mouseCannon = pygame.mouse.get_pos()
            ballX = shipX + 20
            ballY = shipY + 30
            shoot = True

    if ballY > 800 or ballY < 0:
        canShoot = True

    shipRect.x = shipX
    shipRect.y = shipY
    enemyRect1.x = enemy1X
    enemyRect1.y = enemy1Y
    enemyRect2.x = enemy2X
    enemyRect2.y = enemy2Y
    enemyRect3.x = enemy3X
    enemyRect3.y = enemy3Y
    enemyRect4.x = enemy4X
    enemyRect4.y = enemy4Y
    enemyRect5.x = enemy5X
    enemyRect5.y = enemy5Y
    enemyRect6.x = enemy6X
    enemyRect6.y = enemy6Y

    mousePos = pygame.mouse.get_pos()
    
    if running == True:
        if shipRect.colliderect(enemyRect1) or shipRect.colliderect(enemyRect2) or shipRect.colliderect(enemyRect3) or shipRect.colliderect(enemyRect4) or shipRect.colliderect(enemyRect5) or shipRect.colliderect(enemyRect6):
            exit()

        if ballY > enemy1Y and ballY < enemy1Y+50:
            if ballX < enemy1X+50 and ballX > enemy1X:
                enemy1X = 1100

        if ballY > enemy2Y and ballY < enemy2Y+50:
            if ballX < enemy2X+50 and ballX > enemy2X:
                enemy2X = 1100

        if ballY > enemy3Y and ballY < enemy3Y+50:
            if ballX < enemy3X+50 and ballX > enemy3X:
                enemy3Y = -500

        if ballY > enemy4Y and ballY < enemy4Y+50:
            if ballX < enemy4X+50 and ballX > enemy4X:
                enemy4Y = -500

        if ballY > enemy5Y and ballY < enemy5Y+50:
            if ballX < enemy5X+50 and ballX > enemy5X:
                enemy5Y = -500

        if ballY > enemy6Y and ballY < enemy6Y+50:
            if ballX < enemy6X+50 and ballX > enemy6X:
                enemy6X = 1300

        if enemy1X < 1000:
            enemy1X += .5
        else:
            enemy1X = -300

        if enemy4Y < 850:
            enemy4Y += .5
        else:
            enemy4Y = -300

        if enemy2X < 1000:
            enemy2X += .5
        else:
            enemy2X = -300

        if enemy3Y > -50:
            enemy3Y -= .5
        else:
            enemy3Y = 1200

        if enemy5Y > -50:
            enemy5Y -= .5
        else:
            enemy5Y = 1200

        if enemy6X > -50:
            enemy6X -= .5
        else:
            enemy6X = 1200

    
        screen.blit(background,(0,0))
        enemy(enemy1X,enemy1Y)
        enemy(enemy2X,enemy2Y)
        enemy(enemy3X,enemy3Y)
        enemy(enemy4X,enemy4Y)
        enemy(enemy5X,enemy5Y)
        enemy(enemy6X,enemy6Y)

        if shoot and shipY > mouseCannon[1] and ballY < shipY+50:
            ballY -= 1
            ball(ballX,ballY)

        if shoot and shipY < mouseCannon[1] and ballY > shipY:
            ballY += 1
            ball(ballX,ballY)

        ship(shipX,shipY)
        textSurface = font.render("King of Seas", False, (0, 0, 0))
        screen.blit(textSurface,(0,0))
        screen.blit(targetPic,(mousePos))
        pygame.display.flip()
    if running == False:
        textSurface = font.render("PAUSED", False, (255, 255, 255))
        screen.blit(textSurface,(400,300))
        pygame.display.flip()