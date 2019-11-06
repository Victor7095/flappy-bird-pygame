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
menu_sp = pg.image.load(SPRITES_DIR+"message.png").convert_alpha()
game_over_sp = pg.image.load(SPRITES_DIR+"gameover.png").convert_alpha()
ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()
pipe_sprite = pg.image.load(SPRITES_DIR+"pipe-green.png").convert_alpha()
pipe_sprite_inverted = pg.transform.flip(
    pg.image.load(SPRITES_DIR+"pipe-green.png").convert_alpha(), False, True)
birdSprite = [SPRITES_DIR+"redbird-upflap.png",
              SPRITES_DIR+"redbird-midflap.png",
              SPRITES_DIR+"redbird-downflap.png",
              SPRITES_DIR+"redbird-midflap.png"]
ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()

ground_x = 0
ground_x2 = ground.get_width()

pipes = []

running = True


# Desenho do chão
def redraw_ground():
    screen.blit(ground, (ground_x, 400))
    screen.blit(ground, (ground_x2, 400))


# Desenho dos tubos
def redraw_pipes():
    for pipe in pipes:
        screen.blit(pipe_sprite_inverted, (pipe["x"], pipe["upper"]))
        screen.blit(pipe_sprite, (pipe["x"], pipe["lower"]))


def redraw_menu():
    screen.blit(background, (0, 0))
    screen.blit(menu_sp, ((background.get_width() - menu_sp.get_width())/2,
                          (background.get_height() - menu_sp.get_height())/2))


def redraw_game_over(player, player_position):
    screen.blit(background, (0, 0))
    redraw_pipes()
    screen.blit(game_over_sp,
                ((background.get_width() - menu_sp.get_width())/2,
                 (background.get_height() - menu_sp.get_height())/2))

    redraw_ground()
    screen.blit(player, (60, player_position))
    pg.display.update()


def generate_pipe():
    pipe_height_key = randint(4, 9)
    pipe = {
        "upper": -pipe_height_key*30,
        "lower": -pipe_height_key*30+430,
        "x": background.get_width()}
    return pipe


def move_ground():
    global ground_x, ground_x2
    ground_x -= 4
    ground_x2 -= 4
    if ground_x <= ground.get_width()*-1:
        ground_x = ground.get_width()
    if ground_x2 <= ground.get_width()*-1:
        ground_x2 = ground.get_width()


def stop():
    pg.quit()


def game_menu():
    while True:
        redraw_menu()
        redraw_ground()
        move_ground()
        pg.display.update()

        for event in pg.event.get():

            # Sair ao clicar no X ou pressionar ESC
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key == K_ESCAPE):
                stop()

            if event.type == KEYDOWN and (event.key == K_SPACE or
                                          event.key == K_UP):
                return

        clock.tick(SPEED)


def main_game():
    original_player = pg.image.load(
        SPRITES_DIR+"redbird-downflap.png").convert_alpha()
    player = original_player
    player_position = 60
    sprite = angle = timer1 = timer2 = y_speed = 0
    DidPlayerHitPipe = False

    pipes.clear()
    pipes.append(generate_pipe())

    while True:
        # Redesenhando a tela
        screen.blit(background, (0, 0))
        redraw_pipes()
        redraw_ground()
        screen.blit(player, (60, player_position))
        pg.display.update()

        timer1 += 1
        timer2 += 1

        # Animação de queda
        if timer2 == 2:
            timer2 = 0
            if y_speed >= -6:
                y_speed -= 1
                angle = (angle - 9) % 360
        if player_position <= 375:
            player_position = player_position - y_speed
        player = pg.transform.rotate(original_player, angle)

        # Tempo da animação de voo
        if timer1 == 5 and player_position <= 375:
            original_player = pg.image.load(birdSprite[sprite])
            sprite = (sprite + 1) % len(birdSprite)
            timer1 = 0

        # condição de morte pelos tubos
        for pipe in pipes:
            if 30 <= pipe["x"] <= 90 and (
                pipe["lower"] - 35 <= player_position or
                    pipe["upper"] + 310 >= player_position):
                DidPlayerHitPipe = True

        if not DidPlayerHitPipe:
            move_ground()

            # Movimentação dos tubos
            for pipe in pipes:
                pipe["x"] -= 4

        elif DidPlayerHitPipe and player_position >= 375:
            return (player, player_position)

        # Geração do próximo tubo
        if pipes[0]["x"] <= background.get_width()*-1:
            pipes.pop(0)
        if pipes[-1]["x"] == 108:
            pipes.append(generate_pipe())

        for event in pg.event.get():
            # Sair ao clicar no X ou pressionar ESC
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key == K_ESCAPE):
                stop()
            if event.type == pg.KEYDOWN:
                # insira aqui a condiçao de vida do passaro
                if(event.key == pg.K_SPACE and
                   0 < player_position < 375 and
                   not DidPlayerHitPipe):
                    y_speed = 7
                    angle = 60

        clock.tick(SPEED)


def game_over(player, player_position):
    while True:
        redraw_game_over(player, player_position)

        for event in pg.event.get():

            # Sair ao clicar no X ou pressionar ESC
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key == K_ESCAPE):
                stop()

            if event.type == KEYDOWN and (event.key == K_SPACE or
                                          event.key == K_UP):
                return

        clock.tick(SPEED)


while running:
    game_menu()
    [player, player_position] = main_game()
    game_over(player, player_position)
