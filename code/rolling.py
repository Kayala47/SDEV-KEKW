from random import *
import csv

# Component Design - Rolling Module

# Team: Discord Dragons
#     Members: Dana, Kevin, Max, Swamik
#     Project: 3C: Component Design
#     Primary Author: Max
#     Slip Days: 0

# PURPOSE: 

# The purpose of this module is to cover rolling requirements
# for common TTRPG games. The module will be able to use this 
# module to randomize custom dice rolls, specify manual input 
# rolls, and store player items in the database.

#--------------------------------------------#
# Error toolkit
#--------------------------------------------#

def inputError(paramlist):
    params = ', '.join(paramlist)
    res = 'Slow your roll! We did not recognize the following parameters: [%s], please be sure to use the following format: x d y + z.' %(params)
    return res 

def dbError(keyfound, itemname):
    if keyfound:
        res = '%s already exists. Please remove item if attempting to add item of same name.' %(itemname)
    else:
        res = '%s does not exist. Check your item name.' %(itemname)
    return res

#--------------------------------------------#
# Rolling toolkit
#--------------------------------------------#

def roll(num = 20):
    if not isinstance(num, int):
        return inputError(['roll'])
    res = randint(1,num)
    return res

def rollAdv(adv = True):
    if not isinstance(adv, bool):
        return inputError(['adv'])
    roll1, roll2 = roll(), roll()
    if adv:
        res = 'rolled %s and %s for %s!' %(roll1, roll2, max(roll1,roll2))
    else:
        res = 'rolled %s and %s for %s!' %(roll1, roll2, min(roll1,roll2))
    return res

def multiroll(die = 20, q = 1, mod = 0, fudge = 0):
    errorlist = []
    if not isinstance(die, int):
        errorlist.append(str(die))
    if not isinstance(q, int):
        errorlist.append(str(q))
    if not isinstance(mod, int):
        errorlist.append(str(mod))
    if not isinstance(fudge, int):
        errorlist.append(str(fudge))
    if errorlist:
        return inputError(errorlist)
    
    rolls = [[roll(die)] for i in range(q)]
    if fudge == 0:
        res = 'rolled %s d %s + (%s) for %s!' %(q, die, mod, sum(rolls))
    else:
        res = 'rolled %s d %s + (%s) for %s!' %(q, die, mod, fudge)
    return res    

def manualRoll(roll, die = 20, q = 1, mod = 0):
    errorlist = []
    if not isinstance(die, int):
        errorlist.append(str(die))
    if not isinstance(q, int):
        errorlist.append(str(q))
    if not isinstance(mod, int):
        errorlist.append(str(mod))
    if not isinstance(roll, int):
        errorlist.append(str(roll))
    if errorlist:
        return inputError(errorlist)
    
    res = 'rolled %s d %s + %s for %s!' %(q, die, mod, roll)
    return res


#--------------------------------------------#
# Macro toolkit
#--------------------------------------------#

def addMacro(q, die, mod, itemname):
    errorlist = []
    if not isinstance(die, int):
        errorlist.append(str(die))
    if not isinstance(q, int):
        errorlist.append(str(q))
    if not isinstance(mod, int):
        errorlist.append(str(mod))
    if not isinstance(itemname, str):
        errorlist.append(str(itemname))
    if errorlist:
        return inputError(errorlist)

    def build_set(filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            return {row[0] for row in reader}

    with open('macroset.csv', mode='a+', newline='') as macro_file:
        if itemname in build_set('macroset.csv'):
            return print(dbError(True, itemname))
        macro_writer = csv.writer(macro_file, lineterminator='\r')
        item = [itemname, q, die, mod]
        macro_writer.writerow(item)
        return 'successfully added item %s with attributes %sd%s+(%s) to the game database!'%(itemname, q, die, mod)
        
def delMacro(itemname):
    with open('macroset.csv', mode='w') as macro_file:
        macro_writer = csv.writer(macro_file)
        for row in csv.reader(macro_file):
            if row[0] == itemname:
                macro_writer.writerow(row)

def callMacro(itemname):
    pass



if __name__ == '__main__':

        
    name = input('name: ')
    q = input('q: ')
    die = input('die: ')
    mod = input('mod: ')
    print(addMacro(int(q), int(die), int(mod), name))
    # cond = input("New Item? (y/n)")
    # if cond == 'n':
    #     break
