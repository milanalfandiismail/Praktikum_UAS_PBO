from utils.logger import FileLogger, ConsoleLogger, MultiLogger
from repositories import InMemoryEqRepository
from services import SeismicAlertService, PemberitahuSMS, PemberitahuEmail, SensorA, SensorB

def main():
    file_logger = FileLogger("system.log")
    console_logger = ConsoleLogger()
    logger = MultiLogger(file_logger, console_logger)

    logger.info("Sistem pemantauan gempa dimulai...")

    try:
        sensorA = SensorA("Sensor-A-Puncak", "", logger)
        repo = InMemoryEqRepository()
        alert_service = SeismicAlertService(repo, logger)

        sms_notifier = PemberitahuSMS("082152296778", logger)
        email_notifier = PemberitahuEmail("kelompok_1@umkt.ac.id", logger)
        daftar_pemberitahu = [sms_notifier, email_notifier]

        data_gempa_a = sensorA.baca_data()
      
        daftar_data = [data_gempa_a]

        daftar_peringatan = []
        for data in daftar_data:
            peringatan = alert_service.analisa_dan_peringatkan(data)
            daftar_peringatan.append(peringatan)

        for peringatan in daftar_peringatan:
            for pemberitahu in daftar_pemberitahu:
                pemberitahu.kirim(peringatan)

        # Log ringkasan
        logger.info("Proses selesai: semua data gempa telah dianalisis dan notifikasi dikirim.")

    except Exception as e:
        logger.error(f"Kesalahan sistem: {str(e)}")

if __name__ == "__main__":
    main()