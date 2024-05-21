from typing import Optional

from cat import Cat
from dog import Dog
from animal import Animal


class ValueWrapper:
    value: Optional[object] = None


def execute_object_method_rec(clazz, self, method_name):
    if clazz.__dict__.get(method_name):
        ValueWrapper.value = clazz.__dict__.get(method_name)(self)
        return True

    bases = clazz.__bases__

    for base in bases:
        if execute_object_method_rec(clazz=base, self=self, method_name=method_name):
            return True

    return False


def execute_object_method(obj, method_name):
    if execute_object_method_rec(clazz=obj.__class__, self=obj, method_name=method_name):
        return ValueWrapper.value
    raise AttributeError(f"'{obj.__class__.__name__}' object has no attribute '{method_name}'")


def animals_print_greeting(*animals: Animal):
    for animal in animals:
        print(
            f"{execute_object_method(obj=animal, method_name='__str__')} greets: "
            f"{execute_object_method(obj=animal, method_name='greet')}"
        )


def main():
    cat: Cat = Cat(name="Mica Maca")
    dog: Dog = Dog(name="Peso")

    animals_print_greeting(cat, dog)

    execute_object_method(obj=cat, method_name="nope")


main()
