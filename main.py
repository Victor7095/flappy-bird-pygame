""" Flappy Bird """
import pygame as pg
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE, K_UP
from random import randint

SPEED = 60
SPRITES_DIR = "assets/images/"
AUDIO_DIR = "assets/audio/"

pg.init()
pg.display.set_caption("Flappy Bird")
clock = pg.time.Clock()

screen = pg.display.set_mode((288, 512))

background = pg.image.load(
    SPRITES_DIR+"background-day.png").convert_alpha()
menu = pg.image.load(SPRITES_DIR+"message.png").convert_alpha()
ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()
pipe_sprite = pg.image.load(SPRITES_DIR+"pipe-green.png").convert_alpha()
pipe_sprite_inverted = pg.transform.flip(
    pg.image.load(SPRITES_DIR+"pipe-green.png").convert_alpha(), False, True)
birdSprite = [SPRITES_DIR+"redbird-upflap.png",
              SPRITES_DIR+"redbird-midflap.png",
              SPRITES_DIR+"redbird-downflap.png",
              SPRITES_DIR+"redbird-midflap.png"]
ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()

running = True


def redraw_menu():
    screen.blit(background, (0, 0))
    screen.blit(menu, ((background.get_width() - menu.get_width())/2,
                       (background.get_height() - menu.get_height())/2))
    pg.display.update()


def generate_pipe():
    pipe_height_key = randint(4, 9)
    pipe = {
        "upper": -pipe_height_key*30,
        "lower": -pipe_height_key*30+430,
        "x": background.get_width()}
    return pipe


def stop():
    global running
    running = False


def game_menu():
    while True:
        redraw_menu()
        for event in pg.event.get():

            # Sair ao clicar no X ou pressionar ESC
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key == K_ESCAPE):
                pg.quit()

            if event.type == KEYDOWN and (event.key == K_SPACE or
                                          event.key == K_UP):
                return

        clock.tick(SPEED)


def main_game():
    original_player = pg.image.load(
        SPRITES_DIR+"redbird-downflap.png").convert_alpha()
    player = original_player
    player_position = 60
    sprite = 0
    angle = 0
    x = 0
    y = 0
    y_speed = 0

    ground_x = 0
    ground_x2 = ground.get_width()

    pipes = [generate_pipe()]

    while True:
        # Redesenhando a tela
        screen.blit(background, (0, 0))
        for pipe in pipes:
            screen.blit(pipe_sprite_inverted, (pipe["x"], pipe["upper"]))
            screen.blit(pipe_sprite, (pipe["x"], pipe["lower"]))
        screen.blit(ground, (ground_x, 400))
        screen.blit(ground, (ground_x2, 400))
        screen.blit(player, (60, player_position))
        pg.display.update()

        x += 1
        y += 1
        player = pg.transform.rotate(original_player, angle)
        if y == 2:
            y = 0
            if y_speed >= -8:
                y_speed -= 1
                angle = (angle - 9) % 360
        player_position = player_position - y_speed

        # if x == 10 and playerIsAlive == True: (idle/ menu animation)
        if x == 5:
            original_player = pg.image.load(birdSprite[sprite])
            sprite = (sprite + 1) % len(birdSprite)
            x = 0

        # Movimentação do background
        ground_x -= 4
        ground_x2 -= 4
        if ground_x <= ground.get_width()*-1:
            ground_x = ground.get_width()
        if ground_x2 <= ground.get_width()*-1:
            ground_x2 = ground.get_width()

        # Movimentação dos tubos
        for pipe in pipes:
            pipe["x"] -= 3

        # Geração do próximo tubo
        if pipes[0]["x"] <= background.get_width()*-1:
            pipes.pop(0)
        if pipes[-1]["x"] == 108:
            pipes.append(generate_pipe())

        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    y_speed = 8
                    angle = 60

        clock.tick(SPEED)


while running:
    game_menu()
    main_game()
    clock.tick(SPEED)
