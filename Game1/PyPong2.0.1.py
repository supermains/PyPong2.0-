# PyPong2.0.1:1V1乒乓比赛(New)
# 作者：17好学生(QQ名), 邮箱：wen_zihao@qq.com
# 支持BSD开源协议,你们可以下载后更改代码
# 下载地址:
# PS:本版本会分成几个文件来写,更利于学习,记得全部下载!!!
# 本文件为主文件，下载后执行这个!

import pygame
from settings import Settings
from paddle import Paddle
from ball import Ball
import game

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen)
    myball = Ball([250, 250], screen)
    my_paddle = Paddle([270, 400])
    ai_paddle = Paddle([270, 100])
    ballgroup = pygame.sprite.Group(myball)
    pygame.display.set_caption("PyPong2.0.1")
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        screen.fill(settings.color)
        for event in pygame.event.get():
            game.game1(event, my_paddle)
        game.game2(ai_paddle, myball, my_paddle, ballgroup)
        game.game3(myball, settings)
        myball.move()
        game.game4(settings, screen, myball, my_paddle, ai_paddle)
        game.game5(settings, screen)

main()