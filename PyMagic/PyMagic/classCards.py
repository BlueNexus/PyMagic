import csv

allCards = []
with open('monsterList.csv', 'rb') as csvfile:
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
                IDname = word
            elif cache == 2:
                cost = word
            elif cache == 3:
                power = word
            elif cache == 4:
                defence = word
            elif cache == 5:
                ability = word
            cache += 1
        IDname = Monster(name, cost, power, defence, ability)

class Card(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
class Monster(Card):
    sick = False
    def __init__(self, name, cost, power, defence, ability):
        self.name = name
        self.cost = cost
        self.power = power
        self.defence = defence
        self.health = defence
        self.ability = ability
    
    def HealthCheck(self):
        if self.health < 1:
            self.Die()
    
    def summoned(self):
        if self.ability != "Haste":
            self.sick = True
    
    def getLoc(self):
        loc = ""
        for p in [player1, player2]:
            for i in [field, hand, deck]:
                if self in p.i:
                    loc = p.i
        return loc
    
    def Die(self):
        currentPlayer.grave += self
        currentPlayer.field.pop(self)
  
    def Hit(self, target, fast):
        target.health -= self.power
        if fast == True:
            target.HealthCheck()
  
    def Attack(self, target):
        if self.sick == True:
            return self , " has summoning sickness!."
    
        if self.ability == "First Strike" and target.ability != "First Strike":
            self.hit(target, True)
            target.hit(self)
            self.HealthCheck()
      
        elif self.ability == "Double Strike" and target.ability != "Double Strike":
            self.hit(target, True)
            self.hit(target, False)
            target.hit(self, False)
            target.HealthCheck()
            self.HealthCheck()
      
        else:
            self.hit(target, False)
            target.hit(self, False)
            target.HealthCheck()
            self.HealthCheck()
