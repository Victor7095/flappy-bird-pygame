""" Flappy Bird """
import pygame as pg

screen, clock, background, ground, player = [None]*5
SPEED = 60
ground_x = ground_x2 = 0
running = False

SPRITES_DIR = "assets/images/"
AUDIO_DIR = "assets/audio/"


def redraw():
    """Redesenha a tela """
    screen.blit(background, (0, 0))
    screen.blit(ground, (ground_x, 400))
    screen.blit(ground, (ground_x2, 400))
    screen.blit(player, (60, 260))
    pg.display.update()


def main():
    """Main function"""
    global screen, background, clock, ground, ground_x, ground_x2, running, player
    pg.init()
    pg.display.set_caption("Flappy Bird")
    clock = pg.time.Clock()

    screen = pg.display.set_mode((288, 512))

    background = pg.image.load(
        SPRITES_DIR+"background-day.png").convert_alpha()
    player = pg.image.load(SPRITES_DIR+"redbird-midflap.png").convert_alpha()
    ground = pg.image.load(SPRITES_DIR+"base.png").convert_alpha()

    ground_x = 0
    ground_x2 = ground.get_width()

    running = True
    while running:
        redraw()

        ground_x -= 4
        ground_x2 -= 4
        if ground_x < ground.get_width()*-1:
            ground_x = ground.get_width()
        if ground_x2 < ground.get_width()*-1:
            ground_x2 = ground.get_width()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(SPEED)


if __name__ == "__main__":
    main()
