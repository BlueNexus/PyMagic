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
    
  def Die(self):
    if self in player1.field:
      player1.grave += self
      del player1.field(self)
  
  def Hit(self, target, fast):
    target.health -= self.power
    if fast = True:
      target.HealthCheck()
  
  def Attack(self, target):
    if self.ability == 1 and target.ability not == 1:
      self.hit(target, True)
      target.hit(self)
      self.HealthCheck()
      
    elif self.ability == 2 and target.ability not == 2:
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
