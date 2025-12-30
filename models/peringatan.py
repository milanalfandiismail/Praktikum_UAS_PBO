from .data_gempa import DataGempa

class Peringatan:

    def __init__(self, data : DataGempa, tingkat: str):
        self.__data = data
        self.__tingkat = tingkat
        self.__pesan = ""

    def get_tingkat(self) -> str:
        return self.__tingkat

    def get_pesan(self) -> str:
        return self.__pesan

    def set_pesan(self, pesan: str) -> None:
        self.__pesan = pesan

    def get_data(self) -> DataGempa:
        return self.__data