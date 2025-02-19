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

# Buat layar game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerakkan Kotak dengan move_ip")

# Buat objek kotak sebagai Rect
box = pygame.Rect((WIDTH - BOX_SIZE) // 2, (HEIGHT - BOX_SIZE) // 2, BOX_SIZE, BOX_SIZE)
move_x, move_y = 0, 0

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
    move_x, move_y = 0, 0
    if keys[pygame.K_LEFT] and box.left > 0:
        move_x = -VELOCITY
    if keys[pygame.K_RIGHT] and box.right < WIDTH:
        move_x = VELOCITY
    if keys[pygame.K_UP] and box.top > 0:
        move_y = -VELOCITY
    if keys[pygame.K_DOWN] and box.bottom < HEIGHT:
        move_y = VELOCITY

    # Gerakkan kotak menggunakan move_ip
    box.move_ip(move_x, move_y)

    # Gambar ulang layar
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOX_COLOR, box)
    pygame.display.update()

# Keluar dari game
pygame.quit()
