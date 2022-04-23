from pygame import Surface
from abc import ABC, abstractmethod


class Screen(ABC):
    @abstractmethod
    def update(self, elapsed_seconds : float) -> None:
        ...

    @abstractmethod
    def render(self, surface : Surface) -> None:
        ...
