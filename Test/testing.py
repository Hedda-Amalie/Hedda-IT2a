import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fps = 5

#farger
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255, 0, 0)

CELL_SIZE = 60
CELL_NUMBER = 15
WIDTH = CELL_SIZE * CELL_NUMBER
HEIGHT = CELL_SIZE * CELL_NUMBER

screen = pygame.display.set_mode((WIDTH, HEIGHT))
slange = [7 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE]
dir = "right"
eple = [random.randint(0,14) * CELL_SIZE, random.randint(0,14) * CELL_SIZE, CELL_SIZE, CELL_SIZE]

def draw_snake():
    pygame.draw.rect(screen, (GREEN), slange)
    if dir == "right":
        slange[0] += 1 * CELL_SIZE
    elif dir == "left":
        slange[0] -= 1 * CELL_SIZE
    elif dir == "up":
        slange[1] -= 1 * CELL_SIZE
    elif dir == "down":
        slange[1] += 1 * CELL_SIZE

def draw_cells():
    for x in range(CELL_NUMBER):
        pygame.draw.line(screen, (0,0,0), (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT))
        pygame.draw.line(screen, (0,0,0), (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE))

def draw_apple():
    pygame.draw.rect(screen, (RED), eple)

def collide():
    if slange[0] == eple[0] and slange[1] == eple[1]:
        eple[0] = random.randint(0,14) * CELL_SIZE
        eple[1] = random.randint(0,14) * CELL_SIZE

def update():
    screen.fill(WHITE)
    draw_cells()
    draw_snake()
    draw_apple()
    collide()
    pygame.display.update()



main = True

while main == True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main = False
            if event.key == pygame.K_LEFT:
                dir = "left"
            elif event.key == pygame.K_RIGHT:
                dir = "right"
            elif event.key == pygame.K_UP:
                dir = "up"
            elif event.key == pygame.K_DOWN:
                dir = "down"
    update()
