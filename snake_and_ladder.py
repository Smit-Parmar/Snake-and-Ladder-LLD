import random
class Dice:
    def __init__(self,dice_count):
        self.dice_count=dice_count #Number of dice use to play game
        self.dice_output=0 #Output after rolling dice
    
    def rollDice(self):
        self.dice_output=0 
        count=0
        while count<self.dice_count:
            self.dice_output+=random.randint(1,6)
            count+=1
        return self.dice_output

class Game(Dice):

    def __init__(self,board_size,n_player,snakes,ladders,dice_count):
        self.board_size=board_size
        self.destination=board_size*board_size
        self.n_player=n_player
        self.player_position=[0]*n_player
        self.snakes=snakes
        self.ladders=ladders
        self.winner=None
        Dice.__init__(self,dice_count)

    def move_player(self,player): #player will mover forward and check for snake and ladder
        prev_pos = self.player_position[player]
        new_pos = prev_pos + self.rollDice()

        if new_pos >= self.destination: # winner! game over
            self.winner = player
            new_pos = self.destination
        elif new_pos in self.snakes:
            new_pos = self.snakes[new_pos]
            print(f"#{player+1} got bitten by snake and fall to {new_pos}")
        elif new_pos in self.ladders:
            new_pos = self.ladders[new_pos]
            print(f"#{player+1} got ladder and climbed to {new_pos}")
        self.player_position[player] = new_pos

    def move_players(self): #Each player will have turn
        for player in range(self.n_player):
            self.move_player(player)
            if self.winner is not None: # done with game
                break
        print(self.player_position)

    def startGame(self):
        while self.winner is None:
            self.move_players() #Each and every player will have turn

        return f"Player #{self.winner + 1} Wins!"



snakes = {16: 4, 22:10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
ladders = {3: 12, 7: 23, 11:25, 21: 56, 47: 53, 60: 72, 80: 96}
game=Game(10,5,snakes,ladders,1)
winner=game.startGame()
print(winner)
