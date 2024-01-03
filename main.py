from random import choices

import pygame

cubes = [(1, "number/1.png"), (2, "number/2.png"), (3, "number/3.png"), (4, "number/4.png"), (5, "number/5.png"),
         (6, "number/6.png")]

lock_cubes = [(1, "number/1lock.png"), (2, "number/2lock.png"), (3, "number/3lock.png"), (4, "number/4lock.png"),
              (5, "number/5lock.png"), (6, "number/6lock.png")]

playing_numbers = []

hod_play = 0

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
    11: ''
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
current_point = None


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

    def check_flag(self):
        global flag_low_street, flag_big_street, flag_4, flag_1, flag_shans, flag_yahta
        global flag_full_house, flag_kare, flag_set, flag_2, flag_3, flag_5, flag_6
        if flag_1 != 'yellow':
            flag_1 = True
        if flag_2 != 'yellow':
            flag_2 = True
        if flag_3 != 'yellow':
            flag_3 = True
        if flag_4 != 'yellow':
            flag_4 = True
        if flag_5 != 'yellow':
            flag_5 = True
        if flag_6 != 'yellow':
            flag_6 = True
        if flag_set != 'yellow':
            flag_set = True
        if flag_kare != 'yellow':
            flag_kare = True
        if flag_full_house != 'yellow':
            flag_full_house = True
        if flag_low_street != 'yellow':
            flag_low_street = True
        if flag_big_street != 'yellow':
            flag_big_street = True
        if flag_yahta != 'yellow':
            flag_yahta = True
        if flag_shans != 'yellow':
            flag_shans = True

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
        global count_move
        global current_point
        if self.x in range(753, 878) and self.y in range(503, 631):
            count_move -= 1
            if count_move >= 0:
                self.random_cub()
                return self.kubiki
        elif self.x in range(730, 890) and self.y in range(400, 482) and current_point:
            count_move = 3
            return 'play'
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
        elif (self.x in range(367, 411) and self.y in range(53, 95) and flag_1 and playing_numbers
              and flag_1 != 'yellow'):
            current_point = [playing_numbers[0], 1]
            self.check_flag()
            flag_1 = 'red'
            return 'select'
        elif (self.x in range(367, 411) and self.y in range(97, 140) and flag_2 and playing_numbers
              and flag_2 != 'yellow'):
            current_point = [playing_numbers[1], 2]
            self.check_flag()
            flag_2 = 'red'
            return 'select'
        elif (self.x in range(367, 411) and self.y in range(139, 185) and flag_3 and playing_numbers
              and flag_3 != 'yellow'):
            current_point = [playing_numbers[2], 3]
            self.check_flag()
            flag_3 = 'red'
            return 'select'
        elif (self.x in range(367, 411) and self.y in range(185, 230) and flag_4 and playing_numbers
              and flag_4 != 'yellow'):
            current_point = [playing_numbers[3], 4]
            self.check_flag()
            flag_4 = 'red'
            return 'select'
        elif (self.x in range(367, 411) and self.y in range(230, 275) and flag_5 and playing_numbers
              and flag_5 != 'yellow'):
            current_point = [playing_numbers[4], 5]
            self.check_flag()
            flag_5 = 'red'
            return 'select'
        elif (self.x in range(367, 411) and self.y in range(275, 320) and flag_6 and playing_numbers
              and flag_6 != 'yellow'):
            current_point = [playing_numbers[5], 6]
            self.check_flag()
            flag_6 = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(53, 95) and flag_set and playing_numbers
              and flag_set != 'yellow'):
            current_point = [playing_numbers[6], 7]
            self.check_flag()
            flag_set = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(97, 139) and flag_kare and playing_numbers
              and flag_kare != 'yellow'):
            current_point = [playing_numbers[7], 8]
            self.check_flag()
            flag_kare = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(140, 185) and flag_full_house and playing_numbers
              and flag_full_house != 'yellow'):
            current_point = [playing_numbers[8], 9]
            self.check_flag()
            flag_full_house = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(185, 230) and flag_low_street and playing_numbers
              and flag_low_street != 'yellow'):
            current_point = [playing_numbers[9], 10]
            self.check_flag()
            flag_low_street = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(230, 275) and flag_big_street and playing_numbers
              and flag_big_street != 'yellow'):
            current_point = [playing_numbers[10], 11]
            self.check_flag()
            flag_big_street = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(275, 320) and flag_yahta and playing_numbers
              and flag_yahta != 'yellow'):
            current_point = [playing_numbers[11], 12]
            self.check_flag()
            flag_yahta = 'red'
            return 'select'
        elif (self.x in range(625, 665) and self.y in range(320, 365) and flag_shans and playing_numbers
              and flag_shans != 'yellow'):
            current_point = [playing_numbers[12], 13]
            self.check_flag()
            flag_shans = 'red'
            return 'select'
        return None


