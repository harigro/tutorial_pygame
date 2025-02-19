import pygame

# Inisialisasi Pygame
pygame.init()

# Konstanta layar
WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (30, 30, 30)

# Warna dan ukuran kotak
BOX_COLOR = (0, 255, 0)
BOX_SIZE = 50
x, y = (WIDTH - BOX_SIZE) // 2, (HEIGHT - BOX_SIZE) // 2
VELOCITY = 5

# Buat layar game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerakkan Kotak")

# Loop utama
running = True
while running:
    pygame.time.delay(30)  # Tambahkan sedikit jeda untuk mengontrol kecepatan

    # Cek event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ambil input dari keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= VELOCITY
    if keys[pygame.K_RIGHT] and x < WIDTH - BOX_SIZE:
        x += VELOCITY
    if keys[pygame.K_UP] and y > 0:
        y -= VELOCITY
    if keys[pygame.K_DOWN] and y < HEIGHT - BOX_SIZE:
        y += VELOCITY

    # Gambar ulang layar
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOX_COLOR, (x, y, BOX_SIZE, BOX_SIZE))
    pygame.display.update()

# Keluar dari game
pygame.quit()
