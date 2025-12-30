from .data_gempa import DataGempa

class Peringatan:
    def __init__(self, data: DataGempa):
        self.__data = data
        self.__tingkat = self._tentukan_tingkat()
        self.__pesan = ""

    def _tentukan_tingkat(self) -> str:
        magnitude = self.__data.get_magnitude()
        kedalaman = self.__data.get_kedalaman()
        if magnitude >= 6.5 and kedalaman < 30:
            return "Critical"
        elif magnitude >= 5.0 and kedalaman < 70:
            return "Warning"
        else:
            return "Normal"

    def get_tingkat(self) -> str:
        return self.__tingkat

    def get_pesan(self) -> str:
        return self.__pesan

    def set_pesan(self, pesan: str) -> None:
        self.__pesan = pesan

    def get_data(self) -> DataGempa:
        return self.__data