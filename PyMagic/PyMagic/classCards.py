import csv
import PyMagic
import classPlayer
import classGame

class Card(object):
    allCards = []
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
class Creature(Card):
    sick = False
    alive = False
    tapped = False
    def __init__(self, name, cost, power, defence, ability):
        self.name = name
        self.cost = cost
        self.power = power
        self.defence = defence
        self.health = defence
        self.ability = ability
        self.InitCards()

    def InitCards(self):
        with open('CardGenerator\cardList.csv', 'rb') as csvfile:
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
                IDname = Monster(name, cost, power, defence, ability)
                allCards.append(IDname)

    def __repr__(self):
        return "Monster: " + self.name + " H: " + self.health + " C: " + self.cost + " P: " + self.power + " D: " + self.defence + " A: " + self.ability
    
    def HealthCheck(self):
        if self.health < 1:
            self.Die()
    
    def summoned(self):
        if self.ability != "Haste":
            self.sick = True
        self.alive = True
        self.tapped = False

    def tap(self):
        self.tapped = True
    
    def getLoc(self):
        loc = ""
        for p in [player1, player2]:
            for i in [field, hand, deck]:
                if self in p.i:
                    loc = p.i
        return loc
    
    def Die(self):
        self.alive = False
        currentPlayer.grave += self
        del currentPlayer.field[self]
        print(self.name + " has been destroyed!")
  
    def Hit(self, target, fast):
        target.health -= self.power
        print(self.name + " has hit " + target.name + " for " + str(self.power) + " damage!")
        if fast == True:
            target.HealthCheck()
  
    def Attack(self, target):
        if self.sick == True:
            print(self , " has summoning sickness!.")
            return

        if target.IsPlayer():
            self.Hit(target, Fast)

        if self.ability == "First Strike" and target.ability != "First Strike":
            self.Hit(target, True)
            target.Hit(self, False)
            self.HealthCheck()

        elif self.ability == "Double Strike" and target.ability != "Double Strike":
            self.Hit(target, True)
            self.Hit(target, False)
            target.Hit(self, False)
            target.HealthCheck()
            self.HealthCheck()

        elif self.ability == "Leech":
            self.Hit(target, False)
            self.health += self.power
            target.Hit(self, False)
            target.HealthCheck()
            self.HealthCheck()

        elif self.ability == "Ranged":
            self.Hit(target, True)

        elif self.ability == "Cleave":
            target.Hit(self)
            for player in (classPlayer.player1, classPlayer.player2):
                if player.OwnsCard(target):
                    for card in player.field:
                        self.Hit(card, False)
                        card.HealthCheck()
            self.HealthCheck()

        elif self.ability == "Assassin":
            self.Hit(target, False)
            target.Hit(self, False)
            self.HealthCheck()
            target.Die()

        else:
            self.Hit(target, False)
            target.Hit(self, False)
            target.HealthCheck()
            self.HealthCheck()

        self.tap()

