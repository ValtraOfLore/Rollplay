from RollSetup import RollSetup

def genSetup(duelist0Level, duelist1Level, duelist0Form = 0, duelist1Form = 0):
    diff0 = max(duelist0Level - duelist1Level, 0)
    diff1 = max(duelist1Level - duelist0Level, 0)
    upperAttackThres0 = upperDefenseThres0 = upperAttackThres1 = upperDefenseThres1 = 1
    attackDebuff0 = attackDebuff1 = defenseDebuff0 = defenseDebuff1 = 0
    attackBuff0 = defenseBuff0 = diff0
    attackBuff1 = defenseBuff1 = diff1

    # Logic for forms' rules. TODO: Move to a better place.
    if duelist0Form == 2:
        upperAttackThres0 = 2
    elif duelist0Form == 3:
        defenseBuff0 += 1
        attackDebuff0 += 1
    elif duelist0Form == 4:
        attackBuff0 += 1
        defenseDebuff0 += 1
    elif duelist0Form == 5:
        upperDefenseThres0 = 2
    elif duelist0Form == 6:
        print("No simulation for form 6.")
    elif duelist0Form == 7:
        defenseDebuff1 = 1

    if duelist1Form == 2:
        upperAttackThres1 = 2
    elif duelist1Form == 3:
        defenseBuff1 += 1
        attackDebuff1 += 1
    elif duelist1Form == 4:
        attackBuff1 += 1
        defenseDebuff1 += 1
    elif duelist1Form == 5:
        upperDefenseThres1 = 2
    elif duelist1Form == 6:
        print("No simulation for form 6.")
    elif duelist1Form == 7:
        defenseDebuff0 = 1

    setup0 = RollSetup(hp = duelist0Level, attackBonus = attackBuff0, defenseBonus = defenseBuff0, 
        attackDebuff = attackDebuff0, defenseDebuff = defenseDebuff0, upperAttackCritRange = upperAttackThres0, 
        upperDefenseCritRange = upperDefenseThres0, setupName = f"L{duelist0Level}F{duelist0Form}")
    setup1 = RollSetup(hp = duelist1Level, attackBonus = attackBuff1, defenseBonus = defenseBuff1, 
        attackDebuff = attackDebuff1, defenseDebuff = defenseDebuff1, upperAttackCritRange = upperAttackThres1, 
        upperDefenseCritRange = upperDefenseThres1, setupName = f"L{duelist1Level}F{duelist1Form}")

    return (setup0, setup1)