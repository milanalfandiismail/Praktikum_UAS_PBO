# Sistem Peringatan Dini Gempa – UAS 

Aplikasi simulasi sistem pemantauan gempa berbasis prinsip **SOLID** dan **OOP**.  
Mendeteksi gempa, menganalisis risiko, menyimpan data, dan mengirim notifikasi.

## Struktur data Proyek

UAS_Kelompok_1/
├── models/ # Entitas data: DataGempa, Peringatan
├── repositories/ # Penyimpanan data: InMemoryEqRepository
├── services/ # Logika bisnis: Sensor, Alert_Service, Notifier
├── utils/ # Utilitas: Logging (file & console)
├── system.log # Mencatat Informasi Yang Dikeluarkan Sistem
├── main.py # Entry point aplikasi
└── README.md


## Cara Menjalankan Sistem Radar
```bash
Pada file main.py jalankan sistem

Sistem akan melakukan:

Membaca data dari SensorA 

Menganalisis tingkat risiko:
Ancaman: Magnitudo ≥ 7.0 & kedalaman < 60 km
Bahaya: Magnitudo ≥ 6.0 & kedalaman < 300 km
Normal: Magnitudo ≥ 5.0 

Setelah menganalisis sistem akan
Mengirim notifikasi simulasi ke SMS & Email

Mencatat aktivitas ke:
Terminal (console)
File: system.log

---
