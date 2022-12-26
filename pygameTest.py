# pygame 製作
import sys
sys.path.append("modules")
import pygame
import random
import os
# 遊戲初始化，創建視窗
pygame.init()
pygame.mixer.init()

FPS = 120
WIDTH = 500
HEIGHT = 600

# 顏射(色)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("射擊遊戲__by羊劇(遊玩時就知道了)")
clock = pygame.time.Clock()

# 載入圖片
#bullet_img = pygame.image.load(os.path.join("img", "米洛斯.jpg")).convert()
bullet_img = pygame.image.load(os.path.join("img", "回復_陽具.jpg")).convert()
rock_img = pygame.image.load(os.path.join("img", "陽具_裁切2.jpg")).convert()
#player_img = pygame.image.load(os.path.join("img", "玩家角色_陽具.jpg")).convert()
player_img = pygame.image.load(os.path.join("img", "米洛斯_開頭畫面2.jpg")).convert()
power_img = {}
power_img['power'] = pygame.image.load(os.path.join("img", "威而鋼.jpg")).convert()
power_img['heal'] = pygame.image.load(os.path.join("img", "回復_陽具.jpg")).convert()
# 初始畫面的圖片.gif
first_img = pygame.image.load(os.path.join("img", "米洛斯.jpg")).convert()
# 載入背景音樂
#pygame.mixer.music.load(os.path.join("sound", "Aaron Smith-DancinRicardo Milos Song 米洛斯之歌(MEME).mp3"))
pygame.mixer.music.load(os.path.join("sound", "米洛斯.mp3"))
pygame.mixer.music.set_volume(0.2) # 音量調整 0 ~ 1
# 子彈撞到目標物的音效
hit_sound = pygame.mixer.Sound(os.path.join("sound", "Ahh.wav"))
player_hit_sound = pygame.mixer.Sound(os.path.join("sound", "Yamete Kudasai.wav"))

# arial 只支援英文
font_name = os.path.join("文字", "font.ttf")
# 顯示文字
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

# 玩家的血條(HP)
def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 120
    BAR_HEIGHT = 12
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

# 製造新目標物(補回來)
def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

# 顯示角色生命數
def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 75*i
        img_rect.y = y
        surf.blit(img, img_rect)

# 遊戲初始畫面
def draw_init():
    screen.blit(first_img, (0, 0))
    draw_text(screen, '射擊遊戲__by羊劇(遊玩時就知道了)', 30, WIDTH/2, HEIGHT/2)
    draw_text(screen, 'W,A,S,D 鍵移動角色 CTRL鍵,空白鍵射擊', 20, WIDTH/2, HEIGHT/4)
    draw_text(screen, '按 P 鍵開始遊戲', 25, WIDTH/2, HEIGHT/3)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    waiting = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(BLUE)
        self.image = pygame.transform.scale(player_img, (100, 50))
        self.rect = self.image.get_rect()
        self.radius = 45
        #pygame.draw.circle(self.image, YELLOW, self.rect.center, self.radius)
        self.rect.x = WIDTH / 2 - 2
        self.rect.y = HEIGHT
        self.speedx = 3
        self.speedy = 3
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_time > 1000:
            self.hidden = False
            self.rect.x = WIDTH / 2 - 2
            self.rect.y = HEIGHT
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_s]:
            self.rect.y += self.speedy
        if key_pressed[pygame.K_w]:
            self.rect.y -= self.speedy
        
        # x軸限制不跑出視窗
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        # y軸限制不跑出視窗
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        # y軸往上跑的限制
        if self.rect.top < 300:
            self.rect.top = 300
        
    def shoot(self):
        if not(self.hidden):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            '''
            if self.rect.left > WIDTH:
                self.rect.right = 0
            '''
        
    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.x = WIDTH / 2
        self.rect.y = 700

    def gun_LV(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image_ori = rock_img
        # self.image = self.image_ori.copy()
        # self.image = pygame.transform.scale(self.image_ori, (30, 60))
        # self.image = pygame.Surface((40, 40))
        # self.image.fill(GREEN)
        self.image = pygame.transform.scale(rock_img, (30, 60))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.9 / 2
        #pygame.draw.circle(self.image, YELLOW, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-2, 3)
        self.speedy = random.randrange(-3, 6)
        # self.total_degree = 0
        # self.rot_degree = 3

    # def rotate(self):
    #     self.total_degree += self.rot_degree
    #     self.total_degree = self.total_degree % 360
    #     self.image = pygame.transform.rotate(self.image_ori, self.rot_degree)
    #     center = self.rect.center()
    #     self.rect.center = center

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-2, 3)
            self.speedy = random.randrange(-3, 5)    
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (50, 100))
        # self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((10, 20))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = 4

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['heal', 'power'])
        self.image = pygame.transform.scale(power_img[self.type], (50, 100))
        # self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((10, 20))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powers = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    new_rock()

# 背景音樂
pygame.mixer.music.play(-1)

score = 0
running = True
# 遊戲迴圈
show_init = True
while running:
    if show_init:
        draw_init()
        show_init = False
        all_sprites = pygame.sprite.Group()
        rocks = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(20):
            r = Rock()
            all_sprites.add(r)
            rocks.add(r)
        score = 0
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL or event.key == pygame.K_SPACE:
                player.shoot()
            '''
            elif event.key == pygame.K_LCTRL:
                player.shoot()
            '''
    # 更新遊戲

    '''
    碰撞判斷
    '''
    # 羊具 與 子彈
    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        new_rock()
        hit_sound.play()
        score += hit.radius
        if random.random() > 0.1:
            power = Power(hit.rect.center)
            all_sprites.add(power)
            powers.add(power)
    
    # 羊具 與 玩家
    hits = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)
    for hit in hits:
        new_rock()
        player_hit_sound.play()
        player.health -= hit.radius
        if player.health <= 0:
            hit_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()
            if player.lives == 0:
                show_init = True

    # 道具 與 玩家
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        if hit == 'heal':
            player.health += 20
            if player.health >= 100:
                player.health = 100
        if hit == 'power':
            player.gun_LV()
        
    # 畫面顯示
    screen.fill(BLACK)    # fill(R, G, B)
    #first_back_img = pygame.transform.scale(first_img, (500, 500))
    screen.blit(first_img, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 20, WIDTH/2, 10)
    draw_health(screen, player.health, 5, 15)
    draw_lives(screen, player.lives, pygame.transform.scale(player_img, (60, 30)), WIDTH-210, 20)
    pygame.display.update()
    
pygame.quit()