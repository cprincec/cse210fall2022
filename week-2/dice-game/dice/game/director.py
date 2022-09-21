import time
from game.die import Die

class Director:
    """The dictator of the sequence of play.
    
    Attributes:
        self.dice(list): five Die instances.
        self.is_playing(boolen): Tells if the player wants to play the game.
        self.score(int): score for one round of play.
        self.total_score(int): Total score for entire game.
    """
    def __init__(self):
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        self.roll_counter = 0

        # Create an instance of Die
        # Populate self.dice list with 5 instances of Die   
        for _ in range(5):
            die = Die()
            self.dice.append(die)
        
    def game_play(self):
        """Starts and ends the game.
        
        Args:
            self(Director): An instance of the Director."""
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Receives input from user
        
        Args:
            self(Director): An instance of the Director.
        """
        # list of valid values the user can enter.
        roll_values = ["n", "y", "no", "yes"]

        if self.roll_counter == 0:
            print("\nWELCOME TO THE DICE GAME!!!")
            print("Continue rolling the dice to score points.")
            print("You score 100 points when you roll a 1")
            print("You score 50 points when you roll a 5")
            print("The game ends when you fail to roll a 1 or 5.")
            print("Type y to roll dice. Type n to exit.\n")
            time.sleep(1.5)
            roll = input("Roll again? y/n:  ").lower()

        else:
            roll = input("Roll again? y/n:  ").lower()

        while roll not in roll_values:
            print("Invalid input!")
            roll = input("\nRoll Dice? y/n ").lower()

        self.is_playing = (roll == "y")
        if self.is_playing:
            for _ in range(3):
                time.sleep(.6)
                print(".", end=" ", flush=True)
                
                
        else: 
            print(f"\nYour total score is {self.total_score} from {self.roll_counter} rounds of play.")
            print("Thanks for playing!\n")
                


    def do_updates(self):
        """Updates the attributes 
        
        Args: 
            self(Director): An instance of the Director."""
        
        if not self.is_playing:
            return

        for i in range(5):
            self.dice[i].rollDie()
            self.score += self.dice[i].points
        self.total_score += self.score

    def do_outputs(self):
        """Controls the outputs of the game.
        
        Args:
            self(Director): An instance of the Director."""

        if not self.is_playing:
            return
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "
        
        print(f"\nYou rolled {values}")
        time.sleep(1)
        print(f"Your total score is {self.total_score}\n")
        time.sleep(1.5)

        # Count number of rolls
        self.roll_counter += 1

        # Check if score for current round is more than zero.
        if self.score > 0:
            self.is_playing = True
        else:
            print("Game Over! You did not roll a 1 or 5.")
            print(f"\nYour total score is {self.total_score} from {self.roll_counter} rounds of play.")
            print("Thanks for playing!\n")
            self.is_playing = False

        # Reset the score for this round of play.
        self.score = 0



        



        
