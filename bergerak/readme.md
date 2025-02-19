# 🎮 Game Menggerakkan Kotak dengan Pygame

Game sederhana menggunakan **Python** dan **Pygame** untuk menggerakkan kotak di layar menggunakan tombol **panah** pada keyboard.

## 📌 Fitur
✅ Menggunakan **Pygame** untuk rendering.  
✅ Kotak dapat bergerak ke **atas, bawah, kiri, dan kanan**.  
✅ **Dua versi**:  
  - **Tanpa `move_ip`** (menggunakan variabel `x, y`).  
  - **Dengan `move_ip`** (menggunakan `pygame.Rect`).  

## 🛠 Persyaratan
- Python 3.x
- Pygame (`pip install pygame`)

## 📂 Struktur Proyek
```
/game
├── game_basic.py   # Versi tanpa move_ip
├── game_move_ip.py # Versi dengan move_ip
└── README.md       # Dokumentasi
```

---

## 🕹 Versi 1: Menggerakkan Kotak **Tanpa `move_ip`**
### 🔹 Deskripsi
Versi ini menggerakkan kotak dengan mengubah koordinat `(x, y)` secara manual.

### 📜 Kode `game_basic.py`
```python
import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (30, 30, 30)
BOX_COLOR = (0, 255, 0)
BOX_SIZE = 50
x, y = (WIDTH - BOX_SIZE) // 2, (HEIGHT - BOX_SIZE) // 2
VELOCITY = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerakkan Kotak")

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= VELOCITY
    if keys[pygame.K_RIGHT] and x < WIDTH - BOX_SIZE:
        x += VELOCITY
    if keys[pygame.K_UP] and y > 0:
        y -= VELOCITY
    if keys[pygame.K_DOWN] and y < HEIGHT - BOX_SIZE:
        y += VELOCITY

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOX_COLOR, (x, y, BOX_SIZE, BOX_SIZE))
    pygame.display.update()

pygame.quit()
```

### 🏃 Cara Menjalankan
```sh
python game_basic.py
```

---

## 🕹 Versi 2: Menggerakkan Kotak **Dengan `move_ip`**
### 🔹 Deskripsi
Versi ini menggunakan metode `.move_ip()` dari **pygame.Rect** untuk pergerakan yang lebih efisien.

### 📜 Kode `game_move_ip.py`
```python
import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (30, 30, 30)
BOX_COLOR = (0, 255, 0)
BOX_SIZE = 50
VELOCITY = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerakkan Kotak dengan move_ip")

box = pygame.Rect((WIDTH - BOX_SIZE) // 2, (HEIGHT - BOX_SIZE) // 2, BOX_SIZE, BOX_SIZE)

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    box.move_ip(move_x, move_y)

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOX_COLOR, box)
    pygame.display.update()

pygame.quit()
```

### 🏃 Cara Menjalankan
```sh
python game_move_ip.py
```

---

## 📊 Perbandingan
| Versi             | Tanpa `move_ip` (`game_basic.py`) | Dengan `move_ip` (`game_move_ip.py`) |
|------------------|--------------------------------|---------------------------------|
| **Pergerakan**   | Mengubah koordinat `(x, y)` manual | Menggunakan `move_ip()` dari `pygame.Rect` |
| **Keunggulan**   | Lebih eksplisit dalam memahami logika pergerakan | Lebih sederhana dan efisien |
| **Kekurangan**   | Perlu lebih banyak variabel (`x, y`) | Perubahan berbasis `pygame.Rect`, kurang fleksibel |

---

## ⭐ Kesimpulan
- Gunakan **tanpa `move_ip`** jika ingin **memahami dasar pergerakan**.
- Gunakan **dengan `move_ip`** jika ingin kode yang **lebih simpel dan rapi**.

🚀 **Selamat bermain dan bereksperimen!** 🎮
