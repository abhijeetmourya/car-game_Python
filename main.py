import pygame
import random

# window
WIDTH = 400
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DODGE THE POLICE!')

#rgb
BLACK = (0, 0, 0)
GREY = (128, 128, 128)



#Image load
raw_sian = pygame.image.load('sian.png')
raw_police = pygame.image.load('police.png')
raw_bg = pygame.image.load('images.jpg')
raw_lose = pygame.image.load('lose.png')
raw_replay = pygame.image.load('1420678-200.png')
sian = pygame.transform.scale(raw_sian, (200, 200))
police = pygame.transform.scale(raw_police, (200, 200))
bg = pygame.transform.scale(raw_bg, (400, 600))
lose = pygame.transform.scale(raw_lose, (300, 300))
replay = pygame.transform.scale(raw_replay, (100, 100))

#coordinates
sian_x = 200
sian_y = 550
police_xoptions = [100, 300]
police_x = random.choice(police_xoptions)
police_y = -70
policey_change = 10
polce_collition = police_y + 200

#displays message
def display_messsage():
    pygame.time.delay(2000)
    WIN.fill(GREY)
    WIN.blit(lose, (50, 150))
    pygame.display.update()
    pygame.time.delay(5000)
    run = False


#DRAW OBJECT
def draw():

    WIN.blit(bg, (0, 0))
    WIN.blit(sian, (sian_x - sian.get_width()/2, sian_y - sian.get_height()/2))
    WIN.blit(police, (police_x - police.get_width() / 2, police_y))
    pygame.display.update()

#Game loop
def main():
    # Clock
    FPS = 60
    run = True
    clock = pygame.time.Clock()

    global police_x, police_y, sian_x, policey_change

    while run:
        clock.tick(FPS)

        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                sian_x = 100

            if keys[pygame.K_RIGHT]:
                sian_x = 300

        police_y += policey_change
        if police_y == 600:
            police_y = -70
            police_x = random.choice(police_xoptions)
            lives = 3
            lost = False
        if sian_y == police_y + 200 and sian_x == police_x:
            lost = True
            break
    if lost:
        display_messsage()

main()
pygame.quit()
