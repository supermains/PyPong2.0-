# PyPong2.0.1:1V1乒乓比赛（急速模式）
# 作者：17好学生(QQ名), 邮箱：wen_zihao@qq.com
# 支持BSD开源协议,你们可以下载后更改代码
# 下载地址:https://github.com/2016haoxuesheng/PyPong2.0-/edit/PyPong2.0_VS/Game1/paddle.py
# PS:本版本会分成几个文件来写,更利于学习,记得全部下载!!!
# 本文件为球拍定义文件,下载后无需执行!

import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):

    def __init__(self, location):
        Sprite.__init__(self)
        image_surface = pygame.surface.Surface((100, 20))
        image_surface.fill((0, 0, 0))
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
