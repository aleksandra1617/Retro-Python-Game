import random
import pygame
import time
import math

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
def randomize_apple_pos(app_width, app_height, game_view):
    global width, height  # window dimensions

    rand_x = random.randint(game_view[0], game_view[2] - app_height)
    rand_y = random.randint(game_view[1], game_view[3] - app_width)

    return rand_x, rand_y


def wait_for(start_time, curr_time):
    elapsed_time = curr_time - start_time

    #if elapsed_time > seconds:
        #return True


def main():
    start_time = time.time()
    timer_start = 0

    view_width = 1000
    view_height = 600

    # Calculate game view rectangle starting position
    start_x = (width - view_width) / 2
    start_y = (height - view_height) / 2

    game_view_data = (start_x, start_y, view_width, view_height)

    score = 0
    lives = 3
    live_taken = False

    # Construct a snake
    snake = Snake(400, 400, 3, 3, 15, (0, 0, 0))

    # Apple
    app_width = 10
    app_height = 10

    rand_x, rand_y = randomize_apple_pos(app_width, app_height, game_view_data)

    # Game loop
    while run:
        curr_time = time.time()

        # Draw background, needs to happen every frame
        window.fill((255, 255, 255))

        # Player
        get_key_entered(snake)

        game_view = pygame.draw.rect(window, (98, 244, 66), game_view_data)
        game_border = pygame.draw.rect(window, (3, 132, 36), game_view_data, 4)

        snake.draw_snake(window)
        snake.update_position()

        # Draw apple
        apple = pygame.draw.rect(window, (255, 0, 0), (rand_x, rand_y, app_width, app_height))

        # If the apple was eaten
        if snake.eat(apple):
            # Spawn a new apple
            rand_x, rand_y = randomize_apple_pos(app_width, app_height, game_view_data)

            # Update score
            score += 5

        snakeX = snake.segments.head.rect.x
        snakeY = snake.segments.head.rect.y

        # The top left and top right corners of the snake head.
        # Those exact points create the exact boundary needed and at the same time save computation.
        point1 = (snakeX, snakeY)
        point2 = (snakeX+snake.size, snakeY+snake.size)

        not_collide_top_left = not game_border.collidepoint(point1)
        not_collide_top_right = not game_border.collidepoint(point2)

        if not_collide_top_left and not_collide_top_right and not live_taken:
            timer_start = curr_time
            lives -= 1
            live_taken = True

        if round(curr_time - timer_start, 0) == 5:
            live_taken = False

        # Displays TEXT
        GUI.display_text(window, "Score: " + str(score), 50, (0, 0, 0), [40, 10])
        GUI.display_text(window, "Lives: " + str(lives), 50, (0, 0, 0), [910, 10])

        # Displays the buffered data
        pygame.display.update()

        # Limit frames to 60
        clock.tick(60)


main()
