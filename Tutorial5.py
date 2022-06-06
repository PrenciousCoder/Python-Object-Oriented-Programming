class Dog:
    dogs = []
    xc=5

    def __init__(self,name):
        self.name=name
        self.dogs.append(self)
    
    # CLass methods
    def num_dogs(cls):
        return len(cls.dogs)

    # Static method....to use as normal functions inside a class
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("bark!")

tim = Dog("Tim")
jim= Dog('Jim')

print(tim.num_dogs())
Dog.bark(5)
