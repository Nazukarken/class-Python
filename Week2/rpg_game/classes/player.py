class Player:
    #dunder method
    def __init__(self, name, strength = 100 ):
        
        self.name = name
        self.strength = strength

        self.weapons = []
    
    def walk(self):
        self.strength -=1 #strength = strength -1