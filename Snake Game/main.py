import pygame
import sys
import random

pygame.init()

SW, SH = 800, 800

BLOCK_SIZE = 50
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir, self.ydir = 1, 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and self.ydir != -1:
                self.ydir = 1
                self.xdir = 0
            elif event.key == pygame.K_UP and self.ydir != 1:
                self.ydir = -1
                self.xdir = 0
            elif event.key == pygame.K_RIGHT and self.xdir != -1:
                self.ydir = 0
                self.xdir = 1
            elif event.key == pygame.K_LEFT and self.xdir != 1:
                self.ydir = 0
                self.xdir = -1

    def update(self):
        global apple

        for square in self.body:
            if self.head.colliderect(square):
                self.dead = True
            if not (0 <= self.head.x < SW and 0 <= self.head.y < SH):
                self.dead = True

        if self.dead:
            self.reset()
            apple = Apple()

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].topleft = self.body[i + 1].topleft
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.pop()


class Apple:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = random.randint(0, SW // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.y = random.randint(0, SH // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "orange", self.rect)


def draw_grid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))


snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        snake.handle_events(event)

    snake.update()

    screen.fill('black')
    draw_grid()

    apple.update()

    score = FONT.render(f"{len(snake.body)}", True, "white")

    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    screen.blit(score, score_rect)

    if snake.head.colliderect(apple.rect):
        snake.body.append(pygame.Rect(square.topleft, (BLOCK_SIZE, BLOCK_SIZE)))
        apple.spawn()

    pygame.display.update()
    clock.tick(10)  # Adjust the frames per second to your liking
