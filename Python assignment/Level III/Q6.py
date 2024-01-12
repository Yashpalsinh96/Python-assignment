class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog_instance = Dog("Buddy")
print(dog_instance.speak())

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} can fly"

class FlyingDog(Dog, Bird):
    def __init__(self, name):
        Dog.__init__(self, name)
        Bird.__init__(self, name)

flying_dog_instance = FlyingDog("SkyBuddy")
print(flying_dog_instance.speak())
print(flying_dog_instance.fly())

class Reptile(Animal):
    def crawl(self):
        return f"{self.name} can crawl"

class Snake(Reptile):
    def __init__(self, name):
        Reptile.__init__(self, name)

snake_instance = Snake("Slither")
print(snake_instance.speak())
print(snake_instance.crawl())
