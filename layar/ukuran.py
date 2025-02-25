import pygame

pygame.init()

# Membuat layar penuh
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Mendapatkan informasi layar
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

print(f"Lebar layar: {screen_width}, Tinggi layar: {screen_height}")

pygame.quit()
