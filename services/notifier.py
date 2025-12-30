from abc import ABC, abstractmethod
from models.peringatan import Peringatan
from utils.logger import ILogger

class IPemberitahu(ABC):
    """Interface untuk layanan pengiriman notifikasi.

    Mendefinisikan kontrak pengiriman peringatan melalui berbagai saluran.
    """

    @abstractmethod
    def kirim(self, peringatan: Peringatan) -> None:
        """Kirim peringatan melalui saluran tertentu.

        Args:
            peringatan (Peringatan): Objek peringatan yang akan dikirim.
        """
        pass

class PemberitahuSMS(IPemberitahu):
    """Pengirim notifikasi melalui SMS.

    Mensimulasikan pengiriman SMS ke nomor ponsel tertentu.
    """

    def __init__(self, nomor: str, logger: ILogger):
        """Inisialisasi pengirim SMS.

        Args:
            nomor (str): Nomor ponsel penerima (format string).
            logger (ILogger): Utilitas untuk mencatat aktivitas pengiriman.
        """
        self.__nomor = nomor
        self.__logger = logger

    def kirim(self, peringatan: Peringatan) -> None:
        """Kirim notifikasi SMS berisi tingkat peringatan.

        Args:
            peringatan (Peringatan): Objek peringatan yang akan dikirim.
        """
        pesan = f"[SMS ke {self.__nomor}] Peringatan Gempa: {peringatan.get_tingkat()}"
        self.__logger.info(pesan)

class PemberitahuEmail(IPemberitahu):
    """Pengirim notifikasi melalui email.

    Mensimulasikan pengiriman email ke alamat tertentu.
    """

    def __init__(self, email: str, logger: ILogger):
        """Inisialisasi pengirim email.

        Args:
            email (str): Alamat email penerima.
            logger (ILogger): Utilitas untuk mencatat aktivitas pengiriman.
        """
        self.__email = email
        self.__logger = logger

    def kirim(self, peringatan: Peringatan) -> None:
        """Kirim notifikasi email berisi tingkat peringatan.

        Args:
            peringatan (Peringatan): Objek peringatan yang akan dikirim.
        """
        pesan = f"[Email ke {self.__email}] Peringatan Gempa : {peringatan.get_tingkat()}"
        self.__logger.info(pesan)

class PemberitahuTelegram(IPemberitahu):
    """Pengirim notifikasi melalui telegram.

    Mensimulasikan pengiriman pesan telegram ke nomor tertentu.
    """

    def __init__(self, telegram: str, logger: ILogger):
        """Inisialisasi pengirim email.

        Args:
            telegram (str): Nomor telepon penerima.
            logger (ILogger): Utilitas untuk mencatat aktivitas pengiriman.
        """
        self.__telegram = telegram
        self.__logger = logger

    def kirim(self, peringatan: Peringatan) -> None:
        """Kirim notifikasi email berisi tingkat peringatan.

        Args:
            peringatan (Peringatan): Objek peringatan yang akan dikirim.
        """
        pesan = f"[Telegram ke {self.__telegram}] Peringatan Gempa : {peringatan.get_tingkat()}"
        self.__logger.info(pesan)