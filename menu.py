import sys
import os
import pygame
import datetime
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sqlite3

from main import playing_vuvvlic
from stats import MainWindow

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


def create_sql_table():
    con = sqlite3.connect('sql/database.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE solo (
                                                        id INTEGER PRIMARY KEY,
                                                        level TEXT,
                                                        point TEXT,
                                                        win_points TEXT,
                                                        passed TEXT,
                                                        date TEXT
                                                )''')
    con.close()


def drag_sql_info():
    global button, itog_total, necessary_total
    try:
        con = sqlite3.connect('sql/database.db')
        sql = (f'INSERT INTO solo (level, point, win_points, passed, date) values(?, ?, ?, ?, ?)')
        if itog_total >= necessary_total:
            pass_level = 'Да'
        else:
            pass_level = 'Нет'
        elements = [button, itog_total, necessary_total, pass_level, datetime.datetime.now()]
        with con:
            con.execute(sql, elements)
        con.close()
    except:
        pass


def show_info_on_table():
    global main_window
    con = sqlite3.connect('sql/database.db')
    cursor = con.cursor()
    data = con.execute(f"select count(*) from sqlite_master where type='table' "
                            f"and name='solo'")
    for i in data:
        if i[0] != 0:
            cursor.execute(f'SELECT * FROM solo')
            info = cursor.fetchall()
            main_window.tableWidget.setRowCount(len(info))
            for row, entry in enumerate(info):
                for column in range(5):  # левел, счёт, необходимо, пройдено, дата
                    main_window.tableWidget.setItem(row, column, QTableWidgetItem(entry[column + 1]))
        else:
           main_window.tableWidget.setRowCount(0)


def start_window():
    global black, white, button, itog_total, necessary_total, main_window
    pygame.init()
    size = width, height = 700, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Покер на костях')
    screen.fill((150, 100, 0))
    button1 = pygame.Rect(50, 50, 200, 50)
    button2 = pygame.Rect(50, 150, 200, 50)
    button3 = pygame.Rect(50, 250, 200, 50)
    back = pygame.image.load('data/back.png')
    running = True
    flag = False
    flag_sql = True
    flag_end = False
    itog_total = 0
    necessary_total = 0
    app = QApplication(sys.argv)
    main_window = MainWindow()

    while running:
        if flag is True:
            if flag_end and itog_total != "end":
                if os.path.exists('sql/database.db') and flag_sql:
                    drag_sql_info()
                    flag_sql = False
                elif flag_sql:
                    create_sql_table()
                    drag_sql_info()
                    flag_sql = False
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
            text3 = pygame.font.Font(None, 30).render('Статистика', True, white)
            screen.blit(text3, (70, 260))

            pic = pygame.image.load('data/orig.jpg')
            screen.blit(pic, (300, 65))

            if flag == 'stats':
                flag = False
                main_window.show()
                if os.path.exists('sql/database.db'):
                    show_info_on_table()
                app.aboutToQuit.connect(main_window.hide)
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
                    flag = 'stats'
            if event.type == pygame.MOUSEBUTTONDOWN and flag and not flag_end:
                level = ChekingTheCoordinates(event.pos[0], event.pos[1])
                button = level.check()
                if button == 1:
                    necessary_total = 70
                    itog_total = playing_vuvvlic(necessary_total)
                    if itog_total == "end":
                        flag_end = False
                    else:
                        flag_end = True
                        flag_sql = True
                if button == 2:
                    necessary_total = 100
                    itog_total = playing_vuvvlic(necessary_total)
                    if itog_total == "end":
                        flag_end = False
                    else:
                        flag_end = True
                        flag_sql = True
                if button == 3:
                    necessary_total = 150
                    itog_total = playing_vuvvlic(necessary_total)
                    if itog_total == "end":
                        flag_end = False
                    else:
                        flag_end = True
                        flag_sql = True
                if button == 4:
                    necessary_total = 200
                    itog_total = playing_vuvvlic(necessary_total)
                    if itog_total == "end":
                        flag_end = False
                    else:
                        flag_end = True
                        flag_sql = True
                if button == 5:
                    necessary_total = 250
                    itog_total = playing_vuvvlic(necessary_total)
                    if itog_total == "end":
                        flag_end = False
                    else:
                        flag_end = True
                        flag_sql = True
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
