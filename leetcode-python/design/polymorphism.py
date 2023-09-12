# Polymorphism = Method Overriding, Method Overloading, Operator Overloading

# A) Method Overriding
# https://zetcode.com/lang/python/oop/
# In order to implement Polymorphism using method overriding,
# you can override the behaviour of a method in a sub-class.

# B) Method Overloading
# https://www.geeksforgeeks.org/python-method-overloading/
# In order to implement Polymorphism using method overloading,
# you need to write many methods with the same name and the
# same number of parameters but with different data types and
# implement different behavious in these methods.
# Now that is also polymorphism.

# C) Operator Overloading
# https://zetcode.com/lang/python/oop/
# Other ways to implement polymorphism is operator overloading and implementing interfaces.

class Computer:
    def __init__(self, storage_size: int, ram: int, ghz: float, cost: float):
        self.storage_size = storage_size
        self.ram = ram
        self.cpu_ghz = ghz
        self.cost = cost

    # A - Method Overriding
    def __len__(self):  # Operator overloading
        return self.storage_size

    # A - Method Overriding
    def __lt__(self, other):
        value_ratio = self.value_ratio()
        value_ratio_other = other.value_ratio()
        return value_ratio < value_ratio_other

    def value_ratio(self) -> float:
        return (self.storage_size + self.ram + self.cpu_ghz) / self.cost


# A - Method overriding
# https://zetcode.com/lang/python/oop/
class Laptop(Computer):
    def __init__(self, storage_size: int, ram: int, ghz: float, cost: float, weight: float):
        super().__init__(storage_size, ram, ghz, cost)
        self.weight = weight

    def value_ratio(self) -> float:  # Method overriding
        return (self.storage_size + self.ram + self.cpu_ghz) / (self.cost + self.weight)


# B - Method Overloading
# https://www.geeksforgeeks.org/python-method-overloading/
# https://github.com/mrocklin/multipledispatch
import multipledispatch


@multipledispatch.dispatch(int, int, int)
def addition(a, b, c) -> int:
    return a + b + c


@multipledispatch.dispatch(float, float, float)
def addition(a, b, c) -> float:
    return a + b + c


def test_method_overloading():
    print('\n')
    print(f"int values: {addition(1, 2, 3)}")
    print(f"float values: {addition(1.0, 2.0, 3.0)}")


def test_method_overriding_and_operator_overloading():
    my_laptop = Laptop(256, 16, 2.0, 1000, 2.2)
    my_desktop = Computer(256, 16, 2.0, 1000)

    my_computers = [my_desktop, my_laptop]
    my_computers.sort()

    print(f"\nsize of laptop: {len(my_laptop)}GB")
    print(f"Value ratio of laptop: {my_laptop.value_ratio()}")
    print(f"Value ratio of computer desktop: {my_desktop.value_ratio()}")

    for comp in my_computers:
        print(comp.value_ratio())
