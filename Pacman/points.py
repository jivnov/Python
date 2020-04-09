from pygame import *
import os

POINT_WIDTH = 8
POINT_HEIGHT = 8
POINT_COLOR = "#FFFF00"
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами

class Point(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((POINT_WIDTH, POINT_HEIGHT))
        self.image.fill(Color(POINT_COLOR))
        self.image = image.load("%s/POINT.png" % ICON_DIR)
        self.image.set_colorkey(Color(POINT_COLOR))
        self.rect = Rect(x, y, POINT_WIDTH, POINT_HEIGHT)