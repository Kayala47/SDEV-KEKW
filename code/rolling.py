import random
import csv
import os

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
    res = 'Slow your roll! We did not recognize the following parameters: [%s].' %(params)
    return res 

def negativeError():
    return 'Please ensure that dice and/or quantity are positive integers!'

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
        return inputError([num])
    if num < 1:
        return negativeError()
    res = random.randint(1,num)
    return res

def rollAdv(adv = True):
    if not isinstance(adv, bool):
        return inputError([adv])
    roll1, roll2 = roll(), roll()
    if adv:
        res = 'rolled %s and %s for %s!' %(roll1, roll2, max(roll1,roll2))
    else:
        res = 'rolled %s and %s for %s!' %(roll1, roll2, min(roll1,roll2))
    return res

def multiroll(die = 20, q = 1, mod = 0, fudge = 0):
    errorlist = []
    try: q = int(q)
    except ValueError: errorlist.append(str(q))
    try: die = int(die)
    except ValueError: errorlist.append(str(die))
    try: mod = int(mod)
    except ValueError: errorlist.append(str(mod))
    try: fudge = int(fudge)
    except ValueError: errorlist.append(str(fudge))
    if errorlist:
        return inputError(errorlist)
    
    if q < 1 or die < 1:
        return negativeError()
    
    rolls = [roll(die) for i in range(q)]
    if fudge == 0:
        res = 'rolled %s d %s + (%s) for %s!' %(q, die, mod, sum(rolls))
    else:
        res = 'rolled %s d %s + (%s) for %s!' %(q, die, mod, fudge)
    return res    

def manualRoll(roll, die = 20, q = 1, mod = 0):
    errorlist = []
    try: int(q)
    except ValueError: errorlist.append(str(q))
    try: int(die)
    except ValueError: errorlist.append(str(die))
    try: int(mod)
    except ValueError: errorlist.append(str(mod))
    try: int(roll)
    except ValueError: errorlist.append(str(roll))
    if errorlist:
        return inputError(errorlist)
    
    if q < 1 or die < 1:
        return negativeError()

    res = 'rolled %s d %s + (%s) for %s!' %(q, die, mod, roll)
    return res


#--------------------------------------------#
# Macro toolkit
#--------------------------------------------#

def addMacro(q, die, mod, itemname):
    errorlist = []
    try: int(q)
    except ValueError: errorlist.append(str(q))
    try: int(die)
    except ValueError: errorlist.append(str(die))
    try: int(mod)
    except ValueError: errorlist.append(str(mod))
    if errorlist:
        return inputError(errorlist)

    def build_set(filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            return {row[0] for row in reader}

    with open('macroset.csv', mode='a+', newline='') as macro_file:
        if itemname in build_set('macroset.csv'):
            return dbError(True, itemname)
        macro_writer = csv.writer(macro_file, lineterminator='\r')
        item = [itemname, q, die, mod]
        macro_writer.writerow(item)
        return 'successfully added item %s with attributes %s d %s + (%s) to the game database!'%(itemname, q, die, mod)
        
def delMacro(itemname):
    lines = list()
    item = itemname
    flag = False
    with open('macroset.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == item:
                    flag = True
                    lines.remove(row)
        if not flag:
            return dbError(flag, itemname)
    with open('macroset.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile, lineterminator='\r')
        writer.writerows(lines)
    return 'successfully deleted item %s from the game database!'%(itemname)


def callMacro(itemname):
    lines = list()
    with open('macroset.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
    for item in lines:
        if item[0] == itemname:
            return multiroll(item[2], item[1], item[3])
    return dbError(False, itemname)

def deleteMacroFile():
    if os.path.exists('macroset.csv'):
        os.remove('macroset.csv')

if __name__ == '__main__':
    
        
    name = input('name: ')
    q = input('q: ')
    die = input('die: ')
    mod = input('mod: ')
    print(addMacro(q,die,mod,name))
    # print(callMacro(name))
    # print(delMacro(name))
    # deleteFile()
    # print(rollAdv('x'))
    # cond = input("New Item? (y/n)")
    # if cond == 'n':
    #     break
