import sys
import time
import random
import pygame
from pygame.locals import *

pygame.init()

# Window information
windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Simon Game')

# Clock
windowclock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
RED = ()
WHITE = (255, 255, 255)

# Images
yellow = pygame.image.load("yellow.jpg")
yellowRect = yellow.get_rect()
yellowStronger = pygame.image.load("yellowStronger.jpg")
yellowStrongerRect = yellowStronger.get_rect()

red = pygame.image.load("red.jpg")
redRect = red.get_rect()
redStronger = pygame.image.load("redStronger.jpg")
redStrongerRect = redStronger.get_rect()

green = pygame.image.load("green.jpg")
greenRect = green.get_rect()
greenStronger = pygame.image.load("greenStronger.jpg")
greenStrongerRect = greenStronger.get_rect()

blue = pygame.image.load("blue.jpg")
blueRect = blue.get_rect()
blueStronger = pygame.image.load("blueStronger.jpg")
blueStrongerRect = blueStronger.get_rect()

rectangles = [
    {'soft': blueRect, 'strong': blueStronger, 'strongRect': blueStrongerRect},
    {'soft': greenRect, 'strong': greenStronger, 'strongRect': greenStrongerRect},
    {'soft': redRect, 'strong': redStronger, 'strongRect': redStrongerRect},
    {'soft': yellowRect, 'strong': yellowStronger, 'strongRect': yellowStrongerRect}
]

while True:
        playerRect = pygame.Rect(0, 0, 5, 5)

        yellowRect.topleft = (50, 20)
        yellowStrongerRect.topleft = yellowRect.topleft 

        blueStrongerRect.topleft = (yellowRect.right + 20, yellowRect.top)
        blueRect.topleft = (yellowRect.right + 20, yellowRect.top)

        redStrongerRect.topleft = (yellowRect.left, yellowRect.bottom + 20)
        redRect.topleft = (yellowRect.left, yellowRect.bottom + 20)
        
        greenStrongerRect.topleft = (blueRect.left, blueRect.bottom + 20)
        greenRect.topleft = (blueRect.left, blueRect.bottom + 20)

        simon = []
        games_attempts = 0
        buttonPressed = False

        while True:
            window.fill(BLACK)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEMOTION:
                    # If the mouse moves, move the player where to the cursor.
                    playerRect.centerx = event.pos[0]
                    playerRect.centery = event.pos[1]
                if event.type == MOUSEBUTTONDOWN:
                    buttonPressed = True

            print(playerRect.topleft)
            window.blit(yellow, yellowRect)
            window.blit(blue, blueRect)
            window.blit(red, redRect)
            window.blit(green, greenRect)


            # if simon == []:
            #     for i in range(3):
            #         ran = random.randint(0, len(rectangles) - 1)
            #         window.blit(rectangles[ran]['strong'], rectangles[ran]['strongRect'])
            #         displayed = {'strong': rectangles[ran]['strong'], 'strongRect': rectangles[ran]['strongRect']}
            #         simon.append(rectangles[ran]['soft'])
            #         time.sleep(1)
            # else:
            #     for s in simon[::]:
            #         ran = random.randint(0, len(rectangles) - 1)
            #         window.blit(rectangles[ran]['strong'], rectangles[ran]['strongRect'])
            #         displayed = {'strong': rectangles[ran]['strong'], 'strongRect': rectangles[ran]['strongRect']}
            #         simon.append(rectangles[ran]['soft'])
            #         time.sleep(1)

            for rectangle in rectangles:
                if playerRect.colliderect(rectangle['soft']) and buttonPressed:
                    window.blit(rectangle['strong'], rectangle['strongRect'])
                    buttonPressed = False

            pygame.display.update()
            windowclock.tick(FPS)

