import pygame

pygame.init()

width = 800
height = 800

# Colours
white = (255, 255, 255)
black = (0, 0, 0)

# Other Vars
run = True

# Window
window = pygame.display.set_mode([width, height])
pygame.display.set_caption("Snake")

# Time keeping in pygame
clock = pygame.time.Clock()


class Snake:

    width = 15
    height = 15

    x_speed = 0
    y_speed = 0

    x_pos = 0
    y_pos = 0

    directions = {"left": [-1, 0], "right": [1, 0], "up": [0, -1], "down": [0, 1]}

    #  the key to the directions dictionary
    snake_dir = "left"

    def __init__(self, x_pos, y_pos, x_speed, y_speed, w, h):

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.width = w
        self.height = h

    def change_move_direction(self, key):
        if key == pygame.K_LEFT:
            self.snake_dir = "left"

        elif key == pygame.K_UP:
            self.snake_dir = "up"

        elif key == pygame.K_RIGHT:
            self.snake_dir = "right"

        elif key == pygame.K_DOWN:
            self.snake_dir = "down"

    def update_position(self):
        x_vel = self.x_speed * self.directions[self.snake_dir][0]
        y_vel = self.y_speed * self.directions[self.snake_dir][1]

        self.x_pos += x_vel
        self.y_pos += y_vel

    def draw_snake(self):
        pygame.draw.rect(window, black, (self.x_pos, self.y_pos, 15, 15))


# Get key input (QUIT, KEY DOWN, LEFT MOUSE CLICK, etc)
def get_key_entered(player):
    global run

    for event in pygame.event.get():
        print(pygame.event.get())

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            player.change_move_direction(event.key)


def main():

    # Construct a snake
    snake = Snake(400, 400, 3, 3, 15, 15)

    # Game loop
    while run:
        # Draw background, needs to happen every frame
        window.fill(white)

        get_key_entered(snake)
        snake.draw_snake()

        snake.update_position()

        # Displays the buffered data
        pygame.display.update()

        # Limit frames to 30
        clock.tick(30)


main()
