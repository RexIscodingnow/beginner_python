# 模組導入，叫做 modules 的資料夾
# import pygame -> by modules folder
import sys as system  # 有另外開資料夾存放 pygame 模組，就使用，沒有的不用加上這兩行
system.path.append("modules")  # 從「叫什麼名稱的資料夾 (資料夾不是叫 modules 請更改成該存放資料夾名稱)」導入 pygame 模組
import pygame
import random
# 檔案導入 (by 圖片、音檔 一般來說...)
import os
# 遊戲初始化，遊戲功能設定一定要在遊戲初始化之後(往下)編寫，**否則無法執行** 喔~~~
pygame.init()

# 遊戲視窗的大小設定
WIDTH = 550
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 視窗的上方標題
pygame.display.set_caption("坦克大戰 battle city pygame_製作")
# 給 pygame.time.Clock() 的 tick() 函式執行
FPS = 120
clock = pygame.time.Clock()
# 檔案導入_*圖片*
# pygame.image.load(檔案路徑, 檔名.檔案格式).convert() -> convert() 轉成 pygame 容易載入的格式
# 我方坦克 & 雙方子彈 
gamer_tank = pygame.image.load(os.path.join("image", "玩家坦克.jpg")).convert()
tank_bullet = pygame.image.load(os.path.join("image", "子彈要使用的.jpg")).convert()
# 敵方坦克
simple_tank = pygame.image.load(os.path.join("image", "一般坦克.jpg")).convert()

# 顏色顯示
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# 關卡數，預設為 level: 1
level = []
level = 1
# 玩家的初始旋轉角度，預設為 0 度(朝上方 0 -> 轉左方 90 -> 下方 180 -> 右方 270 (度))
player_rotate = []
player_rotate = 0

# 子彈的初始旋轉角度
player_bullet_rotate = []
player_bullet_rotate = 0

# 敵方的初始旋轉角度
simple_tank_rotate = []
simple_tank_rotate = 0

# 敵方生成點
def oppsite_simple_tank():
    simple_tank_sprite = Other_Tank()
    all_sprites.add(simple_tank_sprite)
    other_tank.add(simple_tank_sprite)

# 玩家坦克的設定
class Player(pygame.sprite.Sprite):
    # *玩家*坦克*類別(class ...)*初始值設定，恩......~~~恩~~對!
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # pygame.transform.rotate(載入的圖片, 旋轉角度)
        # pygame.transform.scale(圖片檔案, (橫向, 縱向)) --> 修改圖片大小(放大/縮小) *單位: 「像素」*
        self.image = pygame.transform.rotate(pygame.transform.scale(gamer_tank, (45, 55)), player_rotate)
        # 取得圖片(玩家)座標位置
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - 40
        self.rect.y = HEIGHT
        self.player_rotate = player_rotate
        # 玩家移動速度
        self.speedx = 2
        self.speedy = 2
    
    # 更新資料，操控的部分
    def update(self):
        # 按下 __ 鍵，移動玩家坦克 (只能直線前進，不會突然斜線跑)
        key_pressed = pygame.key.get_pressed()
            # D 鍵，往右
        if key_pressed[pygame.K_d] == True and key_pressed[pygame.K_a] == False and key_pressed[pygame.K_s] == False and key_pressed[pygame.K_w] == False:
            player_rotate = 270
            self.image = pygame.transform.rotate(pygame.transform.scale(gamer_tank, (45, 55)), player_rotate)
            self.rect.x += self.speedx
            self.player_rotate = player_rotate
            # A 鍵，往左
        if key_pressed[pygame.K_a] == True and key_pressed[pygame.K_d] == False and key_pressed[pygame.K_s] == False and key_pressed[pygame.K_w] == False:
            player_rotate = 90
            self.image = pygame.transform.rotate(pygame.transform.scale(gamer_tank, (45, 55)), player_rotate)
            self.rect.x -= self.speedx
            self.player_rotate = player_rotate
            # S 鍵，往下
        if key_pressed[pygame.K_s] == True and key_pressed[pygame.K_w] == False and key_pressed[pygame.K_a] == False and key_pressed[pygame.K_d] == False:
            player_rotate = 180
            self.image = pygame.transform.rotate(pygame.transform.scale(gamer_tank, (45, 55)), player_rotate)
            self.rect.y += self.speedy
            self.player_rotate = player_rotate
            # W 鍵，往上
        if key_pressed[pygame.K_w] == True and key_pressed[pygame.K_s] == False and key_pressed[pygame.K_a] == False and key_pressed[pygame.K_d] == False:
            player_rotate = 0
            self.image = pygame.transform.rotate(pygame.transform.scale(gamer_tank, (45, 55)), player_rotate)
            self.rect.y -= self.speedy
            self.player_rotate = player_rotate

        # 限制玩家移動範圍，不跑出視窗外面(繼續跑~~)
        if self.rect.right > WIDTH:     # 左右兩邊
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:   # 上下兩邊
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    
    # 發射子彈的函式
    def shoot(self):
        if self.player_rotate == 0:
            bullet = Tank_Bullet_player(self.rect.centerx, self.rect.top, player_rotate=0)
        elif self.player_rotate == 180:
            bullet = Tank_Bullet_player(self.rect.centerx, self.rect.bottom, player_rotate=180)
        
        if self.player_rotate == 90:
            bullet = Tank_Bullet_player(self.rect.left, self.rect.centery+3, player_rotate=90)
        elif self.player_rotate == 270:
            bullet = Tank_Bullet_player(self.rect.right, self.rect.centery+3, player_rotate=270)

        all_sprites.add(bullet)
        shoot_bullets.add(bullet)

