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
GRAVITY = 1  # Efek gravitasi
JUMP_STRENGTH = 15  # Kekuatan lompatan
FLOOR_Y = HEIGHT - BOX_SIZE  # Posisi lantai

# FPS
FPS = 60
clock = pygame.time.Clock()

# Buat layar game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerakkan Kotak dengan Kelas")


class Box:
    """Kelas untuk merepresentasikan kotak yang bisa bergerak dan melompat."""

    def __init__(self, x, y, size):
        """Inisialisasi kotak dengan posisi, ukuran, dan atribut lainnya."""
        self.rect = pygame.Rect(x, y, size, size)
        self.velocity_y = 0
        self.on_ground = True

    def apply_gravity(self):
        """Menambahkan efek gravitasi ke kotak."""
        self.velocity_y += GRAVITY  # Tambahkan gravitasi ke kecepatan vertikal
        self.rect.y += self.velocity_y  # Gerakkan kotak ke bawah

        # Cegah kotak jatuh melewati lantai
        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.velocity_y = 0
            self.on_ground = True

    def jump(self):
        """Mengatur lompatan saat tombol spasi ditekan."""
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH  # Dorong ke atas
            self.on_ground = False

    def move(self, direction):
        """Menggerakkan kotak ke kiri atau kanan."""
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= VELOCITY
        elif direction == "right" and self.rect.right < WIDTH:
            self.rect.x += VELOCITY

    def draw(self, surface):
        """Menggambar kotak di layar."""
        pygame.draw.rect(surface, BOX_COLOR, self.rect)


def main():
    # Buat objek kotak
    box = Box((WIDTH - BOX_SIZE) // 2, FLOOR_Y, BOX_SIZE)

    # Loop utama
    running = True
    while running:

        # Cek event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Ambil input dari keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            box.move("left")
        if keys[pygame.K_RIGHT]:
            box.move("right")
        if keys[pygame.K_SPACE]:  # Panggil metode jump() jika tombol spasi ditekan
            box.jump()

        # Terapkan gravitasi
        box.apply_gravity()

        # Gambar ulang layar
        screen.fill(BACKGROUND_COLOR)
        box.draw(screen)
        clock.tick(FPS)
        pygame.display.update()

    # Keluar dari game
    pygame.quit()

if __name__=="__main__":
    main()