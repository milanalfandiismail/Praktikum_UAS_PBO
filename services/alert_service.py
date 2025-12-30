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

    def analisa_dan_peringatkan(self, data: DataGempa) -> Peringatan:
        self.__repo.simpan(data)
        peringatan = Peringatan(data)
        self.__logger.catat(f"Data gempa disimpan dan analisis: {peringatan.get_tingkat()}")
        return peringatan