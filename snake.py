# Snake python tutorial using OOPS

# Snake game using python
# importing libraries
import pygame

# import math
import random
import tkinter as tk
from tkinter import messagebox


# Creating cube class
class cube(object):
    rows = 20  # Number of rows
    w = 500  # Width of the window

    # Constructor
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start  # Position of the cube
        self.dirnx = 1  # Direction of the cube
        self.dirny = 0  # Direction of the cube
        self.color = color  # Color of the cube

    # Move function
    def move(self, dirnx, dirny):
        self.dirnx = dirnx  # Direction of the cube
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    # Draw function
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Distance between the rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(
            surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2)
        )  # Draw the rectangle

        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


# Creating snake class
class snake(object):
    body = []  # Body of the snake
    turns = {}  # Turns of the snake

    # Constructor
    def __init__(self, color, pos):
        self.color = color  # Color of the snake
        self.head = cube(pos)
        self.body.append(self.head)  # Add the head to the body
        self.dirnx = 0  # Direction of the snake
        self.dirny = 2  # Direction of the snake

    # Move function
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()  # Get the keys

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):  # Index and cube
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    # Reset function
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    # Add cube function
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        # Checking the direction of the snake
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    # Draw function
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


# Creating drawGrid function
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Size between the rows

    x = 0  # Top left x
    y = 0  # Top left y
    for l in range(rows):
        x = x + sizeBtwn  # Increment x
        y = y + sizeBtwn  # Increment y

        # Draw the lines
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


# Creating redrawWindow function
def redrawWindow(surface):
    global rows, w, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(w, rows, surface)
    pygame.display.update()  # Update the display


# Creating randomSnack function
def randomSnack(rows, item):
    # global rows
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)


# Creating message_box function
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


# Creating main function
def main():
    global w, rows, win, s, snack
    w = 500
    # h = 500
    rows = 20
    win = pygame.display.set_mode((w, w))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()  # Clock object

    while flag:
        pygame.time.delay(50)  # Delay
        clock.tick(30)  # 10 FPS
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1 :])):
                print("Score: ", len(s.body))
                # message_box("You lost!", "Play again...")
                message_box("You lost!", "Play again...")
                s.reset((10, 10))
                break
        redrawWindow(win)
    pass


# Setting the width, rows and cube object
rows = 20
w = 500
h = 500
cube.rows = rows
cube.w = w

# Calling the main function
main()
