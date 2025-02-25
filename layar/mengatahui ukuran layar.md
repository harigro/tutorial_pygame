### **Mengetahui Ukuran Layar dalam Mode Layar Penuh di Pygame**  

Saat mengembangkan game menggunakan `pygame`, sering kali kita perlu mengetahui ukuran layar, terutama saat menggunakan mode layar penuh (`FULLSCREEN`). Ini berguna untuk menyesuaikan elemen UI, posisi objek, atau bahkan mengatur resolusi yang optimal.  

Berikut adalah dua cara untuk mendapatkan ukuran layar saat mode layar penuh di `pygame`:  

---

### **1. Menggunakan `pygame.display.Info()`**  
Metode ini digunakan untuk mendapatkan informasi layar secara langsung dari sistem operasi, termasuk lebar dan tinggi layar.  

```python
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
```

#### **Penjelasan:**  
- `pygame.display.Info()` mengembalikan informasi layar yang sedang digunakan.  
- `info.current_w` memberikan lebar layar yang sebenarnya.  
- `info.current_h` memberikan tinggi layar yang sebenarnya.  

---

### **2. Menggunakan `pygame.display.get_surface()`**  
Metode ini digunakan untuk mendapatkan ukuran jendela `pygame` yang sedang digunakan, baik dalam mode layar penuh maupun jendela biasa.  

```python
import pygame

pygame.init()

# Membuat layar penuh
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Mendapatkan ukuran layar dari surface
screen_width, screen_height = screen.get_size()

print(f"Lebar layar: {screen_width}, Tinggi layar: {screen_height}")

pygame.quit()
```

#### **Penjelasan:**  
- `screen.get_size()` mengembalikan ukuran jendela yang dibuat oleh `pygame`.  
- Jika mode layar penuh aktif, ukuran ini akan sesuai dengan resolusi layar.  

---

### **Kapan Menggunakan yang Mana?**  
| Metode | Keterangan |
|--------|-----------|
| `pygame.display.Info()` | Memberikan ukuran layar fisik yang sesungguhnya. Cocok digunakan sebelum membuat tampilan `pygame`. |
| `screen.get_size()` | Memberikan ukuran jendela `pygame`, yang bisa berbeda jika mode tidak fullscreen. Cocok digunakan setelah jendela dibuat. |

Jika ingin mengetahui ukuran layar sebelum membuat jendela `pygame`, gunakan `pygame.display.Info()`. Namun, jika ingin mendapatkan ukuran layar setelah jendela dibuat, gunakan `screen.get_size()`.  

Dengan memahami perbedaan ini, kamu dapat lebih fleksibel dalam menangani tampilan layar dalam game yang sedang dikembangkan. 🚀