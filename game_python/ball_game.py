import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

x, y = 100, 100
dx, dy = 1, 1

clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    x += dx
    y += dy

    if x < 0 or x > 370:
        dx *= -1
    if y < 0 or y > 270:
        dy *= -1

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

    pygame.display.update()
   