from utils.logger import FileLogger
from repositories import InMemoryEqRepository
from services import SeismicAlertService, PemberitahuSMS, PemberitahuEmail, SensorA, SensorB

def main():
    # Inisialisasi logger
    logger = FileLogger("system.log")

    # Inisialisasi repository
    repo = InMemoryEqRepository()

    # Inisialisasi alert service
    alert_service = SeismicAlertService(repo, logger)

    # Inisialisasi notifiers
    sms_notifier = PemberitahuSMS("08123456789", logger)
    email_notifier = PemberitahuEmail("admin@enviro.id", logger)
    daftar_pemberitahu = [sms_notifier, email_notifier]

    # Inisialisasi sensor (contoh: pakai SensorA)
    sensor = SensorA("Sensor-A-Puncak", "Puncak, Jawa Barat", logger)

    # Simulasi jalankan sistem
    logger.catat("Sistem pemantauan gempa dimulai...")

    try:
        data_gempa = sensor.baca_data()
        peringatan = alert_service.analisa_dan_peringatkan(data_gempa)

        # Kirim peringatan ke semua pemberitahu
        for pemberitahu in daftar_pemberitahu:
            pemberitahu.kirim(peringatan)

        print(f"[INFO] Peringatan tingkat '{peringatan.get_tingkat()}' telah dikirim.")
        print(f"Magnitudo: {data_gempa.get_magnitude()}, Kedalaman: {data_gempa.get_kedalaman()} km")

    except Exception as e:
        logger.catat(f"Terjadi kesalahan: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()