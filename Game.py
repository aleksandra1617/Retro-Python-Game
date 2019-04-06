import random
import pygame

from Snake import Snake
import GUI

pygame.init()

width = 1080
height = 720

# Colours
white = (255, 255, 255)
black = (0, 0, 0)

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


def main():
    view_width = 1000
    view_height = 600
    score = 0

    # Construct a snake
    snake = Snake(400, 400, 3, 3, 15, black)

    # Apple
    app_width = 10
    app_height = 10

    rand_x, rand_y = randomize_apple_pos(app_width, app_height)
    # Game loop
    while run:
        # Draw background, needs to happen every frame
        window.fill(white)

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

        # Displays the score
        GUI.display_text(window, "Score: " + str(score), 50, (0, 0, 0), [10, 10])
        #GUI.display_text(window, str(score), 50, (0, 0, 0), [135, 10])

        # Displays the buffered data
        pygame.display.update()

        # Limit frames to 60
        clock.tick(60)


main()
