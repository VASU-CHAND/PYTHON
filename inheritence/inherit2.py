class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def bark(self):
        print("dog is barking")
d=animal()
s=dog()
d.sound()
s.bark()
s.sound()