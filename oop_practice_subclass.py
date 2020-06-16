from oop_practice import Animal

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(diet = 'carnivore', n_limbs= '4')
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
         self.__name = new_name
         return new_name



