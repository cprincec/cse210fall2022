import random
class Die:
    """A small die with six faces. The responsibility is to 
    keep track of the number facing up and points each number is worth.
    
    Attributes:
        value(int): the number facing up when the die is rolled.
        points(int): the points for the value of the die.
    """
    def __init__(self):
        """Constructs a new instance of Die. Holds the value and points attributes.
        
        Args:
            self(Die): An instance of Die."""
        self.value = 0
        self.points = 0

    def rollDie(self):
        """Roll the die and calculate its point. 
        
        Args:
            self(Die): An instance of Die.

        Return: list of value and its calulated points."""
        self.value = random.randint(1,6)
        if self.value == 1:
            self.points = 100
        elif self.value == 5:
            self.points = 50
        else:
            self.points = 0



