from random import choices

import pygame

cubes = [(1, "number/1.png"), (2, "number/2.png"), (3, "number/3.png"), (4, "number/4.png"), (5, "number/5.png"),
         (6, "number/6.png")]


def poker(llist):
    num_1 = llist.count(1) * 1
    num_2 = llist.count(2) * 2
    num_3 = llist.count(3) * 3
    num_4 = llist.count(4) * 4
    num_5 = llist.count(5) * 5
    num_6 = llist.count(6) * 6
    if len(set(llist[:])) == 1:
        yahta = 50
    else:
        yahta = 0
    if len(set(llist[:])) == 2:
        if llist.count(llist[0]) in [2, 3]:
            full_house = 25
            kare = 0
        else:
            kare = 23
            full_house = 0
    else:
        full_house = 0
        kare = 0
    if len(set(llist[:])) == 3:
        three = 21
    else:
        three = 0
    if len(set(llist[:])) == 4:
        low_street = 30
    else:
        low_street = 0
    if len(set(llist[:])) == 5:
        big_street = 40
    else:
        big_street = 0
    list__ = [num_1, num_2, num_3, num_4, num_5, num_6, three, kare, full_house, low_street, big_street, yahta,
              sum(llist)]
    return list__


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
                    screen.fill((150, 100, 0))
                    pic_cub_1 = pygame.image.load(kubs[0][1])
                    pic_cub_2 = pygame.image.load(kubs[1][1])
                    pic_cub_3 = pygame.image.load(kubs[2][1])
                    pic_cub_4 = pygame.image.load(kubs[3][1])
                    pic_cub_5 = pygame.image.load(kubs[4][1])
                    screen.blit(pic_cub_1, (5, 503))
                    screen.blit(pic_cub_2, (155, 503))
                    screen.blit(pic_cub_3, (305, 503))
                    screen.blit(pic_cub_4, (455, 503))
                    screen.blit(pic_cub_5, (605, 503))
                    _list = poker([kubs[0][0], kubs[1][0], kubs[2][0], kubs[3][0], kubs[4][0]])
                    numbers = []
                    for i in _list:
                        fi = pygame.font.Font(None, 48)
                        text = fi.render(str(i), True, pygame.Color((0, 0, 0)))
                        numbers.append(text)
                    print(numbers[0])
                    screen.blit(numbers[0], (380, 60))
        picture1 = pygame.image.load("data/pole_one.png")
        picture2 = pygame.image.load("data/pole_two.png")
        roll_the_dice = pygame.image.load("data/brosok.png")
        screen.blit(roll_the_dice, (750, 500))
        screen.blit(picture1, (155, 50))
        screen.blit(picture2, (413, 55))
        pygame.display.flip()
    pygame.quit()
