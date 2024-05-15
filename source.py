import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Midpoint Displacement Algorithm")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Алгоритм Midpoint Displacement
def midpoint_displacement(start, end, roughness, vertical_displacement=None):
    if vertical_displacement is None:
        vertical_displacement = (start[1] + end[1]) / 2

    midpoint = (
    (start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + random.uniform(-vertical_displacement, vertical_displacement))
    if (end[0] - start[0]) > 2:
        midpoint_displacement(start, midpoint, roughness, vertical_displacement * roughness)
        midpoint_displacement(midpoint, end, roughness, vertical_displacement * roughness)
    else:
        pygame.draw.line(screen, WHITE, start, midpoint)
        pygame.draw.line(screen, WHITE, midpoint, end)


# Параметры алгоритма
roughness = 0.5
max_displacement = 180
screen.fill(BLACK)
start_point = (0, screen_height // 2)
end_point = (screen_width, screen_height // 2)
midpoint_displacement(start_point, end_point, roughness, max_displacement)
# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

pygame.quit()
