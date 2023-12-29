import pygame


if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 700
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
        picture1 = pygame.image.load("data/pole_one.png")
        picture2 = pygame.image.load("data/pole_two.png")
        screen.blit(picture1, (155, 50))
        screen.blit(picture2, (413, 55))
        pygame.display.flip()
    pygame.quit()