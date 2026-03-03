import pygame
pygame.init()
clock = pygame.time.Clock()
minutes = 1
seconds = 1
hours = 1
milliseconds = 0
while True:
    a = pygame.time.get_ticks()
    # milliseconds is below
    #second is below
    if a == seconds*1000:
        seconds += 1
    # minutes is below 
    if a >= minutes*60000:
        minutes += 1
    # hours is below
    if a >= hours*3600000:
        hours += 1
    print(hours-1, minutes-1, seconds-1)
pygame.quit()