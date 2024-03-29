# 1.
# class Account:
#     def __init__(self, balance) -> None:
#         self.balance = balance
    
#     def dep(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f'Вы пополнили баланс на {amount}'
#         else:
#             return 'Сумма должна быть положительной'
    
#     def get_money(self, amount):
#         if amount <= 0:
#             return 'Сумма должна быть положительной'
#         elif amount <= self.balance:
#             self.balance -= amount
#             return f'Вы сняли {amount}'
#         else:
#             return 'Недостаточно средств'
    
#     def money(self):
#         return self.balance

# account = Account(1488)
# print(account.dep(500))  
# print(account.get_money(100))  
# print(account.money())  

# 2.
# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return 'Гав'
# class Cat(Animal):
#     def speak(self):
#         return 'Mяу'

# dog = Dog()
# cat = Cat()

# print(f'Собака говорит: {dog.speak()}')
# print(f'Кошка говорит: {cat.speak()}')

# 3.
# from math import pi
# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,a,b) -> None:
#         self.a = a
#         self.b = b
#     def area(self):
#         return self.a * self.b

# class Circle(Shape):
#     def __init__(self,radius) -> None:
#         self.radius = radius
#     def area(self):
#         return pi * self.radius**2   
     
# rectangle = Rectangle(2,3)
# print(f'Площадь прямоугольника: {rectangle.area()} см в кв')


# 4.
# class Furniture:
#     def __init__(self, name):
#         self.name = name

# class Bed(Furniture):
#     pass

# class Sofa(Furniture):
#     pass

# class Table(Furniture):
#     pass

# class Room:
#     def __init__(self):
#         self.furniture = []

#     def add(self, furniture):
#         self.furniture.append(furniture)

# bed = Bed("Кровать")
# sofa = Sofa("Диван")
# table = Table("Стол")

# room = Room()
# room.add(bed)
# room.add(sofa)
# room.add(table)

# for furniture in room.furniture:
#     print(furniture.name)

# 5.
class Device:
    def turn_on(self):
        pass
class Laptop(Device):
    def turn_on(self):
        return print('Включение ноута')
class Smartphone(Device):
    def turn_on(self):
        return print('Включение телефона')

laptop = Laptop()
smartphone = Smartphone()
laptop.turn_on()
smartphone.turn_on()
