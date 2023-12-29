from random import choices

import pygame

cubes = [(1, "number/1.png"), (2, "number/2.png"), (3, "number/3.png"), (4, "number/4.png"), (5, "number/5.png"),
         (6, "number/6.png")]


class ChekingTheCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kubiki = []

    def random_cub(self):
        self.kubiki = choices(cubes, k=5)

    def check(self):
        if self.x in range(753, 878) and self.y in range(503, 631):
            self.random_cub()
            return self.kubiki



if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 700
    screen = pygame.display.set_mode(size)
    screen.fill((150, 100, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                play = ChekingTheCoordinates(event.pos[0], event.pos[1])
                kubs = play.check()
                if type(kubs).__name__ == 'list':
                    pass
        picture1 = pygame.image.load("data/pole_one.png")
        picture2 = pygame.image.load("data/pole_two.png")
        roll_the_dice = pygame.image.load("data/brosok.png")
        screen.blit(roll_the_dice, (750, 500))
        screen.blit(picture1, (155, 50))
        screen.blit(picture2, (413, 55))
        pygame.display.flip()
    pygame.quit()
