class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi i am", self.name, 'and i am', self.age, 'years old')

    def talk(self):
        print("Bark")


class Cat(dog):  # dog is the parent class....cat will derive from the dog
   def __init__(self, name, age, color):
       super().__init__(name, age)  # arguments inherited from dog
       self.color = color

   def talk(self):
        print("meow!")


jim=dog('jim',70)
jim.talk()
tim=Cat('Tim', 5, 'Blue')
tim.speak()

class vehicle():
    def __init__(self,price,gas,color):
        self.price =price
        self.gas=gas
        self.color=color

    def fillUptank(self):
        self.gas=100
        
    def emptyTank(self):
        self.gas=0

    def gasLeft(self):
        return self.gas

class Car(vehicle):
    def __init__(self, price,gas,color,speed):
        super().__init__(price,gas,color) # arguments inherited from vehicle
        self.speed=speed
    def beep(self):
        print('Beep Beep')

class Truck(vehicle):
    def __init__(self,price,gas,color,tires):
        super().__init__(price,gas,color)
        self.tires=tires

    def beep(self):
        print("honk Honk")
