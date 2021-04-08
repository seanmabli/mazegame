import pygame
import numpy as np

Display = pygame.display.set_mode([500, 500])
Screen = 'start'

PlayerX = 0
PlayerY = 0

pygame.init()

done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if(Screen == 'start'):
      Display.fill((0, 0, 0))
      pygame.draw.rect(Display, (255, 255, 255), (150, 300, 200, 60),  2)
      Display.blit(pygame.font.SysFont("Raleway", 40).render("Conplete The Maze", 1, (255, 255, 255)), (174, 317))
      Display.blit(pygame.font.SysFont("Raleway", 40).render("Start Game", 1, (255, 255, 255)), (174, 317))

    if(Screen == 'game'):
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          PlayerX -= 1
        if event.key == pygame.K_RIGHT:
          PlayerX += 1
        if event.key == pygame.K_UP:
          PlayerY -= 1
        if event.key == pygame.K_DOWN:
          PlayerY += 1

      Display.fill((0, 0, 0))

      Wall = np.ones((4, int(500 / 20), int(500 / 20)))

      for i in range(int(500 / 20)):
        for j in range(int(500 / 20)):
          if (Wall[0, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20, j * 20), (i * 20, j * 20 + 20))
          if (Wall[1, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20, j * 20 + 20), (i * 20 + 20, j * 20 + 20))
          if (Wall[2, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20 + 20, j * 20 + 20), (i * 20 + 20, j * 20))
          if (Wall[3, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20 + 20, j * 20), (i * 20, j * 20))

    pygame.display.flip()

pygame.quit()