class Parent:
    def __init__(self, tt):
        self.message = tt

    def bilgi(self):
        print(self.message*3)

class Child(Parent):
    def __init__(self, yazi):
        super().__init__(yazi)

    def bilgi(self):
        print(self.message*5)

x = Child("Hello! ")

x.bilgi()
