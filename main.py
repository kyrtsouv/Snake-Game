import pygame,sys
from Snake import Snake
from random import randint
pygame.font.init()

BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

blocks = 30
block_size = 16
SIZE = blocks*block_size

UP = pygame.K_UP
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT


WIN = pygame.display.set_mode((SIZE,SIZE))
pygame.display.set_caption("Snake")
FONT = pygame.font.SysFont("None",100)
BOX = pygame.Rect(0,0,block_size,block_size)

GAME_OVER = pygame.USEREVENT + 1


def move(key,direction,snake):
    tail = snake.blocks[-1]
    if (snake.head[0] == 0 and key == LEFT) or (snake.head[0] == blocks - 1 and key == RIGHT) or (snake.head[1] == 0 and key == UP) or (snake.head[1] == blocks - 1 and key == DOWN):
        pygame.event.post(pygame.event.Event(GAME_OVER))    
        return tail,direction
    elif key == DOWN and direction != "U":
        direction = "D"
    elif key == UP and direction != "D":
        direction = "U"
    elif key == RIGHT and direction != "L":
        direction = "R"
    elif key == LEFT and direction != "R":
        direction = "L"
    snake.move(direction)

    if snake.head in snake.blocks[1:]:
        pygame.event.post(pygame.event.Event(GAME_OVER))
        return tail,direction
    else:    
        return tail,direction

def draw_window(snake,apple):
    WIN.fill(BLACK)
    for co in snake.blocks:
        BOX.x = co[0]*block_size
        BOX.y = co[1]*block_size
        pygame.draw.rect(WIN,GREEN,BOX)
    BOX.x = apple[0]*block_size
    BOX.y = apple[1]*block_size
    pygame.draw.rect(WIN,RED,BOX)
    pygame.display.update()

def post_end_loop(Score):
    game_over = FONT.render("Game Over",1,WHITE)
    score = FONT.render(f"Score: {Score}",1,WHITE)

    WIN.blit(game_over,(SIZE/2-game_over.get_width()/2,SIZE/2))
    WIN.blit(score,(SIZE/2-score.get_width()/2,SIZE/2+game_over.get_height()))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def get_apple(snake):
    apple = [randint(0,blocks-1),randint(0,blocks-1)]
    while apple in snake.blocks:
        apple = [randint(0,blocks-1),randint(0,blocks-1)]
    
    return apple

def main():
    Score = 0
    snake = Snake(blocks//2,blocks//2,block_size)
    direction = "D"
    key = DOWN
    key_set = False
    apple = get_apple(snake)
    clock = pygame.time.Clock()

    while True:
        draw_window(snake,apple)
        for i in range(10):
            clock.tick(100)
            for event in pygame.event.get():
                if event.type == GAME_OVER:
                    post_end_loop(Score)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and key_set == False:
                    key = event.key
                    key_set = True
        
        tail,direction = move(key,direction,snake)
        key_set = False

        if snake.head == apple:
            Score += 1
            apple = get_apple(snake)
            snake.add(tail)
           
main()