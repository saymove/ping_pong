from pygame import *
window = display.set_mode((1100, 800))
display.set_caption("Пинг понг")
back = transform.scale(image.load('garazii.jpg'), (1100, 800))

mazl = transform.scale(image.load('mazzelov.png'), (320, 250))
sh = transform.scale(image.load('shkolnik.png'), (230, 250))
bolt = transform.scale(image.load('bolt.png'), (150, 150))
game = True


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
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<550:
            self.rect.y += self.speed

maz = Player('mazzelov.png', -30, 300, 320, 250, 10)

while game:
    window.blit(back, (0, 0)) 
    #window.blit(maz, (-30, 300)) 
    window.blit(sh, (820, 300))
    window.blit(bolt,(400, 400))
    for e in event.get():
        if e.type == QUIT:
            game = False
    maz.reset()
    maz.update()
    display.update()
time.delay(60)