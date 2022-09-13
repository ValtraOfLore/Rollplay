import random

class RollSetup:
    def __init__(self, hp = 3, dSize = 20, lowerAttackCritRange = 1, upperAttackCritRange = 1, lowerDefenseCritRange = 1, upperDefenseCritRange = 1, attackBonus = 0, defenseBonus = 0, attackDebuff = 0, defenseDebuff = 0, setupName = ""):
        self.name = setupName
        self.maxHealth = hp
        self.health = hp
        self.diceSize = dSize
        self.lowerAttackCritRange = lowerAttackCritRange
        self.upperAttackCritRange = upperAttackCritRange
        self.lowerDefenseCritRange = lowerDefenseCritRange
        self.upperDefenseCritRange = upperDefenseCritRange
        self.rollAttackBonus = attackBonus
        self.rollDefenseBonus = defenseBonus
        self.rollAttackDetraction = attackDebuff
        self.rollDefenseDetraction = defenseDebuff

    def damage(self, amt = 1):
        self.health = self.health - amt
        return self.health > 0

    def isAlive(self):
        return self.health > 0

    def rollAttack(self):
        d = random.randrange(1, self.diceSize)
        return {
            "Natural": d,
            "Unnatural": min(d + self.rollAttackBonus - self.rollAttackDetraction, self.diceSize),
            "CritSuccess": d > self.diceSize - self.upperAttackCritRange,
            "CritFail": d <= self.lowerAttackCritRange
        }

    def rollDefense(self):
        d = random.randrange(1, self.diceSize)
        return {
            "Natural": d,
            "Unnatural": min(d + self.rollDefenseBonus - self.rollDefenseDetraction, self.diceSize),
            "CritSuccess": d > self.diceSize - self.upperDefenseCritRange,
            "CritFail": d <= self.lowerDefenseCritRange
        }

    def rollInit(self):
        return random.randrange(1, 100)

    def reset(self):
        self.health = self.maxHealth
