'''  Snake game'''

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
        self.GOsurf = myFont.render('Game over!', True, red)
        self.GOrect = GOsurf.get_rect()
        self.GOrect.midtop = (360, 15)
        self.playSurface.blit(GOsurf, GOrect)
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


def main():

    snake = Snake()

    # Main Logic of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    snake.changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    snake.changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == ord('w'):
                    snake.changeto = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    snake.changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # validation of direction
        if snake.changeto == 'RIGHT' and not snake.direction == 'LEFT':
            snake.direction = 'RIGHT'
        if snake.changeto == 'LEFT' and not snake.direction == 'RIGHT':
            snake.direction = 'LEFT'
        if snake.changeto == 'UP' and not snake.direction == 'DOWN':
            snake.direction = 'UP'
        if snake.changeto == 'DOWN' and not snake.direction == 'UP':
            snake.direction = 'DOWN'

        # Update snake position [x,y]
        if snake.direction == 'RIGHT':
            snake.snakePos[0] += 10
        if snake.direction == 'LEFT':
            snake.snakePos[0] -= 10
        if snake.direction == 'UP':
            snake.snakePos[1] -= 10
        if snake.direction == 'DOWN':
            snake.snakePos[1] += 10

        # Snake body mechanism
        snake.snakeBody.insert(0, list(snake.snakePos))
        if snake.snakePos[0] == snake.foodPos[0] and snake.snakePos[1] == snake.foodPos[1]:
            snake.score += 1
            snake.foodSpawn = False
        else:
            snake.snakeBody.pop()

        # Food Spawn
        if snake.foodSpawn == False:
            snake.foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        snake.foodSpawn = True

        # Background
        snake.playSurface.fill(snake.white)

        # Draw Snake
        for pos in snake.snakeBody:
            pygame.draw.rect(snake.playSurface, snake.green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(snake.playSurface, snake.brown, pygame.Rect(snake.foodPos[0], snake.foodPos[1], 10, 10))

        # Bound
        if snake.snakePos[0] > 710 or snake.snakePos[0] < 0:
            snake.gameOver()
        if snake.snakePos[1] > 450 or snake.snakePos[1] < 0:
            snake.gameOver()

        # Self hit
        for block in snake.snakeBody[1:]:
            if snake.snakePos[0] == block[0] and snake.snakePos[1] == block[1]:
                snake.gameOver()

        # common stuff
        snake.showScore()
        pygame.display.flip()

        snake.fpsController.tick(24)

main()