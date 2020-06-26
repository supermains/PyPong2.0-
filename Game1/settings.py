# PyPong2.0.1:1V1乒乓比赛（急速模式）
# 作者：17好学生(QQ名), 邮箱：wen_zihao@qq.com
# 支持BSD开源协议,你们可以下载后更改代码
# 下载地址:https://github.com/2016haoxuesheng/PyPong2.0-/blob/PyPong2.0_VS/Game1/settings.py
# PS:本版本会分成几个文件来写,更利于学习,记得全部下载!!!
# 本文件为配置文件，下载后无需执行!

import pygame

class Settings():

    def __init__(self):
        self.screen = (640, 480)
        self.color = (255, 255, 255)
        self.my_score = 0
        self.ai_score = 0
        self.my_font = pygame.font.Font(None, 50)
        self.ai_font = pygame.font.Font(None, 50)
        self.my_surf = self.my_font.render(str(self.my_score), 1, (0, 0, 0))
        self.ai_surf = self.ai_font.render(str(self.ai_score), 1, (0, 0, 0))
        self.my_pos = [255, 10]
        self.ai_pos = [375, 10]
        self.gang_font = pygame.font.Font(None, 50)
        self.gang_surf = self.gang_font.render("-", 1, (0, 0, 0))
        self.gang_pos = [325, 10]
        self.done = False
