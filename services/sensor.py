from abc import ABC, abstractmethod
from models.data_gempa import DataGempa
from utils.logger import ILogger
import random

class Sensor(ABC):
    def __init__(self, nama: str, lokasi: str, logger: ILogger):
        self._nama = nama
        self._lokasi = lokasi
        self._logger = logger

    @abstractmethod
    def baca_data(self) -> DataGempa:
        pass

class SensorA(Sensor):
    def baca_data(self) -> DataGempa:
        magnitude = round(random.uniform(3.0, 7.5), 1)
        kedalaman = round(random.uniform(10.0, 100.0), 1)
        data = DataGempa(magnitude, self._lokasi, kedalaman)
        self._logger.catat(f"SensorA membaca data: M{magnitude}, {kedalaman} km")
        return data

class SensorB(Sensor):
    def baca_data(self) -> DataGempa:
        magnitude = round(random.uniform(2.5, 6.0), 1)
        kedalaman = round(random.uniform(5.0, 200.0), 1)
        data = DataGempa(magnitude, self._lokasi, kedalaman)
        self._logger.catat(f"SensorB membaca data: M{magnitude}, {kedalaman} km")
        return data