# Tutorial Pygame

Tutorial ini berisi panduan dasar untuk membuat game menggunakan Pygame, pustaka Python untuk pengembangan game 2D.

## 📌 Persyaratan

Sebelum memulai, pastikan kamu sudah menginstal Python dan Pygame. Jika belum, kamu bisa menginstalnya dengan perintah berikut:

```sh
pip install pygame
```

## 🎮 Memulai Proyek Pygame

1. Buat file Python baru, misalnya `main.py`.
2. Tambahkan kode dasar berikut untuk membuat jendela permainan:

```python
import pygame

# Inisialisasi Pygame
pygame.init()

# Konfigurasi layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertama dengan Pygame")

# Warna
WHITE = (255, 255, 255)

# Loop utama game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
```

## 🕹️ Menambahkan Elemen Dasar

- **Menggambar Bentuk** (lingkaran, kotak, dll.)
- **Menampilkan Gambar**
- **Menangani Input Pemain**
- **Menambahkan Suara & Musik**
- **Mengatur Fisika & Gerakan**

## 📚 Referensi

- [Dokumentasi Pygame](https://www.pygame.org/docs/)
- [Tutorial Pygame](https://www.pygame.org/wiki/tutorials)

💡 Silakan eksplorasi lebih lanjut dan mulai buat game pertamamu! 🚀