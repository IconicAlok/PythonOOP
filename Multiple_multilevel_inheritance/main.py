# multiple inheritance = inherit from more than one class
#                         C(A, B)
# multilevel inheritance = ihherit from a prents which inherits from another parents
#                          C(B) <- B(A) <- A


class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass



rabit = Rabit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")




rabit.eat()
rabit.sleep()
rabit.flee()

hawk.eat()
hawk.sleep()
hawk.hunt()

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()


# rabit.hunt() # error 'Rabit' object has no attribute 'hunt'

# hwak.flee() # error 'Hawk' object has no attribute 'flee'
