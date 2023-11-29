
import pygame
import math

# Setting up 

pygame.init()
width, height = 1700, 1000
screen = pygame.display.set_mode((1700, 1000))
clock = pygame.time.Clock()
running = True

# black = (0, 0, 0)
# blue = (0, 0, 255)
# white= (255,255,255)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
center = (width // 2, height // 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.draw.circle(screen, "red", player_pos, 40)
screen.fill("white")
