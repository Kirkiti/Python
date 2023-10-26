class Cars:
    def __init__(self, type, color, model):
        self.type = type
        self.color = color
        self.model = model
    def onyesha(self):
        print(f"I love {self.model} cars which is a {self.type} being {self.color} in color")

# creating object
myobj = Cars("Saloon", "White", "Toyota")
myobj.onyesha()
myobj2 = Cars("S.Wagon", "Black", "Mercedes")
myobj2.onyesha()

