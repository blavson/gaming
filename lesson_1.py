import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Simple game')

clock = pygame.time.Clock()
crashed = False

carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        gameDisplay.fill((56,78,125))
        car(x,y)
        pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()  

