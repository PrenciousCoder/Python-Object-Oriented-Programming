class private:

    def __init__(self,name):
        self.name=name

class NotPrivate:
    def __init__(self, name):
        self.name=name
        self.priv= private(name)

    def _display(self):
        print("Hello")
    def display(self):
        print('Hi')
