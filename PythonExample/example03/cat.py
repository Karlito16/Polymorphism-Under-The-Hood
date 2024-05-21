from animal import Animal


class Cat(Animal):

    def __init__(self, name: str):
        super().__init__(name=name)

    def greet(self) -> str:
        return "Mijau!"
