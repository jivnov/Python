#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

import blocks
import pyganim
import os

from points import Point

MOVE_SPEED = 13
WIDTH = 20
HEIGHT = 20
COLOR = "#888888"
#JUMP_POWER = 10
#GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.001  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/pacman_r.png' % ICON_DIR),
            ('%s/pacman.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/pacman_l.png' % ICON_DIR),
            ('%s/pacman.png' % ICON_DIR)]
ANIMATION_UP = [('%s/pacman_u.png' % ICON_DIR),
            ('%s/pacman.png' % ICON_DIR)]
ANIMATION_DOWN = [('%s/pacman_d.png' % ICON_DIR),
            ('%s/pacman.png' % ICON_DIR)]
ANIMATION_STAY = [('%s/pacman.png' % ICON_DIR, 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        boltAnim = []
        for anim in ANIMATION_UP:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimUP = pyganim.PygAnimation(boltAnim)
        self.boltAnimUP.play()
        boltAnim = []
        for anim in ANIMATION_DOWN:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimDOWN = pyganim.PygAnimation(boltAnim)
        self.boltAnimDOWN.play()
        boltAnim = []
        for anim in ANIMATION_STAY:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

    def update(self, left, right, up, down, platforms, ghost, points):
        self.xvel = self.yvel = 0
        #if up:
            #if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                #self.yvel = -JUMP_POWER
        self.image.fill(Color(COLOR))
        # self.boltAnimJump.blit(self.image, (0, 0))

        if up == down == left == right:
            self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            # self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            # self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))

        if up:
            self.yvel = -MOVE_SPEED  # Право = x + n
            self.boltAnimUP.blit(self.image, (0, 0))
        #     self.image.fill(Color(COLOR))
        #     self.boltAnimJumpRight.blit(self.image, (0, 0))
        # else:
        #     self.boltAnimRight.blit(self.image, (0, 0))

        if down:
            self.yvel = MOVE_SPEED  # Право = x + n
            self.boltAnimDOWN.blit(self.image, (0, 0))
            # self.image.fill(Color(COLOR))

        self.collide(0, self.yvel, platforms, ghost, points)

        self.rect.left += self.xvel  # переносим свои положение на xvel
        self.rect.top += self.yvel
        self.collide(self.xvel, self.yvel, platforms, ghost, points)

    def collide(self, xvel, yvel, platforms, ghost, points):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    # self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

                if isinstance(p, blocks.BlockTeleport):
                       self.teleporting(p.goX, p.goY)

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

