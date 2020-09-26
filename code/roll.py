import random
def roll(die):
    return random.randint(1, die)

def rolladv(adv):
    roll1 = roll(20)
    roll2 = roll(20)

    if adv == True:
        out = "Rolled a {} and {} with advantage for a {}.".format(roll1, roll2, max(roll1, roll2))
        return out
    else:
        out = "Rolled a {} and {} with disadvantage for a {}.".format(roll1, roll2, min(roll1, roll2))
        return out

def multiroll(q, die, mod = 0):
    totalroll = []
    sum = 0
    for i in range(q):
        d = roll(die)
        totalroll.append(d)
        sum+=d
    print(totalroll)
    return sum + mod
    


if __name__ == "__main__":
    res = int(input(""" 
    1. roll a single die
    2. roll a single die with advantage
    3. multiroll a die

    """))
    if res == 1:
        d_size = int(input("size?> "))
        print(roll(d_size))
    
    elif res == 2:
        adv = int(input("""
        1. Advantage
        2. Disadvantage

        """))
        if adv == 1:
            print(rolladv(True))
        else:
            print(rolladv(False))
    
    elif res == 3:
        d_quant = int(input("How many?> "))       
        d_size = int(input("size?> "))
        d_mod = int(input("mod?> "))
        print(multiroll(d_quant, d_size, d_mod))
