import pygame

# inisialisai pygame
pygame.init()

# konstanta ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blur Effect Modal")

# warna
GREY = (200, 200, 200)
GREEN = (100, 200, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font
font = pygame.font.Font(None, 36)

# fungsi untuk membuat efek blur
def blur_surface(surface, scale_factor=0.2):
    """Menghasilkan efek blur dengan mengecilkan dan memperbesar kembali"""
    size = surface.get_size()
    small_size = (int(size[0] * scale_factor), int(size[1] * scale_factor))
    small_surface = pygame.transform.smoothscale(surface, small_size)
    return pygame.transform.smoothscale(small_surface, size)

# fungsi untuk menampilkan modal
def show_modal():
    # screenshot layar dan blur
    snapshot = screen.copy()
    blurred = blur_surface(snapshot)

    # tampilkan layar yang blur
    screen.blit(blurred, (0, 0))

    # gambar modal di atasnya
    modal_rect = pygame.Rect(200, 150, 400, 300)
    pygame.draw.rect(screen, WHITE, modal_rect, border_radius=10)

    # teks modal
    text = font.render("Ini adalah modal", True, BLACK)
    screen.blit(text, (modal_rect.x + 120, modal_rect.y + 130))

    pygame.display.flip()

# loop utama
running = True
showing_modal = False

while running:
    screen.fill(GREY) # latar belakang abu-abu
    pygame.draw.rect(screen, GREEN, (300, 200, 200, 150)) # kotak hijau
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m: # tekan m untuk menampilkan modal
                showing_modal = not showing_modal
                if showing_modal:
                    show_modal()
        
    if not showing_modal:
        pygame.display.flip()

pygame.quit()