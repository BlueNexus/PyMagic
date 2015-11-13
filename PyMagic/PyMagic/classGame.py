import classPlayer
import classCard
import PyMagic

class Game(Object):
    turn = 0
    currentPlayer = ""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.allPlayers = [player1, player2]
        self.currentPlayer = player1
        self.turn = 1
    
    def SwitchTurn(self):
        if currentPlayer == self.player1:
            currentPlayer = self.player2
            player2.startTurn()
        else:
            currentPlayer = self.player1
            player1.startTurn()
  
    def PlayTurn(self):
        playerChoice = ""
        do until playerChoice == "E":
            do until playerChoice in ["S", "V", "VB", "VG, "VL", "A", "E"]:
                playerChoice = input(currentPlayer + ", please select one of the following options. S = Summon, V = View hand, VB = View field, VG = View graveyard, VL = View lands, A - Attack, E - End turn")
            if playerChoice == "S":
                cardChoice = input("Please enter the creature you wish to summon.")
                if currentPlayer.CanSummon(cardChoice):
                    currentPlayer.Summon(cardChoice)
            elif playerChoice == "V":
                currentPlayer.SeeHand()
            elif playerChoice == "VB":
                for player in players:
                    player.SeeField()
            elif playerChoice == "VG":
                currentPlayer.SeeGrave()
            elif playerChoice == "VL":
                currentPlayer.SeeLand()
            elif playerChoice == "A":
                attacking = input("Please enter a card on the field to attack with.")
                inField = False
                if attacking in currentPlayer.field:
                    inField = True
                target = input("Please enter a card on the field to attack.")


player1 = classPlayer.player()
player2 = classPlayer.player()
newGame = Game(player1, player2)
            
    
