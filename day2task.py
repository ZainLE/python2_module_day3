
import pygame
import math

# Setting up 

pygame.init()
width, height = 1700, 1000
screen = pygame.display.set_mode((1700, 1000))
clock = pygame.time.Clock()
running = True

black = (0, 0, 0)
blue = (0, 0, 255)
white= (255,255,255)

center = (width // 2, height // 2)
radius = 5
angle = 0
radius_rate = 3
radius_limit = 200
angle_rate = 0.15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    angle += angle_rate

    radius += radius_rate
    circle_x = center[0] + int(radius * math.cos(angle))
    circle_y = center[1] + int(radius * math.sin(angle))

    pygame.draw.circle(screen, blue, (circle_x, circle_y), 15)

    pygame.draw.line(screen, black, center, (circle_x, circle_y), 3)

    pygame.display.flip()
    
    if radius>radius_limit or radius < 2:
         radius_rate *= -1
         angle_rate *= -1
         

    clock.tick(60)


pygame.quit()