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
# rolls, and store player items in the database for use.

#--------------------------------------------#
# Error toolkit
#--------------------------------------------#

def inputError(paramlist: list) -> str:
    ''' Returns an error message indicating incorrect params.
        Inputs: paramlist : list
        Outputs: error message '''

    params = ', '.join(paramlist)
    res = 'Slow your roll! We did not recognize the following parameters: [%s].' %(params)
    return res 

def negativeError() -> str:
    ''' Returns an error message indicating illegal negative params.
        Inputs: None
        Outputs: error message '''
    
    return 'Please ensure that dice and/or quantity are positive integers!'


def dbError(keyfound: bool, itemname: str) -> str:
    ''' Returns an error message indicating incorrect params.
        Inputs: keyfound : boolean indicating type of error
                itemname : str name of item raising error
        Outputs: error message '''
    
    if keyfound:
        res = '%s already exists. Please remove item if attempting to add item of same name.' %(itemname)
    else:
        res = '%s does not exist. Check your item name.' %(itemname)
    return res

#--------------------------------------------#
# Rolling toolkit
#--------------------------------------------#

# Rolling method
def roll(num: int = 20) -> int:
    ''' Returns a random integer within specified range.
        Inputs: num : int representing upper range
        Outputs: random number between 1 and num '''

    if not isinstance(num, int):
        return inputError([num])
    if num < 1:
        return negativeError()
    res = random.randint(1,num)
    return res

def rollAdv(adv: bool = True) -> str:
    ''' Returns a random integer between 1 and 20 determined by adv.
        Inputs: adv : bool indicating advantage or disadvantage
        Outputs: better or worse of two rolls depending on adv '''
    if not isinstance(adv, bool):
        return inputError([adv])
    roll1, roll2 = roll(), roll()
    if adv: # True indicates advantage, False indicates disadvantage
        res = 'rolled %s and %s for %s!' %(roll1, roll2, max(roll1,roll2))
    else:
        res = 'rolled %s and %s for %s!' %(roll1, roll2, min(roll1,roll2))
    return res

def multiroll(die: int = 20, q: int = 1, mod: int = 0, fudge: int = 0) -> str:
    ''' Rolls a given amount of die and applies modifer. Supports fudge rolling.
        Inputs: die   : upper bound on individual dice roll
                q     : number of dice to roll
                mod   : modifier for resulting roll
                fudge : if nonzero, guarantees output
        Outputs: formatted dice roll with result (changed if fudge != 0) '''
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

def manualRoll(roll: int, die: int = 20, q: int = 1, mod: int = 0) -> str:
    ''' Formats a set of rolls for manual user input.
        Inputs: die   : upper bound on individual dice roll
                q     : number of dice to roll
                mod   : modifier for resulting roll
                roll  : the amount the user actually rolled
        Outputs: formatted dice roll with user specified result '''

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

def addMacro(q: int, die: int, mod: int, itemname: str) -> str:
    ''' Adds a given item with attributes to a csv file.
        Inputs: die      : upper bound on individual dice roll
                q        : number of dice to roll
                mod      : modifier for resulting roll
                itemname : key for database
        Outputs: string indicating addition was successful '''
    
    errorlist = []
    try: int(q)
    except ValueError: errorlist.append(str(q))
    try: int(die)
    except ValueError: errorlist.append(str(die))
    try: int(mod)
    except ValueError: errorlist.append(str(mod))
    if errorlist:
        return inputError(errorlist)

    def build_set(filename: str) -> dict:
        # Creates a dict of items that can be manipulated
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            return {row[0] for row in reader} #

    with open('macroset.csv', mode='a+', newline='') as macro_file:
        if itemname in build_set('macroset.csv'):
            return dbError(True, itemname) # Disallow collisions

        macro_writer = csv.writer(macro_file, lineterminator='\r')
        item = [itemname, q, die, mod]
        macro_writer.writerow(item) # Appends new addition
        return 'successfully added item %s with attributes %s d %s + (%s) to the game database!'%(itemname, q, die, mod)
        
def delMacro(itemname: str) -> str:
    ''' Deletes a given item from the csv file.
        Inputs: itemname : key for database
        Outputs: string indicating removal was successful '''
    
    lines = list()
    item = itemname
    flag = False # Flag whether item has been found
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
        # Repopulate file with item removed and fixes formatting
        writer = csv.writer(writeFile, lineterminator='\r')
        writer.writerows(lines)
    return 'successfully deleted item %s from the game database!'%(itemname)


def callMacro(itemname: str) -> str:
    ''' Uses an item in the database.
        Inputs: itemname : key for database
        Outputs: roll message after successful item use '''
    
    lines = list()
    with open('macroset.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)

    for item in lines:
        if item[0] == itemname:
            # Uses item attributes as params for multiroll()
            return multiroll(item[2], item[1], item[3])

    return dbError(False, itemname)

def deleteMacroFile() -> None:
    ''' Deletes the database.
        Inputs: None
        Outputs: None '''
    if os.path.exists('macroset.csv'):
        os.remove('macroset.csv')

# if __name__ == '__main__':
    
        
#     name = input('name: ')
#     # q = input('q: ')
#     # die = input('die: ')
#     # mod = input('mod: ')
#     # print(addMacro(q,die,mod,name))
#     # print(callMacro(name))
#     # print(delMacro(name))
#     # deleteFile()
#     # print(rollAdv('x'))
#     # cond = input("New Item? (y/n)")
#     # if cond == 'n':
#     #     break
