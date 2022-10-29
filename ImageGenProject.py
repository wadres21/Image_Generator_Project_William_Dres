import pygame
from pygame.locals import *
#import gradient_pygame as gp
import random
import os.path

# Initializing pygame
pygame.init()

scaleX = 3000
scaleY = 1500
# Setting up the screen in 640 pixels wide, and 360 pixels high
screen = pygame.display.set_mode((scaleX, scaleY), pygame.SRCALPHA)
pygame.display.set_caption('My Image Generator')
screen = pygame.display.get_surface()
# screen.fill((233, 223, 202))

# creates a random dark color
r = random.randint(0, 20)
g = random.randint(0, 20)
b = random.randint(0, 20)
color_1 = (r, g, b)
# colors screen with random dark color
screen.fill(color_1)
'''
color_2
color_3
color_4
color
'''

# 3️⃣load images in a lists and randomly draw on the screen
BlackHole = pygame.image.load(os.path.join('data', 'BlackHole.png'))
GasGiant1 = pygame.image.load(os.path.join('data', 'GasGiant1.png'))
GasGiant2 = pygame.image.load(os.path.join('data', 'GasGiant2.png'))
LavaWorld1 = pygame.image.load(os.path.join('data', 'LavaWorld1.png'))
RockPlanet = pygame.image.load(os.path.join('data', 'RockPlanet.png'))
space_images = [BlackHole, GasGiant1, GasGiant2, LavaWorld1, RockPlanet]

Asteroid1 = pygame.image.load(os.path.join('data', 'Asteroid1.png'))
Asteroid2 = pygame.image.load(os.path.join('data', 'Asteroid2.png'))
Asteroid3 = pygame.image.load(os.path.join('data', 'Asteroid3.png'))
asteroid_images = [Asteroid1, Asteroid2, Asteroid3]


def drawSpaceImage():
    for n in range(0, 3):
        x = random.randint(1, scaleX)
        y = random.randint(1, scaleY)
        screen.blit(random.choice(space_images), (x, y))

def drawAsteroidImage():
    for n in range(0, 50):
        x = random.randint(1, scaleX)
        y = random.randint(1, scaleY)
        screen.blit(random.choice(asteroid_images), (x, y))

def color_palette():
    # chooses a random # to change r,g,b of color_1 to create a color palette
    cr = random.randint(10, 25)
    cg = random.randint(10, 25)
    cb = random.randint(10, 25)

    global color2, color3, color4, color5, color6, color7, color8

    # creates a random palette of 4 new colors
    color2 = (r + cr, g + cg, b + cb)  #10-55
    color3 = (r + (2 * cr), g + (2 * cg), b + (2 * cb))  # 20-80
    color4 = (r + (3 * cr), g + (3 * cg), b + (3 * cb))  # 30-105
    color5 = (r + (4 * cr), g + (4 * cg), b + (4 * cb))  # 40-130
    color6 = (r + (5 * cr), g + (5 * cg), b + (5 * cb))  # 50-155
    color7 = (r + (6 * cr), g + (6 * cg), b + (6 * cb))  # 60-180
    color8 = (r + (7 * cr), g + (7 * cg), b + (7 * cb))  # 70-205
    return color2, color3, color4, color5, color6, color7, color8


color_palette()


def draw_cloud():
    # creates two lists to compile random x and y values
    lx = []
    ly = []
    # draws larger spheres
    for n in range(0, 300):
        x = random.randint(1, scaleX)
        y = random.randint(1, scaleY)
        lx.append(x)
        ly.append(y)
        pygame.draw.circle(screen, color2, (x, y), random.randint(15, 25), 0)

    # draws smaller spheres in same locations as previous for loop
    for m in range(0, 200):
        pygame.draw.circle(screen, color3, (lx[m], ly[m]), random.randint(1, 10), 0)

drawAsteroidImage()
draw_cloud()


