#you can send arguments with the key = value syntax 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
my_function(name = "Buddy", animal = "dog")
my_function("dog", "Buddy")
my_function("Buddy", "dog")
#using key arguements the order
#of argument can be changed
