class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old.")
my_dog.sit()
my_dog.roll_over()


your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} year old.")
your_dog.sit()
your_dog.roll_over()


super_dog = Dog('SUPER', 27)
print(f"This dog's name is {super_dog.name}")
print(f"This dog is {super_dog.age} year old.")
super_dog.sit()
super_dog.roll_over()
