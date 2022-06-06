class Dog(object):
    def __init__(self,name,age): # self is used to create a attribute
        self.name = name 
        self.age=age

    def speak(self): # to create methods
        print("Hi i am", self.name, "and I am", self.age,'years old')

    def change_age(self,age):
        self.age=age

    def add_weight(self,weight):
        self.weight=weight
        

tim = Dog('Tim',55)
fred = Dog('Fred',3)
tim.change_age(5)
tim.add_weight(70)
tim.speak()
fred.speak()

print(tim.age)
print(tim.weight)

