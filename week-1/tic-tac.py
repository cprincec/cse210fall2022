def main():
    game = Director()
    game.playGame()


class Board:
    """This class contains everything about the tic tact toe game board."""
    def __init__(self):
        self.board = []

        for i in range(9):
            self.board.append(i + 1)

    # Print the board
    def displayBoard(self):
        """Display the elements in the board list as a grid"""
        print()
        for i in range(9):
            # Check if the number should be the last on a column.
            # then go to a new line.
            if (i + 1) % 3 == 0:
                print(self.board[i], end="\n")
                if i < 8:
                    print("-+-+-")
            else:
                print(self.board[i], end="|")
        print()
    
    def updateBoard(self, cell, player):
        """Change the value of board element 
        at a given index to a player's symbol."""
        
        if cell > len(self.board) or cell < 1:
            print("Invalid input")
            return False
        
        elif cell not in self.board:  
            print("Taken")
            return False
        
        else:
            self.board[cell - 1] = player
            return True



    def checkWin(self):
        """Return True if there is winner,
        False if there is no winner."""
        return (
            # Check possible win by row.
            (self.board[0] == self.board[1] == self.board[2]) or 
            (self.board[3] == self.board[4] == self.board[5]) or
            (self.board[6] == self.board[7] == self.board[8]) or

            # Check win by column.
            (self.board[0] == self.board[3] == self.board[6]) or 
            (self.board[1] == self.board[4] == self.board[7]) or
            (self.board[2] == self.board[5] == self.board[8]) or 

            # Check win by diagonal.
            (self.board[0] == self.board[4] == self.board[8]) or 
            (self.board[2] == self.board[4] == self.board[6]) 
        )

    def checkTie(self):
        """Return True is the game is a draw,
        False if there isn'nt"""

        for i in range(9):
            if (i + 1) in self.board:
                return False
            
        return True


class Player:
    """This holds everything about the game player."""
    def __init__(self):
        self.player = "x"

    # def setPlayer(self):
    #     """Return the current player"""
    #     return self.player

    def switchPlayer(self):
        if self.player == "x":
            self.player = "o"

        elif self.player ==  "o":
            self.player = "x"

    def makeMove(self):
        try:
            cell = int(input(f"{self.player}'s turn. Enter a number 1-9: "))
            return cell
        
        except ValueError:
            print("Invalid Input")
            return self.makeMove()



class Director:
    """This class controls the game.
    Stores all the needed Objects for the game
    and call the methods as needed."""

    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.winner = ""
        self.keep_playing = True
    
    def playGame(self):

        while self.keep_playing:
            # Switch player's turn.
            self.player.switchPlayer()
            # Display the board.
            self.board.displayBoard()
            cell = self.player.makeMove()
            # Continue asking for new number if user's cell number
            # is not available.
            while not self.board.updateBoard(cell, self.player.player):
                cell = self.player.makeMove()
            # Check win.
            if self.board.checkWin():
                self.winner = self.player.player
                self.board.displayBoard()
                print(f" {self.winner} wins! Congratulations!\n")
                self.keep_playing = False

            # Check Tie.
            elif self.board.checkTie():
                self.board.displayBoard()
                print("The game is a draw!")
                self.keep_playing = False
    



if __name__ == "__main__":
    main()
    

           