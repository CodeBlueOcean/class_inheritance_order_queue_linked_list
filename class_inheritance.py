# Class inheritance Syntax

# class Parent: 
#     def __init__():
        # parent methods and attributes are defined here

# class Child(Parent):
    # parent methods and attributes are inherited
    # child methods and attributes are defined here

# Inheritance example

# class Human:
#     def _init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def walk(self, direction):
#         print(self.name,"walks to the", direction)
#     def talk(self, speech):
#         print(self.name, "says:", speech)

# class Wizard(Human):
#     def cast_spell(self, spell):
#         print(self.name, "casts", spell)

# # Wizard Class is a sub class of Human

# # super() function

# class Parent:
#     def __init__():

# class Child(Parent):
#     def __init__():
#     super().__init__()
    # calls __init__() method of parent

# super() function example

# class Wizard(Human):
#     def __init__(self, name, age, spell_points):
#         super().__init__(name, age)
#         self.spell_points = spell_points
    
    # def cast_spell(self, spell):
    #     print(self.name, "casts", spell)
