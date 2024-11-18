import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y))

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        random_x = 0
        random_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range (0, 16):
                pygame.draw.line(screen, "black", (0,i*32), (640,i*32))
            for i in range (0,20):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512))

            screen.blit(mole_image, mole_image.get_rect(topleft=(random_x, random_y)))

            if event.type == pygame.MOUSEBUTTONDOWN:
                (x,y)=pygame.mouse.get_pos()
                row = x//32
                col = y//32
                if row == random_x // 32 and col == random_y // 32:
                    random_x = random.randrange(0, 640, 32)
                    random_y = random.randrange(0, 512, 32)
                    screen.blit(mole_image, mole_image.get_rect(topleft=(random_x, random_y)))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
