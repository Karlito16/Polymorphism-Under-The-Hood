from animal import Animal


class Dog(Animal):

    def __init__(self, name: str):
        super().__init__(name=name)

    def greet(self) -> str:
        return "Vau!"
