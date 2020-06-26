# PyPong2.0.1:1V1乒乓比赛(New)
# 作者：17好学生(QQ名), 邮箱：wen_zihao@qq.com
# 支持BSD开源协议,你们可以下载后更改代码
# 下载地址:
# PS:本版本会分成几个文件来写,更利于学习,记得全部下载!!!
# 本文件为游戏函数文件,下载后无需执行!

import pygame
import sys
from random import randint

def game1(event, my_paddle):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.MOUSEMOTION:
        my_paddle.rect.centerx = event.pos[0]


def game2(ai_paddle, myball, my_paddle, ballgroup):
    h = randint(1, 100)
    if ai_paddle.rect.left > myball.rect.left and ai_paddle.rect.left > 0 and h <= 92:
        ai_paddle.rect.left = ai_paddle.rect.left - randint(7, 13)
    elif ai_paddle.rect.left < myball.rect.left and ai_paddle.rect.left < 640:
        ai_paddle.rect.left = ai_paddle.rect.left + randint(7, 13)

    if pygame.sprite.spritecollide(my_paddle, ballgroup, False):
        myball.speed[1] = -randint((myball.speed[1] - 2), (myball.speed[1] + 2))
    if pygame.sprite.spritecollide(ai_paddle, ballgroup, False):
        myball.speed[1] = -randint((myball.speed[1] - 2), (myball.speed[1] + 2))

def game3(myball, settings):
    if myball.rect.top <= 0:
        settings.ai_score = settings.ai_score + 1
        settings.ai_surf = settings.ai_font.render(str(settings.ai_score), 1, (0, 0, 0))
        myball.rect.topleft = [320, 350]
        pygame.time.delay(2000)

    if myball.rect.top >= 640:
        settings.my_score = settings.my_score + 1
        settings.my_surf = settings.my_font.render(str(settings.my_score), 1, (0, 0, 0))
        myball.rect.topleft = [320, 350]
        pygame.time.delay(2000)

def game4(settings, screen, myball, my_paddle, ai_paddle):
    if not settings.done:
        screen.blit(myball.image, myball.rect)
        screen.blit(my_paddle.image, my_paddle.rect)
        screen.blit(ai_paddle.image, ai_paddle.rect)
        screen.blit(settings.my_surf, settings.my_pos)
        screen.blit(settings.ai_surf, settings.ai_pos)
        screen.blit(settings.gang_surf, settings.gang_pos)
        pygame.display.flip()

def game5(settings, screen):
    if settings.ai_score >= 6:
        final_text1 = "Game Over! Ai winner"
        ft1_font = pygame.font.Font(None, 70)
        ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
        screen.blit(ft1_surf, [screen.get_width() / 2 - \
                               ft1_surf.get_width() / 2, 100])
        pygame.display.flip()
        settings.done = True

    if settings.my_score >= 6:
        final_text1 = "Game Over! You winner"
        ft1_font = pygame.font.Font(None, 70)
        ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
        screen.blit(ft1_surf, [screen.get_width() / 2 - \
                               ft1_surf.get_width() / 2, 100])
        pygame.display.flip()
        settings.done = True
