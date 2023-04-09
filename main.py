from pygame import *

window = display.set_mode((1500, 800))
display.set_caption("Пинг понг")
back = transform.scale(image.load('ggg.jpg'), (1500, 800))
clock = time.Clock()

mazl = transform.scale(image.load('mazzelov.png'), (320, 280))
sho = transform.scale(image.load('shcolnik.png'), (320, 280))
bolt = transform.scale(image.load('bolt.png'), (150, 150))
game = True

speed_x = 5
speed_y = 5

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>-10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<520:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>-30:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<520:
            self.rect.y += self.speed

maz = Player('mazzelov.png', -50, 300, 320, 280, 10)
sh = Player2('shcolnik.png', 1210, 260, 320, 280, 10)
bol = GameSprite('bolt.png', 675, 400, 150, 150, 5)

font.init()
font2 = font.SysFont('Times New Roman', 48)

lose1 = font2.render('Левый лох!', True, (180, 0, 0))
lose2 = font2.render('Правый лох!', True, (180, 0, 0))

finish = False

while game:
    window.blit(back, (0, 0)) 
    #window.blit(bolt,(675, 400))
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        bol.rect.x += speed_x
        bol.rect.y += speed_y

        if sprite.collide_rect(maz, bol) or sprite.collide_rect(sh, bol):
            speed_x *= -1
            speed_y *= 1
        
        if bol.rect.y > 650 or bol.rect.y < 0:
            speed_y *= -1

        if bol.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if bol.rect.x > 1350:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        maz.reset()
        maz.update()
        sh.reset()
        sh.update()
        bol.reset()
        display.update()
clock.tick(360)
