import cAbility
import cCards
import cGame
import cPlayer
import cCardGenerator
import csv

allCards = []
def InitCards():
        with open('CardGenerator\cardList.csv', 'r+') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                cache = 0
                IDname = ""
                name = ""
                cost = 0
                power = 0
                defence = 0
                ability = 0
                for word in row:
                    if cache == 0:
                        name = word
                    elif cache == 1:
                        cost = word
                    elif cache == 2:
                        power = word
                    elif cache == 3:
                        defence = word
                    elif cache == 4:
                        ability = word
                    elif cache == 5:
                        IDname = word
                    cache += 1
                cardName = IDname
                cardName = cCards.Creature(name, cost, power, defence, ability)
                allCards.append(cardName)

playerChoice = input("Would you like to run the card generator? (yes/no)").lower
if playerChoice == "yes":
    maxPower = int("Please enter a maximum card power.")
    maxDefence = int("Please enter a maximum card defence.")
    balancer = int("Please enter a value for the balancer. Recommended: 2 (!Advanced!)")
    cardCount = int("Please enter the number of cards you wish to generate")
    cardGen = cCardGenerator.CardGenerator(maxPower, maxDefence, balancer, cardCount)

player1 = cPlayer.player()
player2 = cPlayer.player()
newGame = cGame.Game(player1, player2)