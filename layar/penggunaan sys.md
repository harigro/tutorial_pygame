# Perbedaan Menggunakan Modul Sys.Exit Dan Tidak Sama Sekali
Berikut adalah dua contoh untuk menunjukkan perbedaan antara menggunakan `sys.exit()` dan tidak menggunakannya.  

---

### **1. Menggunakan `sys.exit()` (Keluar sepenuhnya)**
```python
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()  # Program benar-benar keluar di sini

if __name__ == "__main__":
    main()
    print("Program selesai.")  # Baris ini tidak akan dieksekusi karena sys.exit()
```
#### **Penjelasan:**
- Saat `sys.exit()` dipanggil, program langsung keluar.
- `print("Program selesai.")` tidak akan dieksekusi.

---

### **2. Tanpa `sys.exit()` (Program masih berjalan)**
```python
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()
    
    pygame.quit()
    print("Program selesai.")  # Baris ini tetap akan dieksekusi

if __name__ == "__main__":
    main()
    print("Kode setelah main() tetap berjalan.")  # Kode ini tetap dieksekusi
```
#### **Penjelasan:**
- Setelah `pygame.quit()`, program **tidak langsung keluar**.
- `print("Program selesai.")` dan kode setelah `main()` tetap dieksekusi.
- Jika dijalankan dalam **beberapa IDE atau terminal**, mungkin program tetap "berjalan" di latar belakang meskipun jendela `pygame` sudah tertutup.

---

### **Kesimpulan**
- **Gunakan `sys.exit()`** jika ingin memastikan program benar-benar keluar.
- **Tanpa `sys.exit()`**, program tetap bisa berjalan setelah `pygame.quit()`, terutama jika ada kode lain yang masih berjalan.

Jika ingin mematikan `pygame` tetapi tetap menjalankan kode lain setelahnya, gunakan tanpa `sys.exit()`. Jika ingin keluar sepenuhnya dari aplikasi, gunakan `sys.exit()`.