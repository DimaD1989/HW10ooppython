# 📌Доработаем задачи 5-6. Создайте класс-фабрику. ○Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# []
# 📌Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.
import random


class Animal:
    def __init__(self, name: str = None, breed: str = 'unknown', age: int = 0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'

    def __eq__(self, other):
        """__eq__(self, other) - поведения при =="""
        return self.name == other.name

    def __gt__(self, other):
        """"__gt__(self, other) - Определяет поведение оператора больше >"""
        return self.name > other.name

    def __lt__(self, other):
        """__lt__(self, other) - Определяет поведение оператора меньше <"""
        return self.name < other.name


class Predatory(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_flights: int = 0):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.count_flights = count_flights

    def print_specific(self):
        return f'Predatory: {self.name}'


class Primates(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', commands: list[str] = 'unknown'):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.commands = commands

    def print_specific(self):
        return f'Primates: {self.name}'


class Rodents(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_fins: int = 0):
        super().__init__(name, breed)
        # self.name = name
        # self.breed = breed
        self.count_fins = count_fins

    def print_specific(self):
        return f'Rodents: {self.name}'


class AnimalPlant:
    available_classes = [Primates, Predatory, Rodents]
    max_size = 0

    list_of_animals = []
    current_size = 0

    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size

    def create_animal(self, _class, *args, **kwargs):
        if self.current_size < self.max_size:
            if _class in self.available_classes:
                index = self.available_classes.index(_class)
                animal = self.available_classes[index](*args, **kwargs)
                self.list_of_animals.append(animal)
                self.current_size += 1

                return animal
            else:
                raise ValueError
        else:
            print("Лимит исчерпан")

    def __str__(self):
        res_list = ""
        for i in self.list_of_animals:
            res_list += i.print_specific() + "\n"
        return res_list

    def born(self, mother, father):

        if type(mother) == type(father):
            child_name = f"{mother.name[:len(mother.name) // 2]}{father.name[len(father.name) // 2:]}"

            child_breed = random.choice([mother.breed, father.breed])

            if type(mother) == Primates:
                child_commands = mother.commands.append(father.commands)
                self.create_animal(Primates, child_name, child_breed, child_commands)

            elif type(mother) == Predatory:
                child_count_flights = random.choice([mother.count_flights, father.count_flights])
                self.create_animal(Predatory, child_name, child_breed, child_count_flights)


            elif type(mother) == Rodents:
                child_count_fins = random.choice([mother.counts_flights, father.counts_flights])
                self.create_animal(Rodents, child_name, child_breed, child_count_fins)


        else:
            print("Так нельзя")

    def sort_animals(self):
        return self.list_of_animals.sort()


f = AnimalPlant("new", 10)
a = f.create_animal(Primates, 'Hulk', 'chimpanzee', ['YYYY', 'Run'])
b = f.create_animal(Predatory, 'Shark', 'Klach', 4)

c = f.create_animal(Predatory, 'Wolf', 'hare', 2)
d = f.create_animal(Rodents, 'Gopher', 'Cloun', 4)
e = f.born(b, c)

f.sort_animals()

print(type(a) == f.available_classes[0])

print(f)