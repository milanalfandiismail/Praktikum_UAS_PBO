from abc import ABC, abstractmethod
from models.data_gempa import DataGempa
from models.peringatan import Peringatan
from repositories.eq_repository import IEqRepository
from utils.logger import ILogger

class IAlertService(ABC):
    @abstractmethod
    def analisa_dan_peringatkan(self, data: DataGempa) -> Peringatan:
        pass

class SeismicAlertService(IAlertService):

    def __init__(self, repo: IEqRepository, logger: ILogger):
        self.__repo = repo
        self.__logger = logger

    def _tentukan_tingkat(self, data: DataGempa) -> str:
        magnitude = data.get_magnitude()
        kedalaman = data.get_kedalaman()
        if magnitude <= 0 or kedalaman < 0:
            return "Data tidak valid"

        if magnitude >= 7.0 and kedalaman <= 60:
            return "Ancaman Serius"

        # Berbahaya
        elif magnitude >= 6.0 and kedalaman <= 300:
            return "Bahaya"

        # Terasa
        elif magnitude >= 5.0:
            return "Terasa"

        # Normal
        else:
            return "Tidak signifikan"

    def analisa_dan_peringatkan(self, data: DataGempa) -> Peringatan:
        self.__repo.simpan(data)
        tingkat = self._tentukan_tingkat(data)
        peringatan = Peringatan(data, tingkat)
        self.__logger.info(f"Analisis selesai: tingkat = {tingkat}")
        return peringatan