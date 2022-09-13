from RollSetup import RollSetup
from SetupCreator import genSetup
from SimulationHelper import simulateDuel

if __name__ == "__main__":
    duel0 = RollSetup(hp = 4, attackBonus = 0, defenseBonus = 0, setupName = "Bonus")
    duel1 = RollSetup(hp = 3, attackBonus = 0, defenseBonus = 0, setupName = "Non-Bonus")
    simulateDuel(duel0, duel1, 10000)