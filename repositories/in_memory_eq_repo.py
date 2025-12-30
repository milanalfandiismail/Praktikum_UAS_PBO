from typing import List
from models.data_gempa import DataGempa
from .eq_repository import IEqRepository

class InMemoryEqRepository(IEqRepository):

    def __init__(self):
        self.__data_list = []

    def simpan(self, data: DataGempa) -> bool:
        self.__data_list.append(data)
        return True

    def ambil_semua(self) -> List[DataGempa]:
        return self.__data_list.copy()

    def ambil_terbaru(self) -> DataGempa:
        if not self.__data_list:
            raise ValueError("Tidak ada data gempa")
        return self.__data_list[-1]