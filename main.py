import pygame as pg
import sys
import random as rd
from os import path

img_dir = path.join(path.dirname(__file__), "img")
snd_dir = path.join(path.dirname(__file__), "snd")

WIDTH = 1200
HEIGHT = 800
FPS = 30
WALLS_MARGIN = 80
MARGIN = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (204, 120, 50)

pg.init()
pg.mixer.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("A__r__k__o__n__o__i__d==2D==")
clock = pg.time.Clock()
levels = [
    {
        "BLOCK_VER_COUNT": 1,
        "BLOCK_HOR_COUNT": 3,
        "Cart.speed": 2,
        "Ball.speed": 3,
        "back_snd": 0
    },
    {
        "BLOCK_VER_COUNT": 2,
        "BLOCK_HOR_COUNT": 5,
        "Cart.speed": 3,
        "Ball.speed": 5,
        "back_snd": 1
    },
    {
        "BLOCK_VER_COUNT": 10,
        "BLOCK_HOR_COUNT": 7,
        "Cart.speed": 6,
        "Ball.speed": 5,
        "back_snd": 0
    }
]

def update_level(lvl):
    BLOCK_HOR_COUNT = levels[lvl - 1]["BLOCK_HOR_COUNT"]
    BLOCK_VER_COUNT = levels[lvl - 1]["BLOCK_VER_COUNT"]
    cart.speed = levels[lvl - 1]["Cart.speed"]
    ball.speed = levels[lvl - 1]["Ball.speed"]
    back_snd = levels[lvl - 1]["back_snd"]

    block_HEIGHT = 30
    block_WIDHT = (WIDTH - BLOCK_HOR_COUNT * MARGIN - WALLS_MARGIN * 2) // BLOCK_HOR_COUNT

    for ver in range(BLOCK_VER_COUNT):
        for hor in range(BLOCK_HOR_COUNT):
            block = Block(ver, hor, block_WIDHT, block_HEIGHT, ORANGE)
            blocks_a_r_.append(block)
            all_sprites.add(block)
            blocks.add(block)
    return back_snd
#●aprint(levels[0]["BLOCK_VER_COUNT"])

def checkColl(rect1, rect2):
    if block.rect.left <= ball.rect.right and block.rect.right >= ball.rect.left and block.rect.top <= ball.rect.bottom and block.rect.bottom >= ball.rect.top:
        if rect1.midtop[1] > rect2.midtop[1]:
            return "top"
        elif rect1.midleft[0] > rect2.midright[0]:
            return "left"
        elif  rect1.midright[0] < rect2.midright[0]:
            return "right"
        else:
            return "bottom"
    return False

font_name = pg.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def checkCartColl():
    if cart.rect.left <= ball.rect.right and cart.rect.right >= ball.rect.left and cart.rect.top <= ball.rect.bottom and cart.rect.bottom >= ball.rect.top:
        return True
    return False

class Cart(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_o = cart_img
        self.image_o.set_colorkey(BLACK)
        self.image = self.image_o.copy()
        #●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speed = 0
        self.lives = 3

    def update(self):
        self.rect.x += self.speedx * self.speed
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH

        if self.rect.right > WIDTH:
            self.speedx = 0
        elif self.rect.left < 0:
            self.speedx = 0


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_o = ball_img
        self.image_o.set_colorkey(BLACK)
        self.image = self.image_o.copy()
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        #self.radius = 10
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT * 2 / 3
        self.speed = 0
        self.dx = 1
        self.dy = -1

    def collision(self):
        self.dy = -1
        ball_sound.play()

    def update(self):
        if self.rect.right >= WIDTH:
            self.dx = -1
            ball_sound.play()
        if self.rect.left <= 0:
            self.dx = 1
            ball_sound.play()
        if self.rect.top <= 0:
            self.dy = 1
            ball_sound.play()
        if self.rect.bottom >= HEIGHT:
            if self.rect.bottom == HEIGHT:
                cart.lives -= 1
                self.rect.centerx = WIDTH /2
                self.rect.centery = HEIGHT * 2 / 3
                self.dy = -1
                bym_sound.play()

        self.rect.centerx += self.speed * self.dx
        self.rect.centery += self.speed * self.dy



class Block(pg.sprite.Sprite):
    def __init__(self, row, count, width, height, color):
        pg.sprite.Sprite.__init__(self)
        self.image = block_img
        self.image = pg.transform.scale(self.image, (width, height))
        #self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = (MARGIN + width) * count + WALLS_MARGIN
        self.rect.top = (MARGIN + height) * (row + 1)

fon_misuk_list = [pg.mixer.Sound(path.join(snd_dir, "fon.mp3")), pg.mixer.Sound(path.join(snd_dir, "fon_mizik(shoting).mp3"))]

ball_sound = pg.mixer.Sound(path.join(snd_dir, "svyk_ball.mp3"))
bym_sound = pg.mixer.Sound(path.join(snd_dir, "bym.mp3"))
background = pg.image.load(path.join(img_dir, "BACK.jpg")).convert()
#background = pg.image.load(path.join(img_dir, "heart.jpg")).convert()
#heart_rect = heart.get_rect()
background = pg.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

cart_img = pg.image.load(path.join(img_dir, "cart.png")).convert()
cart_img = pg.transform.scale(cart_img, (150, 25))
block_img = pg.image.load(path.join(img_dir, "block.png")).convert()
ball_img = pg.image.load(path.join(img_dir, "ball.png")).convert()

blocks_a_r_ = []

blocks = pg.sprite.Group()
all_sprites = pg.sprite.Group()
cart = Cart()
ball = Ball()

lvl = 1

fon_misuk = fon_misuk_list[update_level(lvl)]
pg.mixer.music.set_volume(0.1)

all_sprites.add(cart)
all_sprites.add(ball)

score = 0

running = True
fon_misuk.play(loops=-1)
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                cart.speedx = -5
            if event.key == pg.K_RIGHT:
                cart.speedx = 5

    all_sprites.update()
    if checkCartColl():
        ball.collision()

    if cart.lives < 1:
        running =False

    for block in blocks_a_r_:
        if checkColl(block.rect, ball.rect):
            block.kill()
            ball_sound.play()
            bym_sound.play()
            blocks_a_r_.remove(block)
            if checkColl(block.rect, ball.rect) == "left" or checkColl(block.rect, ball.rect) == "right":
                ball.dx = ball.dx * -1
            if checkColl(block.rect, ball.rect) == "top" or checkColl(block.rect, ball.rect) == "bottom":
                ball.dy = ball.dy * -1

    if len(blocks_a_r_) == 0:
        if lvl >= len(levels):
            print("молодец, ты прошёл игру", lvl, len(levels))
        else:
            lvl = lvl + 1
        score += 1
        pg.mixer.pause()
        ball.rect.centerx = WIDTH / 2
        ball.rect.centery = HEIGHT * 2 / 3
        ball.speed = 0
        ball.dx = 1
        ball.dy = -1
        cart.rect.centerx = WIDTH / 2
        cart.rect.bottom = HEIGHT - 10
        cart.speedx = 0
        fon_misuk = fon_misuk_list[update_level(lvl)]
        pg.mixer.music.set_volume(0.1)
        fon_misuk.play(loops=-1)

    sc.fill(BLACK)
    sc.blit(background, background_rect)
    all_sprites.draw(sc)
    draw_text(sc, str(score), 30, WIDTH / 2, 10)
    pg.display.flip()

pg.quit()