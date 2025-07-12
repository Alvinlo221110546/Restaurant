# Restaurant
# 🍽️ Restoran HOME FOOD – Aplikasi Pemesanan & Reservasi

**Restoran HOME FOOD** adalah aplikasi konsol berbasis Python yang memungkinkan pelanggan untuk:
- Melihat menu makanan
- Melakukan pemesanan
- Memproses pembayaran menggunakan berbagai metode
- Melakukan reservasi tempat
- Mendapatkan notifikasi pesanan

Proyek ini juga mengimplementasikan beberapa design pattern seperti **Observer**, **Strategy**, dan **Template Method**.

---

## ✨ Fitur Utama

- 📋 Menampilkan daftar menu
- ➕ Menambah dan menghapus item pesanan
- 💳 Pilihan pembayaran (Cash / Credit Card)
- 📢 Notifikasi ke pelanggan setelah pesanan diproses
- 📅 Reservasi tempat dengan validasi waktu
- 🧠 Menggunakan beberapa pola desain software (OOP)

---

## 🧱 Design Pattern yang Digunakan

| Pattern             | Deskripsi |
|---------------------|-----------|
| Observer            | Memberitahu pelanggan ketika pesanan telah diproses |
| Strategy            | Memilih metode pembayaran: Credit Card atau Cash |
| Template Method     | Memproses pesanan dengan langkah yang terstruktur (Display → Payment → Notifikasi) |

---

## 🛠️ Teknologi

- Bahasa: **Python 3.9+**
- Paradigma: **OOP dan Design Patterns**
- Tidak menggunakan pustaka eksternal

---

## 🚀 Cara Menjalankan

1. **Clone repositori:**

```bash
git clone https://github.com/username/home-food.git
cd home-food
Jalankan program:

bash
Copy
Edit
python home_food.py
