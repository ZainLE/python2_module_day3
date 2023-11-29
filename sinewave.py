
import pygame
import math


pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

amplitude = 100
frequency = 0.1
direction = 1
center = (width // 2, height // 2)
player_pos = [center[0], center[1]]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    if player_pos[0] > width or player_pos[0] < 0:
        direction *= -1
        
    player_pos[0] += direction
    player_pos[1] = center[1] + amplitude * math.sin(frequency * player_pos[0])
    
    pygame.draw.circle(screen, blue, (player_pos[0], player_pos[1]), 15)

    # pygame.draw.line(screen, red, center, (player_pos[0], player_pos[1]), 3) 
    
    

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
