import player

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
    if self.ability not == "Haste":
      self.sick = True
    
  def getLoc(self):
    loc = ""
    for p in [player1, player2]
      for i in [field, hand, deck]:
        if self in p.i:
          loc = p.i
      
    return loc
    
  def Die(self):
    currentPlayer.grave += self
    del currentPlayer.field(self)
  
  def Hit(self, target, fast):
    target.health -= self.power
    if fast = True:
      target.HealthCheck()
  
  def Attack(self, target):
    if self.sick = True:
      return self , " has summoning sickness!."
    
    if self.ability == "First Strike" and target.ability not == "First Strike":
      self.hit(target, True)
      target.hit(self)
      self.HealthCheck()
      
    elif self.ability == "Double Strike" and target.ability not == "Double Strike":
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
