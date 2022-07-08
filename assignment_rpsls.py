import random
import enum
import abc

class GamePlayers:
    def __init__(self,value):
        self.value=value
        
class Rock(GamePlayers):
    value=1
class Spock(GamePlayers):
    value=2
class Paper(GamePlayers):
    value=3
class Lizard(GamePlayers):
    value=4
class Scissors(GamePlayers):
    value=5


class PlayerEnum(enum.Enum):
    rock="rock"
    spock="spock"
    paper = "paper"
    lizard = "lizard"
    scissors = "scissors"
    

class PlayGames(abc.ABC):
    def __init__(self,name):
         self.name=name
         self.player=self.get_player_instance()
         
    def get_player_instance(self):
        if PlayerEnum(self.name) == "rock":
            return Rock()
        elif PlayerEnum(self.name) == "spock":
            return Spock()
        elif PlayerEnum(self.name) =="paper":
            return Paper()
        elif PlayerEnum(self.name) =="lizard":
            return Lizard()
        elif PlayerEnum(self.name) =="scissors":
            return Scissors()

class RPSLS(object):
    
    objects = ["rock", "spock", "paper", "lizard", "scissors"]

    def number_to_name(self, idx):
        """
        converting number to object name
        
        """
        return self.objects[idx - 1]

    def computer_guess(self):
        return random.randrange(1, 6)

    def play_one(self, name):
        """
        user vs ai

        """
        
        player = name
        robot  = self.computer_guess()
        winner = (player - robot) % len(self.objects)
        if winner == 0:
            # Result is 0
            winner = "Tie"
            
        elif winner == 1:
            winner = "Player"
            
        elif winner == -1:
            winner = "Robot"
            
        elif (winner % 2 == 0):
            # Result is even
            winner = "Player"
        
        elif (winner % 2 != 0):
            # Result is odd
            winner ="Robot"

        player = self.number_to_name(player)
        robot  = self.number_to_name(robot)

        return (player, robot, winner)
    
    def play_two(self):
        """
        user1 vs user2

        """
        
        player1 = self.computer_guess()
        player2  = self.computer_guess()
        winner = (player1 - player2) % len(self.objects)

        if winner == 0:
            # Result is 0
            winner = "Tie"
            
        elif winner == 1:
            winner = "Player1"
            
        elif winner == -1:
            winner = "Player2"

        elif (winner % 2 == 0):
            # Result is even
            winner = "Player1"
        
        elif (winner % 2 != 0):
            # Result is odd
            winner ="Player2"

        player1 = self.number_to_name(player1)
        player2  = self.number_to_name(player2)

        return (player1, player2, winner)

if __name__ == "__main__":

    game = RPSLS()
    print('Welcome to Rock Paper Scissors Lizard Spock')
    print()
    print('each match will be best of three games')
    print('Use the number keys to enter your selection')
    print()
    print()
    print('Scissors cut Paper')
    print('Paper covers Rock')
    print('Rock crushes Lizard')
    print('Lizard poisons Spock')
    print('Spock smashes Scissors')
    print('Scissors decapitates Lizard')
    print('Lizard eats Paper')
    print('Paper disapproves Spock')
    print('Spock vapourizes Rock')
    print('Rock crushes Scissors')
    print()
    print('How many players? 1, 2')
    n_players = int(input())
    print('Choose 1 for Rock')
    print('Choose 2 for Spock')
    print('Choose 3 for Paper')
    print('Choose 4 for Lizard')
    print('Choose 5 for Scissors')
    print()
    if n_players == 1:
        while(1):
            gesture = int(input('Choose your gesture.'))
            player, robot, winner = game.play_one(gesture)
            print('Player one chose', player)
            print('AI has picked', robot)
            if winner == 'Tie':
                print('Its a tie, play again!')
                continue
            else:
                if winner == 'Player':
                    print('Player has won!!!')
                else:
                    print('Robot has won!!!')
                break
        
    else:
        while(1):
            player1, player2, winner = game.play_two()
            print('AI 1 has picked', player1)
            print('AI 2 has picked', player2)
            if winner == 'Tie':
                print('Its a tie, play again!')
                continue
            else:
                if winner == 'Player1':
                    print('Player 1 has won!!!')
                else:
                    print('Player 2 has won!!!')
                break