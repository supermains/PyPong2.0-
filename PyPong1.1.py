# PyPong1.1:速战速决
# 作者：17好学生(QQ名), 邮箱：wen_zihao@qq.com
# 支持BSD开源协议,你们可以下载后更改代码
# 下载地址:https://github.com/2016haoxuesheng/PyPong2.0-/blob/PyPong2.0_VS/PyPong1.1.py

import pygame, sys


class MyBall(pygame.sprite.Sprite):

    def __init__(self, image_file, location, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = [10, 5]
        self.screen = screen

    def move(self):
        global score, score_surf, score_font, ji, ji_font, ji_surf
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speed[0] = -self.speed[0]

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            score = score + 1
            score_surf = score_font.render(str(score), 1, (0, 0, 0))
            if score % 10 == 0:
                ji = ji + 1
                ji_surf = ji_font.render(str(ji), 1, (0, 0, 0))
                self.speed[0] = self.speed[0] + 5
                self.speed[1] = self.speed[1] + 3


class MyPaddle(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface((100, 20))
        image_surface.fill((0, 0, 0))
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
myball = MyBall('wackyball.bmp', [50, 50], screen)
ballgruop = pygame.sprite.Group(myball)
paddle = MyPaddle((270, 400))
score = 0
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos = [10, 10]
ji = 1
ji_font = pygame.font.Font(None, 50)
ji_surf = ji_font.render(str(ji), 1, (0, 0, 0))
ji_pos = [330, 10]
lives = 5

done = False
while True:
    clock.tick(30)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballgruop, False):
        myball.speed[1] = -myball.speed[1]

    myball.move()

    if not done:
        screen.blit(myball.image, myball.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        screen.blit(ji_surf, ji_pos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myball.image, [width - 40 * i, 20])
        pygame.display.flip()

    if myball.rect.top >= screen.get_rect().bottom:
        lives = lives - 1

        if lives == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(score)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width() / 2 - \
                                   ft1_surf.get_width() / 2, 100])
            screen.blit(ft2_surf, [screen.get_width() / 2 - \
                                   ft2_surf.get_width() / 2, 200])
            pygame.display.flip()
            done = True

        else:
            pygame.time.delay(2000)
            myball.rect.topleft = [50, 50]
