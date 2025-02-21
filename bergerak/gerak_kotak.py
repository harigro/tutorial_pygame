import pygame

# Inisialisasi Pygame
pygame.init()

# Konstanta layar
WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (30, 30, 30)

# Warna dan ukuran kotak
BOX_COLOR = (0, 255, 0)
BOX_SIZE = 50
VELOCITY = 5

# FPS
FPS = 60
clock = pygame.time.Clock()

# rect
kotak = pygame.Rect((WIDTH - BOX_SIZE) // 2, (HEIGHT - BOX_SIZE) // 2, BOX_SIZE, BOX_SIZE)

# Buat layar game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerakkan Kotak")

def main():
    # Loop utama
    running = True
    while running:

        # Cek event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Ambil input dari keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and kotak.x > 0:
            kotak.move_ip(-VELOCITY, 0)
        if keys[pygame.K_RIGHT] and kotak.x < WIDTH - BOX_SIZE:
            kotak.move_ip(VELOCITY, 0)
        if keys[pygame.K_UP] and kotak.y > 0:
            kotak.move_ip(0, -VELOCITY)
        if keys[pygame.K_DOWN] and kotak.y < HEIGHT - BOX_SIZE:
            kotak.move_ip(0, VELOCITY)

        # Gambar ulang layar
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, BOX_COLOR, kotak)
        clock.tick(FPS)
        pygame.display.update()

    # Keluar dari game
    pygame.quit()

if __name__=="__main__":
    main()