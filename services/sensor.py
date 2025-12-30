from abc import ABC, abstractmethod
from models.data_gempa import DataGempa
from utils.logger import ILogger
import random

class Sensor(ABC):
    """Kelas abstrak untuk sensor gempa.

    Mendefinisikan kontrak umum untuk semua jenis sensor.
    """

    def __init__(self, nama: str, lokasi: str, logger: ILogger):
        """Inisialisasi sensor dasar.

        Args:
            nama (str): Nama unik sensor (misal: "Sensor-A").
            lokasi (str): Lokasi fisik sensor dipasang.
            logger (ILogger): Utilitas untuk mencatat aktivitas pembacaan.
        """
        self._nama = nama
        self._lokasi = lokasi
        self._logger = logger

    @abstractmethod
    def baca_data(self) -> DataGempa:
        """Baca data gempa dari sensor.

        Returns:
            DataGempa: Objek data gempa hasil pembacaan.
        """
        pass

class SensorA(Sensor):
    """Sensor simulasi tipe A dengan karakteristik tertentu.

    Menghasilkan data gempa acak dalam rentang:
        - Magnitude: 3.0 – 7.5
        - Kedalaman: 10.0 – 100.0 km
    """

    def baca_data(self) -> DataGempa:
        """Baca data gempa simulasi dari SensorA.

        Returns:
            DataGempa: Objek data gempa dengan nilai acak dalam rentang SensorA.
        """
        magnitude = round(random.uniform(3.0, 7.5), 1)
        kedalaman = round(random.uniform(10.0, 100.0), 1)
        data = DataGempa(magnitude, self._lokasi, kedalaman)
        self._logger.info(f"SensorA membaca gempa: Lokasi {self._lokasi}, Magnitude {magnitude}, Kedalaman {kedalaman} km")
        return data

class SensorB(Sensor):
    """Sensor simulasi tipe B dengan karakteristik berbeda.

    Menghasilkan data gempa acak dalam rentang:
        - Magnitude: 2.5 – 6.0
        - Kedalaman: 5.0 – 200.0 km
    """
    
    def baca_data(self) -> DataGempa:
        """Baca data gempa simulasi dari SensorB.

        Returns:
            DataGempa: Objek data gempa dengan nilai acak dalam rentang SensorB.
        """
        magnitude = round(random.uniform(2.5, 6.0), 1)
        kedalaman = round(random.uniform(5.0, 200.0), 1)
        data = DataGempa(magnitude, self._lokasi, kedalaman)
        self._logger.info(f"SensorB membaca gempa: Lokasi {self._lokasi}, Magnitude,  {magnitude}, Kedalaman {kedalaman} km")
        return data