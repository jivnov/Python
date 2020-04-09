#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

import blocks
import pyganim
import os
import random

random.seed()

from points import Point

MOVE_SPEED = 10
WIDTH = 20
HEIGHT = 20
COLOR = "#888888"
# JUMP_POWER = 10
# GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.001  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/ghost_o.png' % ICON_DIR),
                   # ('%s/pacman_r.png' % ICON_DIR),
                   # ('%s/pacman_r.png' % ICON_DIR),
                   # ('%s/pacman_r.png' % ICON_DIR),
                   ('%s/ghost_o.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/ghost_o.png' % ICON_DIR),
                  # ('%s/pacman_l.png' % ICON_DIR),
                  # ('%s/pacman_l.png' % ICON_DIR),
                  # ('%s/pacman_l.png' % ICON_DIR),
                  ('%s/ghost_o.png' % ICON_DIR)]
ANIMATION_UP = [('%s/ghost_o.png' % ICON_DIR),
                # ('%s/pacman_u.png' % ICON_DIR),
                # ('%s/pacman_u.png' % ICON_DIR),
                # ('%s/pacman_u.png' % ICON_DIR),
                ('%s/ghost_o.png' % ICON_DIR)]
ANIMATION_DOWN = [('%s/ghost_o.png' % ICON_DIR),
                  # ('%s/pacman_d.png' % ICON_DIR),
                  # ('%s/pacman_d.png' % ICON_DIR),
                  # ('%s/pacman_d.png' % ICON_DIR),
                  ('%s/ghost_o.png' % ICON_DIR)]
# ANIMATION_JUMP_LEFT = [('%s/pacman_l.png' % ICON_DIR, 0.1)]
# ANIMATION_JUMP_RIGHT = [('%s/pacman_r.png' % ICON_DIR, 0.1)]
# ANIMATION_JUMP = [('%s/pacman_l.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/ghost_o.png' % ICON_DIR, 0.1)]


class Ghost3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 20  # скорость вертикального перемещения
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
        # self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        # self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        # self.boltAnimJumpLeft.play()
        #
        # self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        # self.boltAnimJumpRight.play()
        #
        # self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        # self.boltAnimJump.play()

    def update(self, platforms):  # left1, right1, up1, down1, platforms):
        # self.xvel = self.yvel = 0
        # if up1:
        # if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
        # self.yvel = -JUMP_POWER
        self.image.fill(Color(COLOR))
        self.boltAnimLeft.blit(self.image, (0, 0))
        # self.boltAnimJump.blit(self.image, (0, 0))

        # if up1 == down1 == left1 == right1:
        #     self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим
        #
        # if left1:
        #     self.xvel = -MOVE_SPEED  # Лево = x- n
        #     # self.image.fill(Color(COLOR))
        #     self.boltAnimLeft.blit(self.image, (0, 0))
        #
        # if right1:
        #     self.xvel = MOVE_SPEED  # Право = x + n
        #     # self.image.fill(Color(COLOR))
        #     self.boltAnimRight.blit(self.image, (0, 0))
        #
        # if up1:
        #     self.yvel = -MOVE_SPEED  # Право = x + n
        #     self.boltAnimUP.blit(self.image, (0, 0))
        # #     self.image.fill(Color(COLOR))
        # #     self.boltAnimJumpright1.blit(self.image, (0, 0))
        # # else:
        # #     self.boltAnimright1.blit(self.image, (0, 0))
        #
        # if down1:
        #     self.yvel = MOVE_SPEED  # Право = x + n
        #     self.boltAnimDOWN.blit(self.image, (0, 0))
        #     # self.image.fill(Color(COLOR))

        # if not (left1 or right1):  # стоим, когда нет указаний идти
        #     self.xvel = 0
        # if not up1:
        #     self.image.fill(Color(COLOR))
        #     self.boltAnimStay.blit(self.image, (0, 0))

        # if not self.onGround:
        # self.yvel += GRAVITY

        # self.onGround = False;  # Мы не знаем, когда мы на земле((
        # self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.left += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.top += self.yvel
        self.collide(self.xvel, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
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

                n = random.randrange(4)
                if n == 0:
                    self.xvel = -MOVE_SPEED
                    self.yvel = 0
                    self.boltAnimLeft.blit(self.image, (0, 0))
                if n == 1:
                    self.xvel = MOVE_SPEED
                    self.yvel = 0
                    self.boltAnimLeft.blit(self.image, (0, 0))
                if n == 2:
                    self.yvel = -MOVE_SPEED
                    self.xvel = 0
                    self.boltAnimLeft.blit(self.image, (0, 0))
                if n == 3:
                    self.yvel = MOVE_SPEED
                    self.xvel = 0
                    self.boltAnimLeft.blit(self.image, (0, 0))

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

