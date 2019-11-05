""" Flappy Bird """
import pygame as pg
from random import randint

SPEED = 60
SPRITES_DIR = "assets/images/"
AUDIO_DIR = "assets/audio/"


def redraw():
    """Redesenha a tela """
    screen.blit(background, (0, 0))
    screen.blit(ground, (ground_x, 400))
    screen.blit(ground, (ground_x2, 400))
    screen.blit(player, (60, player_position))
    pg.display.update()


def generate_pipe():
    pipe_height_key = randint(4, 9)
    pipe = {
        "upper": -pipe_height_key*30,
        "lower": -pipe_height_key*30+430,
        "x": background.get_width()}
    return pipe


pg.init()
pg.display.set_caption("Flappy Bird")
clock = pg.time.Clock()

screen = pg.display.set_mode((288, 512))

background = pg.image.load(
    SPRITES_DIR+"background-day.png").convert_alpha()
player = pg.image.load(SPRITES_DIR+"redbird-midflap.png").convert_alpha()
birdSprite = [SPRITES_DIR+"redbird-upflap.png",
              SPRITES_DIR+"redbird-midflap.png",
              SPRITES_DIR+"redbird-downflap.png",
              SPRITES_DIR+"redbird-midflap.png"]
sprite = 0
x = 1
ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()

global y_speed, player_position
y_speed = 10
player_position = 60
ground_x = 0
ground_x2 = ground.get_width()

running = True
while running:
    redraw()

    x += 1
    if y_speed > -12:
        y_speed -= 1
        if y_speed == -12:
            y_speed = 10
    player_position = player_position - y_speed
    ground_x -= 4
    ground_x2 -= 4
    if ground_x <= ground.get_width()*-1:
        ground_x = ground.get_width()
    if ground_x2 <= ground.get_width()*-1:
        ground_x2 = ground.get_width()
    if x == 10:  # if x == 10 and playerIsAlive == True: (idle/ menu animation)
        player = pg.image.load(birdSprite[sprite])
        sprite = (sprite + 1) % len(birdSprite)
        x = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(SPEED)
