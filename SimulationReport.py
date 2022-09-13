import csv
import math
import time
from itertools import product
from RollSetup import RollSetup
from SetupCreator import genSetup
from SimulationHelper import simulateDuel

if __name__ == "__main__":
    file = open(f"OutFiles/SimulationReport_{math.floor(time.time())}.csv", "w", newline='')

    forms = input("Include forms? (Y/N): ").lower() == "y"
    amt = int(input("Simulations per setup: "))
    lvls = list(product([1, 2, 3, 4, 5, 6, 7], repeat = 2))
    writer = csv.writer(file)
    results = None
    if forms:
        lvlsWithForms = []
        formsList = [2, 3, 4, 5, 7]
        formsPerm = list(product(formsList, repeat = 2))
        for i in lvls:
            for j in formsPerm:
                lvlsWithForms.append((i[0], i[1], j[0], j[1]))
        results = [simulateDuel(*genSetup(x[0], x[1], x[2], x[3]), amt) for x in lvlsWithForms]
    else:
        results = [simulateDuel(*genSetup(x[0], x[1]), amt) for x in lvls]
    writer.writerow([f"{x['Duelist0Name']} vs {x['Duelist1Name']}" for x in results])
    writer.writerow([x["Duelist0Ratio"] for x in results])

    file.close()