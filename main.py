import pygame
pygame.init()
clock= pygame.time.Clock()
b=1
pastb=0
while True:
    a = pygame.time.get_ticks()
    if a == b*60000:
        b += 1
    print(b)
pygame.quit()