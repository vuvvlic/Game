import pygame

from main import playing_vuvvlic

black = (0, 0, 0)
white = (255, 255, 255)
fon_color = (150, 70, 0)


class ChekingTheCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check(self):
        if self.x in range(50, 170) and self.y in range(100, 145):
            return 1
        if self.x in range(250, 375) and self.y in range(100, 145):
            return 2
        if self.x in range(450, 570) and self.y in range(100, 145):
            return 3
        if self.x in range(150, 265) and self.y in range(200, 245):
            return 4
        if self.x in range(350, 470) and self.y in range(200, 240):
            return 5
        if self.x in range(225, 475) and self.y in range(400, 470):
            return 6
        return


def start_window():
    global black, white
    pygame.init()
    size = width, height = 700, 500
    screen = pygame.display.set_mode(size)
    screen.fill((150, 100, 0))
    button1 = pygame.Rect(50, 50, 200, 50)
    button2 = pygame.Rect(50, 150, 200, 50)
    button3 = pygame.Rect(50, 250, 200, 50)
    back = pygame.image.load('data/back.png')
    running = True
    flag = False
    flag_end = False
    itog_total = 0
    necessary_total = 0

    while running:
        if flag:
            if flag_end:
                if itog_total >= necessary_total:
                    word = f"Вы набрали нужное кол-во очков. {itog_total} из {necessary_total}"
                    screen.fill(fon_color)
                    winner = pygame.font.Font(None, 35)
                    winner__ = winner.render(word, True, (0, 0, 0))
                    screen.blit(winner__, (10, 50))
                    sl = pygame.font.Font(None, 60).render('Победа!!!', True, (0, 0, 0))
                    screen.blit(sl, (200, 110))
                else:
                    word = f"Вы не набрали нужное кол-во очков. {itog_total} из {necessary_total}"
                    screen.fill(fon_color)
                    winner = pygame.font.Font(None, 35)
                    winner__ = winner.render(word, True, (0, 0, 0))
                    screen.blit(winner__, (10, 50))
                    sl = pygame.font.Font(None, 60).render('Проигрыш', True, (0, 0, 0))
                    screen.blit(sl, (200, 110))
                screen.blit(back, (225, 400))
            else:
                screen.fill(fon_color)
                level_1 = pygame.image.load('levels/level1.png')
                level_2 = pygame.image.load('levels/level2.png')
                level_3 = pygame.image.load('levels/level3.png')
                level_4 = pygame.image.load('levels/level4.png')
                level_5 = pygame.image.load('levels/level5.png')
                screen.blit(back, (225, 400))
                screen.blit(level_1, (50, 100))
                screen.blit(level_2, (250, 100))
                screen.blit(level_3, (450, 100))
                screen.blit(level_4, (150, 200))
                screen.blit(level_5, (350, 200))

        else:
            screen.fill((150, 70, 0))
            pygame.draw.rect(screen, black, button1)
            text1 = pygame.font.Font(None, 30).render('Уровни', True, white)
            screen.blit(text1, (70, 60))

            pygame.draw.rect(screen, black, button2)
            text2 = pygame.font.Font(None, 30).render('Игра на двоих', True, white)
            screen.blit(text2, (70, 160))

            pygame.draw.rect(screen, black, button3)
            text3 = pygame.font.Font(None, 30).render('', True, white)
            screen.blit(text3, (70, 260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not flag:
                mousepos = event.pos
                if button1.collidepoint(mousepos):
                    flag = True
                elif button2.collidepoint(mousepos):
                    pass
                elif button3.collidepoint(mousepos):
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN and flag and not flag_end:
                level = ChekingTheCoordinates(event.pos[0], event.pos[1])
                button = level.check()
                if button == 1:
                    itog_total = playing_vuvvlic()
                    necessary_total = 70
                    flag_end = True
                if button == 2:
                    itog_total = playing_vuvvlic()
                    necessary_total = 100
                    flag_end = True
                if button == 3:
                    itog_total = playing_vuvvlic()
                    necessary_total = 150
                    flag_end = True
                if button == 4:
                    itog_total = playing_vuvvlic()
                    necessary_total = 200
                    flag_end = True
                if button == 5:
                    itog_total = playing_vuvvlic()
                    necessary_total = 250
                    flag_end = True
                if button == 6:
                    flag = False
                screen = pygame.display.set_mode(size)
            if event.type == pygame.MOUSEBUTTONDOWN and flag and flag_end:
                level = ChekingTheCoordinates(event.pos[0], event.pos[1])
                button = level.check()
                if button == 6:
                    flag_end = False

        pygame.display.update()
        pygame.display.flip()
