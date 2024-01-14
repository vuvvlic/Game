import pygame

set__ = 'Сет - для ее заполнения необходимо, чтобы выпало три одинаковых цифры (21 очко)'
kare = 'Каре - Она заполняется в том случае, если у вас выпало четыре одинаковых цифры (23 очка)'
full_h = 'Фулл–Хаус – это комбинация состоит из тройки (трех одинаковых цифр) и пары (двух одинаковых цифр) - 25 очков'
low_street = 'Малый стрит соответствует выпадению непрерывной последовательности из четырех цифр (30 очков)'
big_street = 'Большой стрит предполагает выпадение непрерывной последовательности из пяти цифр (40 очков)'
yahta = 'Яхта - при яхте должно выпасть пять одинаковых цифр (50 очков)'
shans = 'Шанс - сумму любой выпавшей комбинации цифр'
fon_color = (150, 70, 0)
black = (0, 0, 0)


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


def combo():
    pygame.init()
    size = width, height = 920, 500
    screen = pygame.display.set_mode(size)
    screen.fill(fon_color)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pl = ChekingTheCoordinates(event.pos[0], event.pos[1])
                check__ = pl.check()
                if check__ == 6:
                    return

        screen.fill(fon_color)
        text1 = pygame.font.Font(None, 23).render(set__, True, black)
        screen.blit(text1, (10, 15))
        text2 = pygame.font.Font(None, 23).render(kare, True, black)
        screen.blit(text2, (10, 55))
        text3 = pygame.font.Font(None, 23).render(full_h, True, black)
        screen.blit(text3, (10, 95))
        text4 = pygame.font.Font(None, 23).render(low_street, True, black)
        screen.blit(text4, (10, 135))
        text5 = pygame.font.Font(None, 23).render(big_street, True, black)
        screen.blit(text5, (10, 175))
        text6 = pygame.font.Font(None, 20).render(yahta, True, black)
        screen.blit(text6, (10, 215))
        text7 = pygame.font.Font(None, 20).render(shans, True, black)
        screen.blit(text7, (10, 255))
        back = pygame.image.load('data/back.png')
        screen.blit(back, (225, 400))

        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
