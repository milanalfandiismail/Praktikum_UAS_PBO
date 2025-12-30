from datetime import datetime

class DataGempa:
    def __init__(self, magnitude: float, lokasi: str, kedalaman: float):
        self.__magnitude = magnitude
        self.__lokasi = lokasi
        self.__kedalaman = kedalaman
        self.__waktu = datetime.now()

    def get_magnitude(self) -> float:
        return self.__magnitude

    def get_kedalaman(self) -> float:
        return self.__kedalaman

    def get_lokasi(self) -> str:
        return self.__lokasi

    def get_waktu(self) -> datetime:
        return self.__waktu