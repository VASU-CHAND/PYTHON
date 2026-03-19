#inheritence of where one class (child class) inherit the properties and methods of another classs(parent class)
#purpose --- code reuse
#less duplication
# easy maintainance
class animal:
    def eat(self):
        print("animal is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")


d=dog()
d.eat()
d.bark()