from multiprocessing import Queue
from typing import TypeVar, Generic
from types import new_class


T = TypeVar('T')


class Channel(Generic[T]):
    __queue : Queue

    def __init__(self, queue : Queue):
        self.__queue = queue

    def send(self, message : T) -> None:
        self.__queue.put(message)

    def receive(self) -> T:
        return self.__queue.get(block=True, timeout=1)
