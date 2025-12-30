from datetime import datetime

class DataGempa:
    """Representasi data gempa bumi dengan enkapsulasi penuh dan validasi."""

    def __init__(self, magnitude: float, lokasi: str, kedalaman: float):
        """Inisialisasi dengan validasi awal."""
        self.set_magnitude(magnitude)
        self.set_lokasi(lokasi)
        self.set_kedalaman(kedalaman)
        self.__waktu = datetime.now()

    def get_magnitude(self) -> float:
        """Mengembalikan magnitude gempa."""
        return self.__magnitude

    def get_kedalaman(self) -> float:
        """Mengembalikan kedalaman gempa."""
        return self.__kedalaman

    def get_waktu(self) -> datetime:
        """Mengembalikan waktu kejadian (tidak bisa diubah)."""
        return self.__waktu

    def get_lokasi(self) -> str:
        """Mengembalikan lokasi gempa."""
        return self.__lokasi

    def set_lokasi(self, lokasi: str) -> None:
        """Menetapkan lokasi dengan validasi.

        Args:
            lokasi (str): Nama lokasi (tidak boleh kosong).

        Raises:
            ValueError: Jika lokasi kosong atau hanya spasi.
        """
        if not lokasi or not lokasi.strip():
            raise ValueError("Lokasi tidak boleh kosong")
        self.__lokasi = lokasi

    def set_kedalaman(self, kedalaman: float) -> None:
        """Menetapkan kedalaman dengan validasi.

        Args:
            kedalaman (float): Kedalaman dalam km (harus >= 0).

        Raises:
            ValueError: Jika kedalaman negatif.
        """
        if kedalaman < 0:
            raise ValueError("Kedalaman tidak boleh negatif")
        self.__kedalaman = kedalaman

    