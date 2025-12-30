from abc import ABC, abstractmethod
from typing import List
from models.data_gempa import DataGempa

class IEqRepository(ABC):

    @abstractmethod
    def simpan(self,  DataGempa) -> bool:
        pass

    @abstractmethod
    def ambil_semua(self) -> List[DataGempa]:
        pass

    @abstractmethod
    def ambil_terbaru(self) -> DataGempa:
        pass