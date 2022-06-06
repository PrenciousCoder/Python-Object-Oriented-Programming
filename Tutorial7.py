class Car:
    Make=None
    model=None
    year=None
    color=None

    def __init__(self,Make,model,year,color):
        self.Make=Make
        self.model=model
        self.year=year
        self.color=color
        

    def drive(self):
        print("This Car is driving: ")
    def stop(self):
        print("This car is stopped: ")


car_1=Car("chevy","Corvette",2021,"Blue")

print(car_1.Make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

car_2=Car("Ford","Mustang",2022,"Red")
print(car_2.Make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()
