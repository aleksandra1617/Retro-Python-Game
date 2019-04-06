import random
import pygame
import time

from Snake import Snake
import GUI

pygame.init()

width = 1080
height = 720

run = True

# Window
window = pygame.display.set_mode([width, height])
pygame.display.set_caption("Snake")

# Time keeping in pygame
clock = pygame.time.Clock()

# Get key input (QUIT, KEY DOWN, LEFT MOUSE CLICK, etc)
def get_key_entered(player):
    global run

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            player.change_move_direction(event.key)


# Randomly generates an apple
def randomize_apple_pos(app_width, app_height):
    global width, height  # window dimensions

    rand_x = random.randint(0, width - app_height)
    rand_y = random.randint(0, height - app_width)

    return rand_x, rand_y

def wait_for(miliseconds):
    clock = pygame.time.Clock()
    clock.tick()
    current_time = clock.get_time()
    print(current_time)
    clock.tick()

def main():
    view_width = 1000
    view_height = 600
    score = 0
    lives = 3
    liveTaken = False

    # Construct a snake
    snake = Snake(400, 400, 3, 3, 15, (0,0,0))

    # Apple
    app_width = 10
    app_height = 10

    rand_x, rand_y = randomize_apple_pos(app_width, app_height)

    # Game loop
    while run:
        # Draw background, needs to happen every frame
        window.fill((255, 255, 255))

        # Calculate game view rectangle starting position
        start_x = (width - view_width)/2
        start_y = (height - view_height)/2

        # Player
        get_key_entered(snake)

        game_view = pygame.draw.rect(window, (98, 244, 66), (start_x, start_y, view_width, view_height))
        game_border = pygame.draw.rect(window, (3, 132, 36), (start_x, start_y, view_width, view_height), 4)

        snake.draw_snake(window)
        snake.update_position()

        # Draw apple
        apple = pygame.draw.rect(window, (255, 0, 0), (rand_x, rand_y, app_width, app_height))

        # If the apple was eaten
        if snake.eat(apple):
            # Spawn a new apple
            rand_x, rand_y = randomize_apple_pos(app_width, app_height)

            # Update score
            score += 5

        snakeX = snake.segments.head.rect.x
        snakeY = snake.segments.head.rect.y

        collide_top_left = game_border.collidepoint(snakeX, snakeY)
        collide_top_right = game_border.collidepoint(snakeX+snake.size, snakeY+snake.size)

        if not (collide_top_left and collide_top_right):
            lives -= 1
            liveTaken = True

        wait_for(1000)

        # Displays TEXT
        GUI.display_text(window, "Score: " + str(score), 50, (0, 0, 0), [40, 10])
        GUI.display_text(window, "Lives: " + str(lives), 50, (0, 0, 0), [910, 10])

        # Displays the buffered data
        pygame.display.update()

        # Limit frames to 60
        clock.tick(60)


main()
