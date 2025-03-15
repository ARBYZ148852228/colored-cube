import pygame
import random
pygame.init()


WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # белый
NUM_RECTS = 19
MAX_RECT_SIZE = 300
SIZE_DIFFERENCE = 15


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вложенные Квадраты")


CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


rects = []


for i in range(NUM_RECTS):
    size = MAX_RECT_SIZE - i * SIZE_DIFFERENCE
    if size <= 0:
        break
    rect = pygame.Rect(CENTER_X - size//2, CENTER_Y - size//2, size, size)
    rects.append(rect)


clock = pygame.time.Clock()
running = True
time_passed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    time_passed += clock.tick(60)
    if time_passed >= 500:
        time_passed = 0
        for i in range(len(rects)):
            color = get_random_color()
            pygame.draw.rect(screen, color, rects[i])


    screen.fill(BACKGROUND_COLOR)


    for i in range(len(rects)):
        pygame.draw.rect(screen, get_random_color(), rects[i])

    pygame.display.flip()


pygame.quit()