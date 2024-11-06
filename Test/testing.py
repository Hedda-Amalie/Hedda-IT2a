import pygame

pygame.init()

#farger
WHITE = (255,255,255)
BLACK = (0,0,0)

CELL_SIZE = 60
CELL_NUMBER = 15
WIDTH = CELL_SIZE * CELL_NUMBER
HEIGHT = CELL_SIZE * CELL_NUMBER

screen = pygame.display.set_mode((WIDTH, HEIGHT))

main =True

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            main = False

    screen.fill(WHITE)
    