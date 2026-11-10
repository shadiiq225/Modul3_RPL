# Aplikasi Perpustakaan - Sistem Informasi MVC Python

## 1. Deskripsi Singkat Aplikasi
Aplikasi Perpustakaan adalah perangkat lunak berbasis desktop yang dikembangkan menggunakan bahasa pemrograman Python dengan menerapkan pola arsitektur **Model-View-Controller (MVC)**. Antarmuka grafis (GUI) dibangun menggunakan pustaka `customtkinter`, sementara manajemen basis data menggunakan MySQL.

## 2. Struktur Direktori MVC
Struktur direktori proyek ini dirancang terpisah secara modular:
- `config/`: Berisi konfigurasi koneksi ke basis data MySQL.
- `controllers/`: Berisi logika pengendali (*controller*) yang menjembatani interaksi antara View dan Model.
- `models/`: Berisi logika pengolahan data dan kueri basis data.
- `views/`: Berisi komponen antarmuka grafis (GUI).
- `tests/`: Berisi skrip pengujian unit (*unit testing*) menggunakan `pytest`.
- `.github/workflows/`: Berisi konfigurasi otomatisasi CI/CD GitHub Actions.

## 3. Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan Anda telah menginstal **Python 3.x** dan **Laragon** (untuk MySQL).
2. Buat database baru di MySQL (misalnya: `db_perpustakaan`).
3. Clone repositori ini ke komputer lokal Anda.
4. Buat dan aktifkan *virtual environment*:
   ```bash
   python -m venv env
   env\Scripts\activate     # Untuk Windows