import pygame

# Inisialisasi Pygame
pygame.init()

# Konstanta layar
WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (30, 30, 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Warna dan ukuran kotak
BOX_COLOR = (0, 255, 0)
BOX_SIZE = 50
FLOOR_Y = HEIGHT - BOX_SIZE  # Posisi lantai

# Fisika
VELOCITY = 5  # Kecepatan gerak horizontal
GRAVITY = 1   # Efek gravitasi
JUMP_STRENGTH = 20  # Kekuatan lompatan
MAX_JUMPS = 2  # Jumlah lompatan maksimal
FRICTION = 0.3  # Gesekan untuk memperhalus pergerakan

# FPS
FPS = 60
clock = pygame.time.Clock()


class Box:
    """Kelas untuk merepresentasikan kotak yang bisa bergerak, melompat, dan memiliki gesekan."""

    def __init__(self, x, y, size):
        """Inisialisasi kotak dengan posisi, ukuran, dan atribut lainnya."""
        self.rect = pygame.Rect(x, y, size, size)
        self.velocity_x = 0  # Kecepatan horizontal
        self.velocity_y = 0  # Kecepatan vertikal
        self.jump_count = 0  # Hitungan lompatan

    def apply_gravity(self):
        """Menambahkan efek gravitasi ke kotak."""
        self.velocity_y += GRAVITY  # Tambahkan gravitasi ke kecepatan vertikal
        self.rect.y += self.velocity_y  # Gerakkan kotak ke bawah

        # Cegah kotak jatuh melewati lantai
        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.velocity_y = 0
            self.jump_count = 0  # Reset lompatan saat menyentuh tanah

    def jump(self):
        """Mengatur lompatan dengan batas lompatan ganda."""
        if self.jump_count < MAX_JUMPS:
            self.velocity_y = -JUMP_STRENGTH  # Dorong ke atas
            self.jump_count += 1  # Tambah hitungan lompatan

    def move(self, direction):
        """Menggerakkan kotak ke kiri atau kanan dengan gesekan."""
        if direction == "left" and self.rect.left > 0:
            self.velocity_x = -VELOCITY
        elif direction == "right" and self.rect.right < WIDTH:
            self.velocity_x = VELOCITY

    def apply_friction(self):
        """Kurangi kecepatan horizontal jika tidak ada input (gesekan)."""
        if self.velocity_x > 0:
            self.velocity_x = max(0, self.velocity_x - FRICTION)  # Gesekan ke kanan
        elif self.velocity_x < 0:
            self.velocity_x = min(0, self.velocity_x + FRICTION)  # Gesekan ke kiri

        self.rect.x += self.velocity_x  # Terapkan pergerakan horizontal

    def draw(self, surface):
        """Menggambar kotak di layar."""
        pygame.draw.rect(surface, BOX_COLOR, self.rect)


def main():
    # Buat objek kotak
    box = Box((WIDTH - BOX_SIZE) // 2, FLOOR_Y, BOX_SIZE)

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
        if keys[pygame.K_LEFT]:
            box.move("left")
        if keys[pygame.K_RIGHT]:
            box.move("right")
        if keys[pygame.K_SPACE]:  # Panggil metode jump() jika tombol spasi ditekan
            box.jump()

        # Terapkan gravitasi dan gesekan
        box.apply_gravity()
        box.apply_friction()

        # Gambar ulang layar
        screen.fill(BACKGROUND_COLOR)
        box.draw(screen)
        clock.tick(30)
        pygame.display.update()

    # Keluar dari game
    pygame.quit()

if __name__=="__main__":
    main()