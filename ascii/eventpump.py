import pygame


def pump_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
