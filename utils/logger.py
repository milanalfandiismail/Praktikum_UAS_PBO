from abc import ABC, abstractmethod
from datetime import datetime

class ILogger(ABC):

    @abstractmethod
    def info(self, pesan: str) -> None:
        pass

    @abstractmethod
    def error(self, pesan: str) -> None:
        pass

class FileLogger(ILogger):

    def __init__(self, file: str):
        self.__file = file

    def info(self, pesan: str) -> None:
        self._write(f"[INFO] {pesan}")

    def error(self, pesan: str) -> None:
        self._write(f"[ERROR] {pesan}")

    def _write(self, pesan: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.__file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {pesan}\n")

class ConsoleLogger(ILogger):

    def info(self, pesan: str) -> None:
        print(f"[INFO] {pesan}")

    def error(self, pesan: str) -> None:
        print(f"[ERROR] {pesan}")

class MultiLogger(ILogger):

    def __init__(self, file_logger: FileLogger, console_logger: ConsoleLogger):
        self.__file_logger = file_logger
        self.__console_logger = console_logger

    def info(self, pesan: str) -> None:
        self.__file_logger.info(pesan)
        self.__console_logger.info(pesan)

    def error(self, pesan: str) -> None:
        self.__file_logger.error(pesan)
        self.__console_logger.error(pesan)