""" Flappy Bird """
import pygame as pg

screen, clock, background, ground, player = [None]*5
speed = 30
ground_x = ground_x2 = 0
running = False

SPRITES_DIR = "assets/images/"
AUDIO_DIR = "assets/audio/"


def redraw():
    """Redesenha a tela """
    screen.blit(background, (0, 0))
    screen.blit(ground, (ground_x, 790))
    screen.blit(ground, (ground_x2, 790))
    screen.blit(player, (100, 450))
    pg.display.update()


def main():
    """Main function"""
    global screen, background, clock, ground, ground_x, ground_x2, running, player
    pg.init()
    pg.display.set_caption("Flappy Bird")
    clock = pg.time.Clock()

    screen = pg.display.set_mode((640, 980))
    background = pg.image.load(SPRITES_DIR+"static-bg.jpg")

    ground = pg.transform.scale(pg.image.load(
        SPRITES_DIR+"ground.png"), (772, 224))
    ground_x = 0
    ground_x2 = ground.get_width()

    player = pg.transform.scale(pg.image.load(
        SPRITES_DIR+"redbird-midflap.png"), (102, 72))

    running = True
    while running:
        redraw()

        ground_x -= 8
        ground_x2 -= 8
        if ground_x < ground.get_width()*-1:
            ground_x = ground.get_width()
        if ground_x2 < ground.get_width()*-1:
            ground_x2 = ground.get_width()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(speed)


if __name__ == "__main__":
    main()
