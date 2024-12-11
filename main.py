import sys
import random
import pygame


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class CircleApp:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Random Circles")
        self.circles = []

    def generate_random_circle(self):
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        radius = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = Circle(x, y, radius, color)
        self.circles.append(circle)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))  # Заливка фона белым
            for circle in self.circles:
                circle.draw(self.screen)

            pygame.display.flip()
            self.generate_random_circle()
            pygame.time.delay(500)  # Задержка в 500 мс

        pygame.quit()


if __name__ == "__main__":
    app = CircleApp(800, 600)
    app.run()
