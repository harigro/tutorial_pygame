import pygame
import sys

def main():
    pygame.init()
    
    # Membuat layar penuh
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Warna latar belakang
    bg_color = (0, 0, 0)  # Hitam
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill(bg_color)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
