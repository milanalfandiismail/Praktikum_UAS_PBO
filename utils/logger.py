from abc import ABC, abstractmethod
from datetime import datetime

class ILogger(ABC):
    @abstractmethod
    def catat(self, pesan: str) -> None:
        pass

class FileLogger(ILogger):
    def __init__(self, file: str):
        self.__file = file

    def catat(self, pesan: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.__file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {pesan}\n")