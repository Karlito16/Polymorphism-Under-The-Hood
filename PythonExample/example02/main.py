from cat import Cat
from dog import Dog
from animal import Animal


def animals_print_greeting(*animals: Animal):
    for animal in animals:
        print(f"{animal} greets: {animal.greet()}")


def main():
    cat: Cat = Cat(name="Mica Maca")
    dog: Dog = Dog(name="Peso")

    animals_print_greeting(cat, dog)

    cat.nope()


main()