class Tank_Bullet_player(pygame.sprite.Sprite):
    # *玩家*子彈的*類別(class ...)*初始值設定，恩......~~~恩~~對!
    def __init__(self, x, y, player_rotate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.transform.scale(tank_bullet, (11, 15)), player_bullet_rotate)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.player_rotate = player_rotate
        self.speedx = 4
        self.speedy = 4
    # 更新資料
    def update(self):
        # 坦克轉哪個方向，子彈就轉哪(移動)
            # 向上
        if self.player_rotate == 0:
            player_bullet_rotate = 0
            self.image = pygame.transform.rotate(pygame.transform.scale(tank_bullet, (11, 15)), player_bullet_rotate)
            self.rect.y -= self.speedy
            # 向下
        elif self.player_rotate == 180:
            player_bullet_rotate = 180
            self.image = pygame.transform.rotate(pygame.transform.scale(tank_bullet, (11, 15)), player_bullet_rotate)
            self.rect.y += self.speedy
            # 向左
        if self.player_rotate == 90:
            player_bullet_rotate = 90
            self.image = pygame.transform.rotate(pygame.transform.scale(tank_bullet, (11, 15)), player_bullet_rotate)
            self.rect.x -= self.speedx
            # 向右
        elif self.player_rotate == 270:
            player_bullet_rotate = 270
            self.image = pygame.transform.rotate(pygame.transform.scale(tank_bullet, (11, 15)), player_bullet_rotate)
            self.rect.x += self.speedx
        # 刪除跑出視窗的子彈，沒有加上的話，出了視窗繼續跑喔~~(ㄏㄏ占用記憶體)
            # 往上
        if self.rect.bottom < 0:
            self.kill()
            # 往下
        elif self.rect.top > HEIGHT:
            self.kill()
            # 往左
        elif self.rect.right < 0:
            self.kill()
            # 往右
        elif self.rect.left > WIDTH:
            self.kill()

# 敵方坦克的設定
class Other_Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.transform.scale(simple_tank, (45, 55)), simple_tank_rotate)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = 2
        self.speedy = 2

    def update(self):
        flag = 0
        
        if self.rect.x <= 1 or self.rect.x == WIDTH and flag == 0:
            self.rect.y += self.speedy
            flag = 1

        if self.rect.y == 100 and flag == 1:
            self.image = pygame.transform.rotate(pygame.transform.scale(simple_tank, (45, 55)), 90)
            self.rect.x += self.speedx

        # 限制不跑出視窗
        if self.rect.right > WIDTH:     # 左右兩邊
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.bottom > HEIGHT:   # 上下兩邊
            self.rect.bottom = HEIGHT
        elif self.rect.top < 0:
            self.rect.top = 0

# 創建一個叫做 all_sprites 群組，集中在一起管理
all_sprites = pygame.sprite.Group()
# 玩家角色的群組
player = Player()
all_sprites.add(player)
# 創建*玩家*的子彈的 群組 (叫做 shoot_bullets)，管理*玩家*子彈的
shoot_bullets = pygame.sprite.Group()
# 創建*敵方*的子彈的 群組
other_tank = pygame.sprite.Group()

oppsite_simple_tank()

# 開啟直到 running = False，啊不就「關閉遊戲」停止迴圈
running = True
# 遊戲迴圈
while running:
    
    # 每一次 while 迴圈最多的次數，講簡單一點就是「遊戲偵數」
    clock.tick(FPS)
    # 1. 取得輸入 (按鍵)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # 2. 更新遊戲資料
    all_sprites.update()
    hits = pygame.sprite.groupcollide(shoot_bullets, other_tank, True, True)

    for hit in hits:
        oppsite_simple_tank()

    # 3. 畫面顯示
    # fill(R, G, B) 
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()