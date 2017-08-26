import pygame, sys, random, time

class Snake:
    # check if pygame initialization throws any errors
    check_errors = pygame.init()

    if check_errors[1] > 0:
        print("( Had Errors {0}".format(check_errors[1]))
        sys.exit(-1)
    else:
        print("(+) PyGame successfully initialized!")

    def __init__(self):
        self.playSurface = pygame.display.set_mode((720, 460))
        pygame.display.set_caption('Snakey!')

        self.red = pygame.Color(255, 0, 0)  # gameover
        self.green = pygame.Color(0, 255, 0)  # snake
        self.black = pygame.Color(0, 0, 0)  # score
        self.white = pygame.Color(255, 255, 255)  # background
        self.brown = pygame.Color(165, 42, 42)  # food

        # FPS controller
        self.fpsController = pygame.time.Clock()

        # Important varibles
        self.snakePos = [100, 50]
        self.snakeBody = [[100, 50], [90, 50], [80, 50]]

        self.foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        self.foodSpawn = True

        self.direction = 'RIGHT'
        self.changeto = self.direction

        self.score = 0


# Game over function
    def gameOver(self):
        self.myFont = pygame.font.SysFont('monaco', 72)
        self.GOsurf = self.myFont.render('Game over!', True, self.red)
        self.GOrect = self.GOsurf.get_rect()
        self.GOrect.midtop = (360, 15)
        self.playSurface.blit(self.GOsurf, self.GOrect)
        self.showScore(0)
        pygame.display.flip()

        time.sleep(4)
        pygame.quit()  # pygame exit
        sys.exit()  # console exit


    def showScore(self,choice=1):
        self.sFont = pygame.font.SysFont('monaco', 24)
        self.Ssurf = self.sFont.render('Score : {0}'.format(self.score), True, self.black)
        self.Srect = self.Ssurf.get_rect()
        if choice == 1:
            self.Srect.midtop = (80, 10)
        else:
            self.Srect.midtop = (360, 120)
        self.playSurface.blit(self.Ssurf, self.Srect)