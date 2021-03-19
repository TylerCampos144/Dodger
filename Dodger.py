import pygame
import random

WindowWidth = 600
WindowHeight = 600
TextColor = (0, 0, 0)
BackgroundColor = (255, 255, 255)
FPS = 60
EnemySizeMin = 10
EnemySizeMax = 40
EnemySpeedMin = 1
EnemySpeedMax = 8
EnemySpawnRate = 6
PlayerMoveRate = 5


def terminate():
    pygame.quit()



def WaitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.key == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


def PlayerHitsEnemy(PlayerRect, Enemy):
    for e in Enemy:
        if PlayerRect.colliderect(b['rect']):
            return True
    return False


def DrawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TextColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Set up

pygame.init()
MainClock = pygame.time.Clock()
WindowSurface = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Fonts
font = pygame.font.SysFont(None, 48)

# show start
WindowSurface.fill(BackgroundColor)
DrawText('Dodger', font, WindowSurface, (WindowWidth / 2,), (WindowHeight / 2))
DrawText('press any key to start', font, WindowSurface, (WindowWidth / 3) - 30, (WindowHeight / 3) + 50)
pygame.display.update()
WaitForPlayerToPressKey()

TopScore = 0
while True:
    # start of game
    Enemys = []
    score = 0
    PlayerRect.topleft = (WindowWidth / 2, WindowHeight - 50)
    MoveLeft = MoveRight = MoveUp = MoveDown = False
    ReverseCheat = SlowCheat = False
    EnemyAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:
        # the game loop runs while the game is playing
        score += 1  # increases score

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.type == K_z:
                    ReverseCheat = True
                if event.type == K_x:
                    SlowCheat = True
                if event.type == K_LEFT or event.key == K_a:
                    MoveRight = False
                    MoveLeft = True
                if event.type == K_RIGHT or event.key == K_d:
                    MoveLeft = False
                    MoveRight = True
                if event.type == K_UP or event.key == K_w:
                    MoveDown = False
                    MoveUp = True
                if event.type == K_DOWN or event.key == K_s:
                    MoveUp = False
                    MoveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    ReverseCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.type == K_LEFT or event.key == K_a:
                    MoveLeft = False
                if event.type == K_RIGHT or event.key == K_d:
                    MoveRight = False
                if event.type == K_UP or event.key == K_w:
                    MoveUp = False
                if event.type == K_DOWN or event.key == K_s:
                    MoveDown = False

            if event.type == MOUSEMOTION:
                # if mouse moves, it moves the player
                PlayerRect.centerx = event.pos[0]
                PlayerRect.centery = event.pos[1]

    if not ReverseCheat and not SlowCheat:
        EnemyAddCounter += 1
    if EnemyAddCounter == EnemySpawnRate:
        EnemyAddCounter = 0
        EnemySize = random.randint(EnemySizeMin, EnemySizeMax)
        NewEnemy = {
            'rect': pygame.Rect(random.randint(0, WindowWidth - EnemySize), 0 - EnemySize, EnemySize, EnemySize),
            'speed': random.randint(EnemySpeedMin, EnemySpeedMax),
            'surface': pygame.transform.scale(EnemySize, EnemySize)
            }

        Enemy.apend(NewEnemy)

    # Moves Player
    if MoveLeft and PlayerRect.left > 0:
        PlayerRect.move_ip(-1 * PlayerMoveRate, 0)
    if MoveRight and PlayerRect.right < WindowWidth:
        PlayerRect.move_ip(PlayerMoveRate, 0)
    if MoveUp and PlayerRect.top > 0:
        PlayerRect.move_ip(0, -1 * PlayerMoveRate)
    if MoveDown and PlayerRect.bottom < WindowHeight:
        PlayerRect.move_ip(0, PlayerMoveRate)

    # moves enemy
    for e in enemys:
        if not ReverseCheat and not SlowCheat:
            b['rect'].move_ip(0, b['speed'])
        elif ReverseCheat:
            b['rect'].move_ip(0, -5)
        elif SlowCheat:
            b['rect'].move_ip(0, 1)

    for e in enemys:
        if b['rect'].top > WindowHeight:
            Enemys.remove(b)

    # draw world Surface
    WindowSurface.fill(BackgroundColor)

    # Draw score
    DrawText('Score: %s' % (score), font, WindowSurface, 10, 0)
    DrawText('Top Score: %s' % (TopScore), font, WindowSurface, 10, 40)

    # Draw Player
    WindowSurface.blit(PlayerRect)

    # draw enemys
    for e in enemys:
        WindowSurface.blit(b['surface'], b['rect'])

    pygame.display.update()

    # check if enemy hit Player
    if PlayerHitsEnemy(PlayerRect, enemys):
        if Score > TopScore:
            TopScore = Score  # sets new score
        break

    MainClock.tick(FPS)

# stops game and shows game over
DrawText('Game Over', font, WindowSurface, (WindowWidth / 3), (WindowHeight / 3))
DrawText('Press a key to play again', font, WindowSurface, (WindowWidth / 3) - 80, (WindowHeight / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

