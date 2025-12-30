from typing import List
from models.data_gempa import DataGempa
from .eq_repository import IEqRepository

class InMemoryEqRepository(IEqRepository):
    """Implementasi repositori data gempa menggunakan memori (list Python).

    Data hanya tersimpan selama program berjalan (tidak persisten).
    Digunakan untuk simulasi dan pengujian.
    """

    def __init__(self):
        """Inisialisasi repositori kosong."""
        self.__data_list = []

    def simpan(self, data: DataGempa) -> bool:
        """Simpan data gempa ke dalam daftar internal.

        Args:
            data (DataGempa): Objek data gempa yang akan disimpan.

        Returns:
            bool: Selalu mengembalikan True (simulasi sukses).
        """
        self.__data_list.append(data)
        return True

    def ambil_semua(self) -> List[DataGempa]:
        """Ambil salinan semua data gempa.

        Returns:
            List[DataGempa]: Salinan daftar semua data gempa.
        """
        return self.__data_list.copy()

    def ambil_terbaru(self) -> DataGempa:
        """Ambil data gempa terakhir yang disimpan.

        Returns:
            DataGempa: Data gempa paling baru.

        Raises:
            ValueError: Jika repositori kosong.
        """
        if not self.__data_list:
            raise ValueError("Tidak ada data gempa")
        return self.__data_list[-1]