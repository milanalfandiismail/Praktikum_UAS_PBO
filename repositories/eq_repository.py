from abc import ABC, abstractmethod
from typing import List
from models.data_gempa import DataGempa

class IEqRepository(ABC):
    """Interface untuk repositori data gempa.

    Mendefinisikan kontrak operasi penyimpanan dan pengambilan data gempa.
    Implementasi konkret harus mengikuti antarmuka ini.
    """

    @abstractmethod
    def simpan(self,  DataGempa) -> bool:
        """Simpan data gempa ke repositori.

        Args:
            data (DataGempa): Objek data gempa yang akan disimpan.

        Returns:
            bool: True jika berhasil disimpan, False jika gagal.
        """
        pass

    @abstractmethod
    def ambil_semua(self) -> List[DataGempa]:
        """Ambil semua data gempa yang pernah disimpan.

        Returns:
            List[DataGempa]: Daftar semua objek DataGempa dalam repositori.
        """
        pass

    @abstractmethod
    def ambil_terbaru(self) -> DataGempa:
        """Ambil data gempa terbaru berdasarkan waktu penyimpanan.

        Returns:
            DataGempa: Objek data gempa paling baru.

        Raises:
            ValueError: Jika repositori kosong.
        """
        pass