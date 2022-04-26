from typing import Any
from abc import ABC, abstractmethod


class Settings(ABC):
    @abstractmethod
    def __getitem__(self, key : str) -> Any:
        ...

    @abstractmethod
    def __contains__(self, key : str) -> bool:
        ...
