import sys,os,getpass,time

while(1):
    print("您是否要注册账户？\n\t1(注册)2(不注册)3（退出）\n\t1 or 2 or 3")
    flog = input()
    if flog == str(1):
        print("开始注册")
        name = input("请输入你的用户名(注：用户名不能用‘3’)：")
        powerss = getpass.getpass("请输入你的密码：")
        print("注册成功！")
        break
    elif flog == str(2):
        print("再来一次，请输入1！！！")
        for daojishi in range(3,0,-1):
            print(daojishi)
            time.sleep(1)
        print("再问你最后一次！！")
        
    elif flog == str(3):
        print("再见")
        time.sleep(1)
        sys.exit()
    else:
            print("认真来好吗宝贝，选1啊")
            time.sleep(0.8)


while(1):
    print("开始登录")
    dl = input("用户名:")
    while(1):
        if dl == str(3):
            while(1):
                print("要退出吗 \n\t1（确定退出）2（按错了）")
                a = input()
                if a == str(1):
                    sys.exit()
                else:
                    print("别乱按宝贝")
                    dl = input("用户名:")
                    break
            else:
                break
        break
   
    if dl == str(88888888):
        print("亲爱的管理员，欢迎您！您一定是帅气的高威先生啦！")
        time.sleep(3.2)
        break
    mm = getpass.getpass("密码:")
    if dl == name:
        if(mm == powerss):
            print("登录成功！"+"游戏即将开始")
            time.sleep(1.5)
            break
        else:
                print("密码错误")
    else:
             print("用户名错误")




#引入
import pygame
from pygame.color import THECOLORS
#二维码类定义
class Ewm(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('zfb.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = [200,200]
#小球类定义
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    #动画函数     
    def move(self):
        global score, score_surf, score_font
        self.rect = self.rect.move(self.speed)
        #窗口两侧反弹
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            #小球撞到窗口两侧的声音
            if self.rect.top < screen.get_height():
                hit_wall.play()
        #小球碰到顶部窗口后，玩家得一分
        if self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
            score = score + 1
            score_surf = score_font.render(str(score), 1, THECOLORS['white'])
            #得分的声音
            get_point.play()
#小丑类定义            
class ClownClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('clownFace_right.png')
        self.rect = self.image.get_rect()
        self.rect.center = [40,460]
#初始化 
pygame.init()
pygame.mixer.init()
#加载音乐文件、设置音量
pygame.mixer.music.load('bgm.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
hit = pygame.mixer.Sound('hit_clown.wav')
hit.set_volume(0.4)
new_life = pygame.mixer.Sound('new_life.wav')
new_life.set_volume(0.5)
die = pygame.mixer.Sound('die.wav')
die.set_volume(0.6)
hit_wall = pygame.mixer.Sound('hit_wall.wav')
hit_wall.set_volume(0.2)
get_point = pygame.mixer.Sound('get_point.wav')
get_point.set_volume(0.2)
bye = pygame.mixer.Sound('game_over.wav')
bye.set_volume(0.6)
#设置窗口大小、游戏名称
screen = pygame.display.set_mode([600,500])
pygame.display.set_caption("GW's first game")
#创建Clock的实例颜色
clock = pygame.time.Clock()
#载入小球图片
myBall = MyBallClass('orangeBall.png', [10,5], [50, 50])
ballGroup = pygame.sprite.Group(myBall)
clown = ClownClass()
lives = 3
#创建分数变量
score = 0
#创建分数字体对象
score_font = pygame.font.SysFont('arial', 40)
#渲染文本到表面块Score_surf
score_surf = score_font.render(str(score), 1, THECOLORS['white'])
#文本的位置
score_pos = [10, 10]
done = False
#主循环
running = True
while running:
    clock.tick(30)
    screen.fill(THECOLORS['black'])
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        #如果鼠标移动，小丑就移动
        elif event.type == pygame.MOUSEMOTION:
            clown.rect.centerx = event.pos[0]
    #检查小丑是否碰到小球，若碰到，速度反向，并播放声音
    if pygame.sprite.spritecollide(clown, ballGroup, False):
        hit.play()
        myBall.speed[1] = -myBall.speed[1]
    myBall.move()
    #完全重绘屏幕
    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(clown.image, clown.rect)
        screen.blit(score_surf, score_pos)
        #记录玩家所剩下的机会
        for i in range (lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()
        #如果球碰到底边，就减少一次机会，并播放音乐
        if myBall.rect.top >= screen.get_rect().bottom:
            if not done:
                die.play()
            lives = lives - 1
            #当三次机会都用完时，游戏结束，显示玩家最后分数
            if lives <= 0:
                if not done:
                    pygame.time.delay(1000)
                    bye.play()
             
                final_text1 = "游戏结束"
                final_text2 = "您最后的分数是: " + str(score)
                ft1_font = pygame.font.Font('C:\Windows\Fonts\simhei.ttf',80)
                ft1_surf = ft1_font.render(final_text1, 1, THECOLORS['white'])
                ft2_font = pygame.font.Font('C:\Windows\Fonts\simkai.ttf',50)
                ft2_surf = ft2_font.render(final_text2, 1, THECOLORS['white'])
                #重绘屏幕
                screen.blit(ft1_surf, [screen.get_width()/2 - \
                                       ft1_surf.get_width()/2, 100])
                screen.blit(ft2_surf, [screen.get_width()/2 - \
                                       ft2_surf.get_width()/2, 200])
                pygame.display.flip()
                done = True
                pygame.mixer.music.fadeout(2000)
            #还有机会，小球重新 开始弹跳   
            else:
               pygame.time.delay(1000)
               new_life.play()
               myBall.rect.topleft = [50, 50]
               screen.blit(myBall.image, myBall.rect)
               pygame.display.flip()
               pygame.time.delay(1000)
pygame.quit()

