class Students():
    
    def __init__(self, name, id):
        self.name = name
        self.id = id 
        
    def changeID(self, id):
        self.id = id
        
    def print(self):
        print("{} - {}".format(self.name, self.id))
        

jane = Students("Jane", 10)
jane.print()
jane.changeID(20)
jane.print()