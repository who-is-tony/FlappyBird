import pygame, random

pygame.init()

#gameover
gameover = 0

# bg
BACKGROUND = (0, 0, 0)
bg = pygame.image.load('background-day.png')
base = []
baseX = []
basechange = 0.2

for i in range(50):
    base.append(pygame.image.load('base.png'))
    baseX.append(i*336)

# bird
birdnum = random.randint(1, 3)
birdflap = 1
birdred = {1: pygame.image.load('redbird-upflap.png'), 2: pygame.image.load('redbird-midflap.png'), 3: pygame.image.load('redbird-downflap.png')}
birdyellow = {1: pygame.image.load('yellowbird-upflap.png'), 2: pygame.image.load('yellowbird-midflap.png'), 3: pygame.image.load('yellowbird-downflap.png')}
birdblue = {1: pygame.image.load('bluebird-upflap.png'), 2: pygame.image.load('bluebird-midflap.png'), 3: pygame.image.load('bluebird-downflap.png')}
birdangle = 0
birdac = 0 #ac = angle change
birdX = 50
birdY = 350
birdchange = 0
birdtimer = 0

#pipes
pipe = []
pipeX = []
pipeY = []
pipechange = 0.2

for i in range(50):
    y = random.randint(175, 300)
    x = 150 * i
    pipe.append(pygame.image.load('pipe-green.png'))
    pipeX.append(400 + x)
    pipeY.append(y)
    pipe.append(pygame.transform.flip(pipe[0], False, True))
    pipeX.append(400 + x)
    pipeY.append(y-425)

# Game Setup
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('favicon.png')
pygame.display.set_icon(icon)

running = True
while running:
    screen.blit(bg, (0, 0))

    # costume
    if birdnum == 1:
        bird = pygame.transform.rotate(birdred.get(birdflap), birdangle)
    if birdnum == 2:
        bird = pygame.transform.rotate(birdyellow.get(birdflap), birdangle)
    if birdnum == 3:
        bird = pygame.transform.rotate(birdblue.get(birdflap), birdangle)
    if birdtimer % 20 == 0 and gameover == 0:
        birdflap += 1
        if birdflap == 4:
            birdflap = 1

    # Get inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if gameover == 0:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                birdY-=(50)
                birdchange = 0.2
                birdangle = 45
                birdac = 0.00
                birdtimer = 1


    if birdY <= 0 or birdY >= 389:
        birdY = 389
        gameover = 1

    if birdtimer>=200:
        birdac = 0.8
        birdchange = 0.4
    else:
        birdtimer+=1

    birdY += birdchange
    if birdangle > -90:
        birdangle -= birdac
    if birdangle < -90:
        birdflap = 2



    for i in range(len(pipe)):
        if pipe[i].get_rect(x = pipeX[i], y = pipeY[i]).colliderect(bird.get_rect(x = birdX, y=birdY)):
            pipechange = 0
            birdac = 0
            basechange = 0
            gameover = 1

        pipeX[i] -= pipechange
        screen.blit(pipe[i], (pipeX[i], pipeY[i]))

    screen.blit(bird, (birdX, birdY))

    for i in range(len(base)):
        baseX[i] -= basechange
        screen.blit(base[i], (baseX[i], 412))

    pygame.display.update()