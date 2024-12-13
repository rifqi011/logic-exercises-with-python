def totalLegs(chickens, goats, cows):
    if chickens < 0 or goats < 0 or cows < 0:
        return "Input isn't valid"
    return chickens * 2 + goats * 4 + cows  * 4

print(totalLegs(2, 2, -1))