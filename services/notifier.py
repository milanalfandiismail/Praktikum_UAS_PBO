from abc import ABC, abstractmethod
from models.peringatan import Peringatan
from utils.logger import ILogger

class IPemberitahu(ABC):
    @abstractmethod
    def kirim(self, peringatan: Peringatan) -> None:
        pass

class PemberitahuSMS(IPemberitahu):
    def __init__(self, nomor: str, logger: ILogger):
        self.__nomor = nomor
        self.__logger = logger

    def kirim(self, peringatan: Peringatan) -> None:
        pesan = f"[SMS ke {self.__nomor}] Peringatan: {peringatan.get_tingkat()}"
        self.__logger.catat(pesan)

class PemberitahuEmail(IPemberitahu):
    def __init__(self, email: str, logger: ILogger):
        self.__email = email
        self.__logger = logger

    def kirim(self, peringatan: Peringatan) -> None:
        pesan = f"[Email ke {self.__email}] Peringatan: {peringatan.get_tingkat()}"
        self.__logger.catat(pesan)