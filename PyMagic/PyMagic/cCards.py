import core

class Creature(object):
    '''A creature-type card with health, power, abilites, etc'''
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

    def __repr__(self):
        return("Monster: %s H: %s C: %s P: %s D: %s A: %s" % (self.name, self.health, self.cost, self.power, self.defence, self.ability))
    
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
        for p in [core.player1, core.player2]:
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
            for player in (player1, player2):
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
            self.HealthCheck()
            target.HealthCheck()
        self.tap()

