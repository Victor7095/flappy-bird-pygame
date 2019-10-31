""" Flappy Bird """
import pygame


def main():
    """Main function"""
    pygame.init()
    logo = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Flappy Bird")
    screen = pygame.display.set_mode((640, 980))

    image = pygame.image.load("assets/static-bg.jpg")
    screen.blit(image, (0, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()


if __name__ == "__main__":
    main()