# creates a 3 by 3 pixel diamond shape w/ empty inside
def pixeldmd(x, y, Cp):
    screen.set_at((x, y), Cp)
    screen.set_at((x, y - 2), Cp)
    screen.set_at((x - 1, y - 1), Cp)
    screen.set_at((x + 1, y - 1), Cp)


# creates a 3 by 3 pixel X shape
def pixelX(x, y, Cp):
    screen.set_at((x, y), Cp)
    screen.set_at((x, y - 2), Cp)
    screen.set_at((x + 2, y), Cp)
    screen.set_at((x + 1, y - 1), Cp)
    screen.set_at((x + 2, y - 2), Cp)


def drawpixelX():
    bx = random.randint(1, scaleX)
    by = random.randint(1, scaleY)
    for p in range(0, 60):
        x = random.randint(1, scaleX)
        y = random.randint(1, scaleY)
        #creates a cloud of Xs in a random location
        pixelX((x // 20) + bx, (y // 20) + by, color4)
#random.randfloat(0,1)

def drawDiagonalLine():
    #for i in range(scaleY):
        #line(surface, color, startPosition, endPosition)
        screen = pygame.display.set_mode((scaleX, scaleY))
        color = color8
        pygame.draw.line(screen, color, (0, 0), (scaleX, scaleY), 1)
drawAsteroidImage()
#drawDiagonalLine()
'''
def border():
    global border
    border = []
    # puts the border pixel coordinates into a list
    for j in range(1, scaleX + 1):
        border.append((j, 1))
        border.append((j, scaleY))
    for j in range(2, scaleY):  # lesser to avoid corner double corners
        border.append((1, j))
        border.append((scaleY, j))
'''

# makes a list of all pixels in image
'''
def FindPoint(x1, y1, x2, y2, x, y):
    if x1 < x < x2 and y > y1 and y < y2:
        return True
    else:
        return False
'''

def drawFog():
    for n in range(0, 200):
        drawpixelX()

drawFog()

'''
def getCoords():
    x = random.randint(1, scaleX)
    y = random.randint(1, scaleY)
    return x, y
'''

def drawpixeldmd():
    for n in range(0, 5000):

        x = random.randint(1, scaleX)
        y = random.randint(1, scaleY)
        pixeldmd(x, y, color2)


drawpixeldmd()

def DmD():
    x = random.randint(1, scaleX)
    y = random.randint(1, scaleY)
    u = random.randint(2, 12)
    for n in range(0, u):
        screen.set_at((x, y - n), color8)

def Planet():
    x = random.randint(1, scaleX)
    y = random.randint(1, scaleY)
    s = random.randint(30, 200)
    pygame.draw.circle(screen, color6, (x, y), s, 0)
    pygame.draw.circle(screen, color7, (x + (s / 8) , y), s - (s / 8), 0)

Planet()

def PlanetnMoon():
    x = random.randint(1, scaleX)
    y = random.randint(1, scaleY)
    s = random.randint(20, 50)
    pygame.draw.circle(screen, color6, (x, y), s, 0)
    pygame.draw.circle(screen, color7, (x + (s / 6), y), s - (s / 6), 0)

    mx = random.randint(s, 2 * s)
    my = random.randint(s, 2 * s)
    ms = random.randint(5, s // 2)

    pygame.draw.circle(screen, color5, (x + mx, y + my), ms, 0)
    pygame.draw.circle(screen, color6, (x + mx + (ms / 4), y + my), ms - (ms / 4), 0)

PlanetnMoon()

drawSpaceImage()

# Define a function for exiting program
def exit_program():
    pygame.display.quit()
    pygame.quit()
    exit()


# Update the display
pygame.display.update()

n = 1

# infinite run
while True:
    fileName = "drawn{}.png"
    fileName = fileName.format(n)

    if not os.path.exists(fileName):
        fileName = "drawn{}.png"
        fileName = fileName.format(n)
        pygame.image.save(screen, fileName)
        print("export image:", fileName)
        pygame.display.set_caption(fileName)
        running = True
        # Keep Displaying the window until close it manually
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit_program()
    n += 1
