from random import choices

import pygame

cubes = [(1, "number/1.png"), (2, "number/2.png"), (3, "number/3.png"), (4, "number/4.png"), (5, "number/5.png"),
         (6, "number/6.png")]

lock_cubes = [(1, "number/1lock.png"), (2, "number/2lock.png"), (3, "number/3lock.png"), (4, "number/4lock.png"),
              (5, "number/5lock.png"), (6, "number/6lock.png")]

playing_numbers = []

numbers_sl = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: '',
    7: '',
    8: '',
    9: '',
    10: '',
    12: '',
    13: '',
}

flag_1 = True
flag_2 = True
flag_3 = True
flag_4 = True
flag_5 = True
flag_6 = True
flag_set = True
flag_kare = True
flag_full_house = True
flag_low_street = True
flag_big_street = True
flag_yahta = True
flag_shans = True


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
    last_cubes = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kubiki = []

    def random_cub(self):
        if ChekingTheCoordinates.last_cubes is None:  # если ещё нету сохранённых кубиков
            for _ in range(5):
                self.kubiki.extend(choices(cubes))
            ChekingTheCoordinates.last_cubes = self.kubiki
        else:  # если уже есть сгенерированные кубики
            for cube in range(len(ChekingTheCoordinates.last_cubes)):
                if not 'lock' in ChekingTheCoordinates.last_cubes[cube][1]:
                    ChekingTheCoordinates.last_cubes[cube] = choices(cubes)[0]
            self.kubiki = ChekingTheCoordinates.last_cubes

    def locks_cube(self, cube):
        if 'lock' in ChekingTheCoordinates.last_cubes[cube][1]:
            ChekingTheCoordinates.last_cubes[cube] = cubes[ChekingTheCoordinates.last_cubes[cube][0] - 1]
        else:
            ChekingTheCoordinates.last_cubes[cube] = lock_cubes[ChekingTheCoordinates.last_cubes[cube][0] - 1]
        self.kubiki = ChekingTheCoordinates.last_cubes

    def check(self):
        global playing_numbers
        global flag_1
        global flag_2
        global flag_3
        global flag_4
        global flag_5
        global flag_6
        global flag_set
        global flag_kare
        global flag_full_house
        global flag_big_street
        global flag_low_street
        global flag_yahta
        global flag_shans

        if self.x in range(753, 878) and self.y in range(503, 631):
            self.random_cub()
            return self.kubiki
        elif self.x in range(5, 145) and self.y in range(503, 640) and ChekingTheCoordinates.last_cubes is not None:
            self.locks_cube(0)
            return self.kubiki
        elif self.x in range(155, 295) and self.y in range(503, 640) and ChekingTheCoordinates.last_cubes is not None:
            self.locks_cube(1)
            return self.kubiki
        elif self.x in range(305, 445) and self.y in range(503, 640) and ChekingTheCoordinates.last_cubes is not None:
            self.locks_cube(2)
            return self.kubiki
        elif self.x in range(455, 595) and self.y in range(503, 640) and ChekingTheCoordinates.last_cubes is not None:
            self.locks_cube(3)
            return self.kubiki
        elif self.x in range(605, 740) and self.y in range(503, 643) and ChekingTheCoordinates.last_cubes is not None:
            self.locks_cube(4)
            return self.kubiki
        elif self.x in range(367, 411) and self.y in range(53, 95) and flag_1 and playing_numbers:
            flag_1 = False
            return (playing_numbers[0], 1)
        elif self.x in range(367, 411) and self.y in range(97, 140) and flag_2 and playing_numbers:
            flag_2 = False
            return (playing_numbers[1], 2)
        elif self.x in range(367, 411) and self.y in range(139, 185) and flag_3 and playing_numbers:
            flag_3 = False
            return (playing_numbers[2], 3)
        elif self.x in range(367, 411) and self.y in range(185, 230) and flag_4 and playing_numbers:
            flag_4 = False
            return (playing_numbers[3], 4)
        elif self.x in range(367, 411) and self.y in range(230, 275) and flag_5 and playing_numbers:
            flag_5 = False
            return (playing_numbers[4], 5)
        elif self.x in range(367, 411) and self.y in range(275, 320) and flag_6 and playing_numbers:
            flag_6 = False
            return (playing_numbers[5], 6)
        elif self.x in range(625, 665) and self.y in range(53, 95) and flag_set and playing_numbers:
            flag_set = False
            return (playing_numbers[6], 7)
        elif self.x in range(625, 665) and self.y in range(97, 139) and flag_kare and playing_numbers:
            flag_kare = False
            return (playing_numbers[7], 8)
        elif self.x in range(625, 665) and self.y in range(140, 185) and flag_full_house and playing_numbers:
            flag_full_house = False
            return (playing_numbers[8], 9)
        elif self.x in range(625, 665) and self.y in range(185, 230) and flag_low_street and playing_numbers:
            flag_low_street = False
            return (playing_numbers[9], 10)
        elif self.x in range(625, 665) and self.y in range(230, 275) and flag_big_street and playing_numbers:
            flag_big_street = False
            return (playing_numbers[10], 11)
        elif self.x in range(625, 665) and self.y in range(275, 320) and flag_yahta and playing_numbers:
            flag_yahta = False
            return (playing_numbers[11], 12)
        elif self.x in range(625, 665) and self.y in range(320, 365) and flag_shans and playing_numbers:
            flag_shans = False
            return (playing_numbers[12], 13)
        return None


