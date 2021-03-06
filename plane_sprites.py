import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# 移动速度
MOVE_SPEED = 3


class GameSprite(pygame.sprite.Sprite):
    """Plane War Game Sprite"""

    def __init__(self, image_name, speed=2):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """Game Background Sprite"""

    def __init__(self, is_alt = False):

        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """Enemy Sprite"""

    def __init__(self):
        super().__init__("./images/enemy1.png")

        self.speed = random.randint(1, 3)

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width

        self.rect.x = random.randint(0, max_x)

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("enemy kill itslef")


class Hero(GameSprite):

    def __init__(self):
        super().__init__("./images/me1.png", 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 100

        self.bullets = pygame.sprite.Group()

    def update(self):

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print("firing...")

        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - 10
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)


class Bullet(GameSprite):
    """bullet sprite"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