def playing_vuvvlic():
    global playing_numbers, numbers_sl, flag_low_street, flag_big_street, flag_4, flag_1, flag_shans, flag_yahta
    global hod_play, flag_full_house, flag_kare, flag_set, flag_2, flag_3, flag_5, flag_6, count_move, current_point
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
    count_move = 3
    end_move = False
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
        11: ''
    }
    total = 0
    hod_play = 0
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
                    end_move = False
                    current_point = None
                    play.check_flag()
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
                elif kubs == 'play':
                    ChekingTheCoordinates.last_cubes = None
                    if current_point[1] == 1:
                        flag_1 = 'yellow'
                    elif current_point[1] == 2:
                        flag_2 = 'yellow'
                    elif current_point[1] == 3:
                        flag_3 = 'yellow'
                    elif current_point[1] == 4:
                        flag_4 = 'yellow'
                    elif current_point[1] == 5:
                        flag_5 = 'yellow'
                    elif current_point[1] == 6:
                        flag_6 = 'yellow'
                    elif current_point[1] == 7:
                        flag_set = 'yellow'
                    elif current_point[1] == 8:
                        flag_kare = 'yellow'
                    elif current_point[1] == 9:
                        flag_full_house = 'yellow'
                    elif current_point[1] == 10:
                        flag_low_street = 'yellow'
                    elif current_point[1] == 11:
                        flag_big_street = 'yellow'
                    elif current_point[1] == 12:
                        flag_yahta = 'yellow'
                    elif current_point[1] == 13:
                        flag_shans = 'yellow'
                    total += current_point[0]
                    current_point = None
                    playing_numbers = []
                    hod_play += 1
                    end_move = True
                    if hod_play == 13:
                        return total
                    screen.fill((150, 100, 0))
                    izob = pygame.font.Font(None, 48)
                    text__ = izob.render('Счёт:', True, pygame.Color((0, 0, 0)))  # изображение счета
                    screen.blit(text__, (780, 50))
                    izob1 = pygame.font.Font(None, 48)
                    text__1 = izob1.render(f'{total}', True, pygame.Color((0, 0, 0)))  # изображение счета цифра
                    screen.blit(text__1, (810, 80))
                elif kubs == 'select':
                    numbers_sl[current_point[1]] = current_point[0]

            picture1 = pygame.image.load("data/pole_one.png")
            picture2 = pygame.image.load("data/pole_two.png")
            # делаю повторно потому что чтоб счет изображения сохранялся
            izob = pygame.font.Font(None, 48)
            text__ = izob.render('Счёт:', True, pygame.Color((0, 0, 0)))
            screen.blit(text__, (780, 50))
            izob1 = pygame.font.Font(None, 48)
            text__1 = izob1.render(f'{total}', True, pygame.Color((0, 0, 0)))
            screen.blit(text__1, (810, 80))
            if current_point is None:
                play_button = pygame.image.load("data/lockplay.png")
                screen.blit(play_button, (730, 400))
            else:
                play_button = pygame.image.load("data/play.png")
                screen.blit(play_button, (730, 400))
            if count_move == 3:
                roll_the_dice = pygame.image.load("data/brosok1.png")
                screen.blit(roll_the_dice, (750, 500))
            elif count_move == 2:
                roll_the_dice = pygame.image.load("data/brosok2.png")
                screen.blit(roll_the_dice, (750, 500))
            elif count_move == 1:
                roll_the_dice = pygame.image.load("data/brosok3.png")
                screen.blit(roll_the_dice, (750, 500))
            elif count_move <= 0:
                roll_the_dice = pygame.image.load("data/brosok4.png")
                screen.blit(roll_the_dice, (750, 500))
            screen.blit(picture1, (155, 50))
            screen.blit(picture2, (413, 55))
            s_pic_red = pygame.font.Font(None, 48)
            if numbers:
                if flag_1 == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[1]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 60))
                elif flag_1 == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[1]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (370, 60))
                elif not end_move:
                    screen.blit(numbers[0], (370, 60))
                if flag_2 == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[2]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 110))
                elif flag_2 == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[2]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (370, 110))
                elif not end_move:
                    screen.blit(numbers[1], (370, 110))
                if flag_3 == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[3]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 150))
                elif flag_3 == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[3]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (370, 150))
                elif not end_move:
                    screen.blit(numbers[2], (370, 150))
                if flag_4 == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[4]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 200))
                elif flag_4 == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[4]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (370, 200))
                elif not end_move:
                    screen.blit(numbers[3], (370, 200))
                if flag_5 == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[5]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 240))
                elif flag_5 == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[5]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (370, 240))
                elif not end_move:
                    screen.blit(numbers[4], (370, 240))
                if flag_6 == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[6]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (370, 285))
                elif flag_6 == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[6]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (370, 285))
                elif not end_move:
                    screen.blit(numbers[5], (370, 285))
                if flag_set == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[7]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 60))
                elif flag_set == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[7]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 60))
                elif not end_move:
                    screen.blit(numbers[6], (630, 60))
                if flag_kare == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[8]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 110))
                elif flag_kare == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[8]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 110))
                elif not end_move:
                    screen.blit(numbers[7], (630, 110))
                if flag_full_house == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[9]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 150))
                elif flag_full_house == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[9]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 150))
                elif not end_move:
                    screen.blit(numbers[8], (630, 150))
                if flag_low_street == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[10]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 200))
                elif flag_low_street == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[10]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 200))
                elif not end_move:
                    screen.blit(numbers[9], (630, 200))
                if flag_big_street == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[11]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 240))
                elif flag_big_street == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[11]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 240))
                elif not end_move:
                    screen.blit(numbers[10], (630, 240))
                if flag_yahta == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[12]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 285))
                elif flag_yahta == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[12]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 285))
                elif not end_move:
                    screen.blit(numbers[11], (630, 285))
                if flag_shans == 'red':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[13]), True, pygame.Color((255, 0, 0)))
                    screen.blit(s_pic_red__, (630, 325))
                elif flag_shans == 'yellow':
                    s_pic_red__ = s_pic_red.render(str(numbers_sl[13]), True, pygame.Color((255, 255, 0)))
                    screen.blit(s_pic_red__, (630, 325))
                elif not end_move:
                    screen.blit(numbers[12], (630, 325))
            pygame.display.update()
            pygame.display.flip()
    pygame.quit()