def playing_vuvvlic():
    global playing_numbers
    total = 0
    pygame.init()
    size = width, height = 900, 700
    screen = pygame.display.set_mode(size)
    screen.fill((150, 100, 0))
    running = True
    numbers = []
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
                    playing_numbers = _list[:]
                    numbers = []
                    for i in _list:
                        fi = pygame.font.Font(None, 48)
                        text = fi.render(str(i), True, pygame.Color((0, 0, 0)))
                        numbers.append(text)
                elif kubs is not None:
                    numbers_sl[kubs[1]] = kubs[0]
                    total += kubs[0]  # сумируется счет
                    screen.fill((150, 100, 0))
                    izob = pygame.font.Font(None, 48)
                    text__ = izob.render('Счёт:', True, pygame.Color((0, 0, 0)))  # изображение счета
                    screen.blit(text__, (780, 50))
                    izob1 = pygame.font.Font(None, 48)
                    text__1 = izob1.render(f'{total}', True, pygame.Color((0, 0, 0)))  # изображение счета цифра
                    screen.blit(text__1, (810, 80))

            picture1 = pygame.image.load("data/pole_one.png")
            picture2 = pygame.image.load("data/pole_two.png")
            roll_the_dice = pygame.image.load("data/brosok.png")
            # делаю повторно потому что чтоб счет изображения сохранялся
            izob = pygame.font.Font(None, 48)
            text__ = izob.render('Счёт:', True, pygame.Color((0, 0, 0)))
            screen.blit(text__, (780, 50))
            izob1 = pygame.font.Font(None, 48)
            text__1 = izob1.render(f'{total}', True, pygame.Color((0, 0, 0)))
            screen.blit(text__1, (810, 80))
            screen.blit(roll_the_dice, (750, 500))
            screen.blit(picture1, (155, 50))
            screen.blit(picture2, (413, 55))
            if numbers:
                if flag_1:
                    screen.blit(numbers[0], (370, 60))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[1]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 60))
                if flag_2:
                    screen.blit(numbers[1], (370, 110))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[2]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 110))
                if flag_3:
                    screen.blit(numbers[2], (370, 150))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[3]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 150))
                if flag_4:
                    screen.blit(numbers[3], (370, 200))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[4]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 200))
                if flag_5:
                    screen.blit(numbers[4], (370, 240))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[5]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 240))
                if flag_6:
                    screen.blit(numbers[5], (370, 285))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[6]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 285))
                if flag_set:
                    screen.blit(numbers[6], (630, 60))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[7]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 60))
                if flag_kare:
                    screen.blit(numbers[7], (630, 110))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[8]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 110))
                if flag_full_house:
                    screen.blit(numbers[8], (630, 150))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[9]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 150))
                if flag_low_street:
                    screen.blit(numbers[9], (630, 200))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[10]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 200))
                if flag_big_street:
                    screen.blit(numbers[10], (630, 240))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[11]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 240))
                if flag_yahta:
                    screen.blit(numbers[11], (630, 285))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[12]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 285))
                if flag_shans:
                    screen.blit(numbers[12], (630, 325))
                else:
                    s_pic_red = pygame.font.Font(None, 48)
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[13]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 325))
            pygame.display.update()
            pygame.display.flip()
    pygame.quit()
