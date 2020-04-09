#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame

from blocks import *
from ghostblue import *
from ghostor import *
from ghostpink import *
from ghostred import *
from player import *
from points import *

WIN_WIDTH = 690  # Ширина создаваемого окна
WIN_HEIGHT = 790  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    background = pygame.image.load('pmanbg.png').convert()  # imports the game background
    pygame.display.set_caption("Pacman")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    # pygame.font.init()
    # font = pygame.font.Font('font.ttf', 30)

    hero = Player(345, 579)  # создаем героя по (x,y) координатам
    ghost1 = Ghost1(98, 658)
    ghost2 = Ghost2(98, 158)
    ghost3 = Ghost3(590, 658)
    ghost4 = Ghost4(590, 158)
    left = right = False  # по умолчанию - стоим
    up = down = False


    score = 0
    black = "fff123"


    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    points = []
    ghost = []
    ghost.append(ghost1)
    ghost.append(ghost2)
    ghost.append(ghost3)
    ghost.append(ghost4)

    tp = BlockTeleport(690, 350, 16, 350)
    tp1 = BlockTeleport(-5, 350, 669, 350)
    entities.add(tp1)


    entities.add(tp)
    platforms.append(tp)
    platforms.append(tp1)


    entities.add(hero)
    entities.add(points)
    entities.add(ghost1)
    entities.add(ghost2)
    entities.add(ghost3)
    entities.add(ghost4)

    level = [
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "x            xx            x",
        "x xxxx xxxxx xx xxxxx xxxx x",
        "x xxxx xxxxx xx xxxxx xxxx x",
        "x xxxx xxxxx xx xxxxx xxxx x",
        "x                          x",
        "x xxxx xx xxxxxxxx xx xxxx x",
        "x xxxx xx xxxxxxxx xx xxxx x",
        "x      xx    xx    xx      x",
        "xxxxxx xxxxx-xx-xxxxx xxxxxx",
        "-----x xxxxx-xx-xxxxx x-----",
        "-----x xx----------xx x-----",
        "-----x xx-xxxxxxxx-xx x-----",
        "xxxxxx xx-x------x-xx xxxxxx",
        "------ ---x------x--- ------",
        "xxxxxx xx-x------x-xx xxxxxx",
        "-----x xx-xxxxxxxx-xx x-----",
        "-----x xx----------xx x-----",
        "-----x xx-xxxxxxxx-xx x-----",
        "xxxxxx xx-xxxxxxxx-xx xxxxxx",
        "x            xx            x",
        "x xxxx xxxxx xx xxxxx xxxx x",
        "x xxxx xxxxx xx xxxxx xxxx x",
        "x   xx                xx   x",
        "xxx xx xx xxxxxxxx xx xx xxx",
        "xxx xx xx xxxxxxxx xx xx xxx",
        "x      xx    xx    xx      x",
        "x xxxxxxxxxx xx xxxxxxxxxx x",
        "x xxxxxxxxxx xx xxxxxxxxxx x",
        "x                          x",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"]

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "x":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == " ":
                po = Point(x, y)
                entities.add(po)
                points.append(po)

            x += 25 #PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += 25 #PLATFORM_HEIGHT =  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
                left = right = down = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
                up = right = down = False
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
                left = up = down = False
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
                left = right = up = False

        pygame.mixer.init()  # invokes mixer module (for music playback)

        pygame.mixer.music.load('pmandubstep.wav')  # load background music
        pygame.mixer.music.play(0, 0)  # set music playback to program initialisation

        for t in ghost:
            if sprite.collide_rect(hero, t):
                raise SystemExit("QUIT")

        for l in points:
            if sprite.collide_rect(hero, l):
                entities.remove(l)
                score += 1

        screen.blit(background, (-10, -15))  # draw the background screen

        hero.update(left, right, up, down, platforms, points, ghost)
        ghost1.update(platforms) #left1, right1, up1, down1, platforms)  # передвижение
        ghost2.update(platforms)
        ghost3.update(platforms)
        ghost4.update(platforms)
        entities.draw(screen) # отображение

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
