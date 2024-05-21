from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    @abstractmethod
    def greet(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.__name})"
