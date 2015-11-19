import classAbility
import classCards
import random

class CardGenerator(object):
    nameList = []
    abilityList = []
    def __init__(self, maxPower, maxDefence, balancer, cardCount):
        self.InitNames()
        self.InitAbilities()
        print("CardGen: Initialisation complete.")
        self.maxPower = maxPower
        self.maxDefence = maxDefence
        self.balancer = balancer
        self.cardCount = cardCount
        self.Generate()

    def Generate(self):
        print("CardGen: Generating " + self.cardCount + " cards.")
        workDeck = []
        for i in self.cardCount:
            print("CardGen: Generating card ", i, " of ", self.cardCount)
            workName = self.nameList[randint(len(self.nameList))]
            workAbility = self.abilityList[randint(len(self.abilityList))]
            workPower = randint(self.maxPower)
            workDefence = randint(self.maxDefence)
            workID = randint(self.cardCount * 100)
            workCost = int(((workPower + workDefence) / self.balancer) + (workAbility.cost / self.balancer))
            workID = Creature(workname, workCost, workPower, workDefence, workAbility, workID)
            workDeck.append(workID)
        print("CardGen: Generation complete.")
        self.Save(workDeck)

    def Save(self, deck):
        print("CardGen: Saving cardlist")
        file = open('CardGenerator\cardList.csv', 'a')
        for card in deck:
            file.write(card)
            file.write("\n")
        print("CardGen: Saved ", len(deck), " cards.")
        file.close()

    def InitNames(self):
        with open('CardGenerator\nameList.csv', 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            print("CardGen: Initialising name list.")
            for row in spamreader:
                name = ""
                for word in row:
                    name = word
                self.nameList.append(name)

    def InitAbilities(self):
        with open('CardGenerator\abilityList.csv', 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            print("CardGen: Initialising ability list.")
            for row in spamreader:
                name = ""
                cost = 0
                cache = 0
                for word in row:
                    if cache == 0:
                        name = word
                        cache += 1
                    elif cache == 1:
                        cost = word
                name = Ability(name, cost)
                abilityList.append(name)


'''
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

(In case I decide to go back to premade cards)
'''
