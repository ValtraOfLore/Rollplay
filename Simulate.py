from SetupCreator import genSetup
from SimulationHelper import simulateDuel

if __name__ == "__main__":
    d0L = int(input("Enter duelist 0's level: "))
    d0F = int(input("Enter duelist 0's form (or 0 for none): "))
    d1L = int(input("Enter duelist 1's level: "))
    d1F = int(input("Enter duelist 1's form (or 0 for none): "))
    simCount = int(input("Enter simulation amount: "))
    setup0, setup1 = genSetup(duelist0Level = d0L, duelist1Level = d1L, duelist0Form = d0F, duelist1Form = d1F)
    simulateDuel(setup0, setup1, simCount)