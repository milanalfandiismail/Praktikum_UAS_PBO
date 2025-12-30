from .data_gempa import DataGempa

class Peringatan:
    """Representasi peringatan gempa berdasarkan analisis risiko.

    Merupakan data class yang menyimpan data gempa asli, tingkat peringatan,
    dan pesan opsional. Tidak mengandung logika bisnis.
    """

    def __init__(self, data : DataGempa, tingkat: str):
        """Inisialisasi objek Peringatan.

        Args:
            data (DataGempa): Objek data gempa yang menjadi dasar peringatan.
            tingkat (str): Tingkat peringatan ("Tidak Signifikan", "Terasa", "Bahaya" atau "Ancaman Serius").
        """
        self.__data = data
        self.__tingkat = tingkat
        self.__pesan = ""

    def get_tingkat(self) -> str:
        """Mengembalikan tingkat peringatan.

        Returns:
            str: Salah satu dari "Tidak Signifikan", "Terasa", "Bahaya" atau "Ancaman Serius".
        """
        return self.__tingkat

    def get_pesan(self) -> str:
        """Mengembalikan pesan kustom (jika ada).

        Returns:
            str: Pesan tambahan; default kosong.
        """
        return self.__pesan

    def set_pesan(self, pesan: str) -> None:
        """Menetapkan pesan kustom untuk peringatan.

        Args:
            pesan (str): Pesan yang ingin ditampilkan.
        """
        self.__pesan = pesan

    def get_data(self) -> DataGempa:
        """Mengembalikan data gempa asli.

        Returns:
            DataGempa: Objek data gempa yang terkait dengan peringatan ini.
        """
        return self.__data