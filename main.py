""" Flappy Bird """
import pygame as pg
from random import randint

SPEED = 60
SPRITES_DIR = "assets/images/"
AUDIO_DIR = "assets/audio/"


def redraw():
    """Redesenha a tela """
    screen.blit(background, (0, 0))
    for pipe in pipes:
        screen.blit(pipe_sprite_inverted, (pipe["x"], pipe["upper"]))
        screen.blit(pipe_sprite, (pipe["x"], pipe["lower"]))
    screen.blit(player, (60, 260))
    screen.blit(ground, (ground_x, 400))
    screen.blit(ground, (ground_x2, 400))
    pg.display.update()


def generate_pipe():
    pipe_height_key = randint(4, 8)
    pipe = {
        "upper": -pipe_height_key*20,
        "lower": -pipe_height_key*20+430,
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
              SPRITES_DIR+"redbird-downflap.png"]
sprite = 0
x = 1
ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()
pipe_sprite = pg.image.load(SPRITES_DIR+"pipe-green.png").convert_alpha()
pipe_sprite_inverted = pg.transform.flip(
    pg.image.load(SPRITES_DIR+"pipe-green.png").convert_alpha(), False, True)

ground_x = 0
ground_x2 = ground.get_width()
pipes = [generate_pipe()]

running = True
while running:
    redraw()
    x += 1
    ground_x -= 3
    ground_x2 -= 3
    if ground_x <= ground.get_width()*-1:
        ground_x = ground.get_width()
    if ground_x2 <= ground.get_width()*-1:
        ground_x2 = ground.get_width()
    if x == 10:
        player = pg.image.load(birdSprite[sprite])
        sprite = (sprite + 1) % len(birdSprite)
        x = 0

    for pipe in pipes:
        pipe["x"] -= 3

    if pipes[0]["x"] <= background.get_width()*-1:
        pipes.pop(0)
    if pipes[-1]["x"] == 108:
        pipes.append(generate_pipe())

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(SPEED)
