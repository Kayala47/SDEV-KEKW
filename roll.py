import random

def roll(die, adv):
    roll1 = random.randint(0, die)
    
    if adv == True:
        roll2 = random.randint(0, die)
        out = "Rolled a {}.".format(max(roll1, roll2))
        return out

    else:
        out = "Rolled a {}.".format(roll1)
        return out


if __name__ == "__main__":
    r = int(input("die> "))
    a = input("advantage (y/n)> ")
    
    if a == "y":
        print(roll(r, True))
    else:
        print(roll(r, False))