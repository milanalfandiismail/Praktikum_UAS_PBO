from datetime import datetime

class DataGempa:
    def __init__(self, magnitude: float, lokasi: str, kedalaman: float):
        self.set_magnitude(magnitude)
        self.set_lokasi(lokasi)
        self.set_kedalaman(kedalaman)
        self.__waktu = datetime.now()

    def get_magnitude(self) -> float:
        return self.__magnitude

    def get_kedalaman(self) -> float:
        return self.__kedalaman

    def get_lokasi(self) -> str:
        return self.__lokasi

    def set_lokasi(self, lokasi: str) -> None:
        if not lokasi or not lokasi.strip():
            raise ValueError("Lokasi tidak boleh kosong")
        self.__lokasi = lokasi
        

    def get_waktu(self) -> datetime:
        return self.__waktu