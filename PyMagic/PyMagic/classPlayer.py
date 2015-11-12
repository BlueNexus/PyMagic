class player(object):
    hand = []
    deck = []
    field = []
    grave = []
    lands = []
    health = 0
    mana = 0
    def __init__(self):
        self.initDeck()
        self.health = 20
        for i in range(1, 8):
            self.draw()
    
  
    def draw(self):
        self.hand.append(self.deck[(len(self.deck) - 1)])
        del self.deck[len(self.deck) - 1]

    def startTurn(self):
        if len(self.hand) < 8:
            self.draw()
        for i in self.lands:
            self.mana += i.mana
  
    def endTurn(self):
        for m in self.field:
            m.health = m.defence
            m.untap()
