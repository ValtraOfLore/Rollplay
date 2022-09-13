import math
import random
from RollSetup import RollSetup

# True when attacker succeeds.
def simulateAttack(attacker, defender):
    attackerD = attacker.rollAttack()
    defenderD =  defender.rollDefense()

    # print(f"Attacker {attacker.name} rolls {attackerD}; Defender {defender.name} rolls {defenderD}")

    # Crits cases.
    if attackerD["CritSuccess"]:
        if defenderD["CritSuccess"]:
            # Attack failed. Crit 'ties' goes to defender.
            return False 
        elif defenderD["CritFail"]:
            # 2 * 2 damage.
            defender.damage(4)
            return True
        else:
            # 2 damage otherwise.
            defender.damage(2)
            return True
    elif attackerD["CritFail"]:
        if defenderD["CritSuccess"]:
            # 2 damage to attacker.
            attacker.damage(2)
            return False
        elif defenderD["CritFail"]:
            # Attack failed. Goes to defender.
            return False
    elif defenderD["CritSuccess"]:
        # In this case, attacker did not crit.
        attacker.damage(1)
        return False

    # In every other case where no one crits, we compare the modified die sizes.
    # Ties goes to the defender.
    if attackerD["Unnatural"] > defenderD["Unnatural"]:
        defender.damage(1)
        return True

    return False

def simulateRound(sys0, sys1):
    random.seed()

    attacker = None
    defender = None

    # Roll for initation.
    sys0init = sys0.rollInit()
    sys1init = sys1.rollInit()

    # When duelists tie  in init, roll again.
    while sys0init == sys1init:
        sys0init = sys0.rollInit()
        sys1init = sys1.rollInit()

    if sys0init > sys1init:
        attacker = sys0
        defender = sys1
    else:
        attacker = sys1
        defender = sys0

    while True:
        # One round of attack/defense.
        simulateAttack(attacker, defender)
        if not defender.isAlive():
            return {
                "Winner": attacker,
                "Loser": defender
            }
        elif not attacker.isAlive():
            # Attacker could've encountered crit defense or crit failed and died.
            return {
                "Winner": defender,
                "Loser": attacker
            }
        # Otherwise swap and continue.
        attacker, defender = defender, attacker

def simulateDuel(setup0, setup1, amt):
    setup0wins = 0
    setup1wins = 0

    for i in range(amt):
        result = simulateRound(setup0, setup1)
        if result["Winner"] == setup0:
            setup0wins += 1
        else:
            setup1wins += 1
        setup0.reset()
        setup1.reset()

    winRatio = math.floor(setup0wins/amt*10000)/100
    print(f"{amt} simulations; {setup0.name} won {winRatio}% of the time; ({setup0.name} wins: {setup0wins}, {setup1.name} wins: {setup1wins})")

    return {
        "Duelist0Ratio": winRatio,
        "Duelist0Wins": setup0wins,
        "Duelist1Wins": setup1wins,
        "Duelist0Name": setup0.name,
        "Duelist1Name": setup1.name
    }