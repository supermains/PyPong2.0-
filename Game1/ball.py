# PyPong2.0.1:1V1乒乓比赛（急速模式）
# 作者：17好学生(QQ名), 邮箱：wen_zihao@qq.com
# 支持BSD开源协议,你们可以下载后更改代码
# 下载地址:https://github.com/2016haoxuesheng/PyPong2.0-/blob/PyPong2.0_VS/Game1/ball.py
# PS:本版本会分成几个文件来写,更利于学习,记得全部下载!!!
# 本文件为乒乓球定义文件,下载后无需执行!

from pygame.sprite import Sprite
import pygame

class Ball(Sprite):

    def __init__(self, location, screen):
        Sprite.__init__(self)
        self.image = pygame.image.load(r'images\wackyball.bmp')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = [10, 5]
        self.screen = screen

    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speed[0] = -self.speed[0]
