from abc import ABC, abstractmethod
from models.data_gempa import DataGempa
from models.peringatan import Peringatan
from repositories.eq_repository import IEqRepository
from utils.logger import ILogger

class IAlertService(ABC):
    """Interface untuk layanan analisis dan peringatan gempa.

    Mendefinisikan kontrak untuk menganalisis data gempa dan menghasilkan peringatan.
    """

    @abstractmethod
    def analisa_dan_peringatkan(self, data: DataGempa) -> Peringatan:
        """Analisis data gempa dan hasilkan peringatan.

        Args:
            data (DataGempa): Data gempa yang akan dianalisis.

        Returns:
            Peringatan: Objek peringatan berdasarkan tingkat risiko.
        """
        pass

class SeismicAlertService(IAlertService):
    """Layanan untuk menganalisis risiko gempa dan membuat peringatan.

    Menggunakan repositori untuk menyimpan data dan logger untuk mencatat aktivitas.
    Logika penentuan tingkat risiko:
        - Ancaman Serius: magnitude >= 7.0 dan kedalaman <= 60 km
        - Bahaya : magnitude >= 6.0 dan kedalaman <= 300
        - Terasa: magnitude >= 5.0 
        - Tidak signifikan: selainnya
        - Data tidak valid : <= 0 atau kedalaman < 0
    """

    def __init__(self, repo: IEqRepository, logger: ILogger):
        """Inisialisasi layanan dengan dependensi eksternal.

        Args:
            repo (IEqRepository): Repositori untuk menyimpan data gempa.
            logger (ILogger): Utilitas untuk mencatat log aktivitas.
        """
        self.__repo = repo
        self.__logger = logger

    def _tentukan_tingkat(self, data: DataGempa) -> str:
        """Tentukan tingkat peringatan berdasarkan data gempa.

        Args:
            data (DataGempa): Data gempa yang akan dinilai.

        Returns:
            str: Salah satu dari "Tidak Signifikan", "Terasa", "Bahaya" atau "Ancaman Serius", "Data tidak valid".
        """
        magnitude = data.get_magnitude()
        kedalaman = data.get_kedalaman()
        if magnitude <= 0 or kedalaman < 0:
            return "Data tidak valid"

        if magnitude >= 7.0 and kedalaman <= 60:
            return "Ancaman Serius"

        elif magnitude >= 6.0 and kedalaman <= 300:
            return "Bahaya"

        elif magnitude >= 5.0:
            return "Terasa"

        else:
            return "Tidak signifikan"

    def analisa_dan_peringatkan(self, data: DataGempa) -> Peringatan:
        """Simpan data, analisis risiko, dan buat objek peringatan.

        Args:
            data (DataGempa): Data gempa dari sensor.

        Returns:
            Peringatan: Objek peringatan dengan tingkat yang sesuai.
        """
        self.__repo.simpan(data)
        tingkat = self._tentukan_tingkat(data)
        peringatan = Peringatan(data, tingkat)
        self.__logger.info(f"Analisis selesai: tingkat = {tingkat}")
        return peringatan