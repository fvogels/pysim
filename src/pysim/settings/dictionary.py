from typing import Any
from .settings import Settings


class DictionarySettings(Settings):
    def __init__(self):
        self.__table = {}

    def __getitem__(self, key : str) -> Any:
        return self.__table[key]

    def __contains__(self, key: str) -> bool:
        return key in self.__table
