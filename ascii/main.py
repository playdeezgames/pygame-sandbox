import pygame
import eventpump
import screenbuffer
import updater

pygame.init()
screen = pygame.display.set_mode((screenbuffer.SCREEN_WIDTH, screenbuffer.SCREEN_HEIGHT))
img = pygame.image.load("coco.png").convert()
clock = pygame.time.Clock()
running = True

while running:
    running = eventpump.pump_events()

    updater.update()

    screen.fill((0, 0, 0))
    for index in range(screenbuffer.CELL_COUNT):
        screen.blit(img, screenbuffer.DESTINATIONS[index], screenbuffer.AREAS[screenbuffer.screen_buffer[index]])
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
