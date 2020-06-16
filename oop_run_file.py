from oop_practice import *
from oop_practice_subclass import *

animal = Animal('carnivore', 4)
dog = Dog('Jack', 5)

print(animal.diet)
print(animal.n_limbs)
print(dog.age)
print(dog.get_name)
print(dog.set_name('Julie'))
print(dog.get_name)
julie = Dog('Julie', 10)
print(julie)
print(animal.loud_eater())
