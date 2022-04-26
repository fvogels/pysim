from typing import Any
from abc import ABC, abstractmethod


class Settings(ABC):
    @abstractmethod
    def __getitem__(self, key : str) -> Any:
        ...

    @abstractmethod
    def __contains__(self, key : str) -> bool:
        ...


_settings = {
    'show_fps': False,
    'max_fps': 60,
}

def setting(key):
    return _settings[key]
