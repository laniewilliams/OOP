import random

class Insect:


    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0


    def flight(self):

        self.flight = random.randint(1,10)
        print(self.flight)
    
    def get_flight(self):
        return self.flight

