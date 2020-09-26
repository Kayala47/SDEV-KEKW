import random

def roll(die, adv = False):
    roll1 = random.randint(0, die)
    
    if adv == True:
        roll2 = random.randint(0, die)
        out = "Rolled a {} and {} for a {}.".format(roll1, roll2, max(roll1, roll2))
        return out

    else:
        out = "Rolled a {}.".format(roll1)
        return out

def multiroll(q, die, mod = 0):
    totalroll = []
    sum = 0
    for i in range(q):
        d = roll(die)
        totalroll.append(d)
        sum+=d
    


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
        d_size = int(input("size?> "))
        print(roll(d_size, True))
    # elif res == 3:
    #     d_quant = int(input("How many?> "))       
    #     d_size = int(input("size?> "))
    #     d_mod = int(input("mod?> "))
    #     print(multiroll(d_quant, d_size, d_mod))
