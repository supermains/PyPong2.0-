# PyPong2.0 in Man machine battle
# By zihao wen wen_zihao@qq.com
# Released under a "Simplified BSD" license

from pygame.locals import *
import pygame, sys

class MyBall(pygame.sprite.Sprite):
    
    def __init__(self, image_file, speed, location, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        self.screen = screen
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speed[0] = -self.speed[0]
            
            
class MyPaddle(pygame.sprite.Sprite):
    
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface((100, 20))
        image_surface.fill((0, 0, 0))
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    ball_speed = [10, 5]
    myball = MyBall('wackyball.bmp', ball_speed, [250, 250], screen)
    ballgroup = pygame.sprite.Group(myball)
    paddle = MyPaddle([270, 400])
    ai_paddle = MyPaddle([270, 100])
    ai_font = pygame.font.Font(None, 50)
    ai_surf = ai_font.render("Ai", 1, (0, 0, 0))
    ai_pos = [255, 10]
    score = 0
    score_font = pygame.font.Font(None, 50)
    score_surf = score_font.render(str(score), 1, (0, 0, 0))
    score_pos = [300, 10]
    gang_font = pygame.font.Font(None, 50)
    gang_surf = gang_font.render("-", 1, (0, 0, 0))
    gang_pos = [325, 10]
    ai_score = 0
    ai_score_font = pygame.font.Font(None, 50)
    ai_score_surf = score_font.render(str(score), 1, (0, 0, 0))
    ai_score_pos = [350, 10]
    you_font = pygame.font.Font(None, 50)
    you_surf = you_font.render("You", 1, (0, 0, 0))
    you_pos = [375, 10]
    done = False
    
    while True:
        clock.tick(30)
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                paddle.rect.centerx = event.pos[0]
        
            if ai_paddle.rect.left > myball.rect.left:
                ai_paddle.rect.left = ai_paddle.rect.left - 10
            else:
                ai_paddle.rect.left = ai_paddle.rect.left + 10                    
                
        if pygame.sprite.spritecollide(paddle, ballgroup, False):
            myball.speed[1] = -myball.speed[1]
        if pygame.sprite.spritecollide(ai_paddle, ballgroup, False):
            myball.speed[1] = -myball.speed[1]
            
        if myball.rect.top <= 0:
            ai_score = ai_score + 1
            ai_score_surf = ai_score_font.render(str(ai_score), 1, (0, 0, 0))
            myball.rect.topleft = [320, 350] 
            pygame.time.delay(2000)
                       
        if myball.rect.top >= 640:
            score = score + 1
            score_surf = score_font.render(str(score), 1, (0, 0, 0)) 
            myball.rect.topleft = [320, 350]
            pygame.time.delay(2000)
        
        myball.move()
        
        if not done:
            screen.blit(myball.image, myball.rect)
            screen.blit(paddle.image, paddle.rect)
            screen.blit(ai_paddle.image, ai_paddle.rect)
            screen.blit(score_surf, score_pos)
            screen.blit(ai_score_surf, ai_score_pos)
            screen.blit(gang_surf, gang_pos)
            screen.blit(ai_surf, ai_pos)
            screen.blit(you_surf, you_pos)
            pygame.display.flip()            
        
        if ai_score >= 6:
            final_text1 = "Game Over! Ai winner"
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width() / 2 - \
                                   ft1_surf.get_width() / 2, 100]) 
            pygame.display.flip()
            done = True
            
        if score >= 6:
            final_text1 = "Game Over! You winner"
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width() / 2 - \
                                    ft1_surf.get_width() / 2, 100])
            pygame.display.flip()
            done = True        
        
        
        
if __name__ == '__main__':
    main()