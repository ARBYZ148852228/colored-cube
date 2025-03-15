import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Квадраты")

# Определение количества квадратов
NUM_SQUARES = 19

# Размер самого большого квадрата
MAX_SQUARE_SIZE = 300

# Расстояние между квадратами
SQUARE_GAP = 15

# Центр экрана
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

# Список для хранения объектов квадратов
squares = []

# Функция для создания квадратов
def create_squares():
    global squares
    size = MAX_SQUARE_SIZE
    for i in range(NUM_SQUARES):
        # Создаём объект квадрата
        square = pygame.Surface((size, size))
        square.fill(random_color())
        rect = square.get_rect()
        rect.center = (CENTER_X, CENTER_Y)
        squares.append([square, rect])
        size -= SQUARE_GAP

# Функция для получения случайного цвета
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Функция для отображения квадратов
def draw_squares():
    for idx, (surface, rect) in enumerate(squares):
        screen.blit(surface, rect)
        # Изменяем цвет каждого квадрата каждую секунду
        if idx != 0 and pygame.time.get_ticks() % 100 == 0:
            surface.fill(random_color())

# Основной цикл игры
running = True
create_squares()
while running:
    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очищаем экран
    screen.fill((255, 255, 255))  # Белый фон

    # Отображаем квадраты
    draw_squares()

    # Обновляем экран
    pygame.display.update()

# Завершаем работу Pygame
pygame.quit()