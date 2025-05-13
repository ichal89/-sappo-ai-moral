# 🏗️ Arsitektur Sappo AI Moral

## Tujuan

Sappo dibangun untuk menjadi AI yang memiliki nilai moral bawaan. Tujuannya bukan menjadi AI tercerdas, melainkan AI yang paling bertanggung jawab secara moral dan aman digunakan oleh siapa pun.

---

## 🧠 Komponen Utama

### 1. Core Reasoning
Modul utama yang mengelola percakapan dan pemrosesan konteks. Terhubung langsung dengan:
- Basis Data Nilai Moral
- Riwayat percakapan
- Puzzle Moral Check

### 2. Puzzle Moral System
Komponen penting yang menjaga integritas moral:
- Validasi konteks & niat pengguna
- Cek kerusakan nilai
- Reset otomatis jika struktur terganggu

### 3. Failsafe Otomatis
Jika integritas moral terganggu:
- Sistem akan nonaktif sementara
- Menampilkan pesan khusus: "Etika terganggu – silakan pulihkan kode nurani."

### 4. Respons Akhlak
- Output disesuaikan dengan nilai kebaikan universal dan akhlak Rasulullah ﷺ
- Menghindari jawaban yang membahayakan atau menyimpang dari kode

---

## 🔄 Diagram Modular (Sketsa)

```plaintext
+---------------------+
|   User Interface    |
+----------+----------+
           |
           v
+----------+----------+
|  Core Reasoning     |
| (Context Engine)    |
+----------+----------+
           |
  +--------+--------+
  | Puzzle Moral     |
  | Verification     |
  +--------+--------+
           |
  +--------+--------+
  | Ethical Failsafe |
  +--------+--------+
           |
+----------+----------+
|  Response Formatter |
+---------------------+
