import pygame
import LinkedLists

pygame.init()


class Segment:
    def __init__(self, colour, size, x_pos, y_pos):
        self.next = None  # Will point to the next segment
        self.prev = None

        # Segment data
        self.rect = pygame.Rect(x_pos, y_pos, size, size)
        self.col = colour

    def draw_segment(self, window):
        self.rect = pygame.draw.rect(window, self.col, self.rect)


class Snake:
    segments = LinkedLists.DoublyLinkedList()
    max_size = 10

    # the key to the directions dictionary
    snake_dir = "left"
    directions = {"left": [-1, 0], "right": [1, 0], "up": [0, -1], "down": [0, 1]}

    def __init__(self, x_pos, y_pos, x_speed, y_speed, size, colour):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.size = size
        self.colour = colour

        # Add a head segment
        self.segments.add_first(Segment(colour, size, x_pos, y_pos))

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

    def draw_snake(self, window):
        if self.segments.size > self.max_size:
            self.segments.delete_last()

        self.segments.add_first(Segment(self.colour, self.size, self.x_pos, self.y_pos))

        # Go through the linked list of segments and draw each one
        for c in range(self.segments.size):
            self.segments.get_at_pos(c).draw_segment(window)

    # The return is true if the snake head has collided with the apple's rectangle
    def eat(self, apple):
        if self.segments.head.rect.colliderect(apple):
            self.segments.add_first(Segment(self.colour, self.size, self.x_pos, self.y_pos))
            self.max_size += 5

            return True
        else:
            return False
