
# This is a file that has copied all of the code from the actual bot interface code, however, for testing sake, 
# instead of making the bot listen to messages from chat, the functions are changed to allow for string inputs 
# and thus we can check correctness of the functions automatically using python unittesting 

def helpMe(): 
    return "SOME MESSAGE TO HELP: maybe a link to github"

def roll(arg):
    results = []
    data = " ".join(arg)
    # spliting the input by a space 
    arg = data.split(" ")
    if data == "":
        return "You called default roll, rolling a d20"
    # returns a bool if the user inputted a fudge roll or not. sending data to the helper function 
    isFudgeRoll = hasFudge(data)
    if not("d" in data):
        return "Input Error: Make sure that your input for roll is in the format xdy + m"
    # Even if everthing is spaced out with a fudge roll =, the max length of args is 6 
    if len(arg)>6:
        return "Too many inputs for the roll function"
    #fudge roll will never be in arg[0] because it is space sensative 
    firstParam = arg[0]
    # spliting the first argument by "d"
    paramList = firstParam.split("d")
    if len(paramList) == 0:
        return "Input Error: Make sure that your input for roll is in the format xdy + m"
    numDie = paramList[0]
    if numDie == "": 
        return "Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information"
    results.append(numDie)
    # Call to the helper function to get the side die 
    sideDie = getSideDie(data)
    # the case if they split x d y with spaces between each 
    if sideDie == "": 
        return "Please input a value for the side of dice. Roll should be in format xdy +m where y is the number of sides of the die you want to roll. Please use help for more information"
    sideDie = sideDie.strip()
    results.append(sideDie)

    # We are passing the whole string input to the helper function getModifier 
    modifier = getModifier(data, isFudgeRoll)

    # in case there is extra spaces in the modifier returned after the call to getModifier 
    modifier = modifier.strip()

    # No need to check if modifier is "" because if there is no user input for modifier, defaults to +0 
    results.append(modifier)
    # isFudgeRoll is a bool value to see if there is a fudgeroll in the input, if there is, add to the results list 
    if isFudgeRoll:
        fudgeVal = getFudgeValue(data)
        results.append(fudgeVal)
    # returning the value 
    return(results)
"""
Rolling adv takes no inputs.
"""
def rollAdv():
    return "Called rollAdv."

"""
Rolling disadv takes no inputs.
"""
def rollDisadv():
    return "Called rollDisadv."
# """
# The function that takes care of manual rolls. we want to make sure that the format for manual rolls is the same as the one for normal rolls. 
# As such, we will have almost all the similar checks as the ones used in roll 
# """
def mRoll(arg):
    results = []
    data = " ".join(arg)
    # spliting the input by a space 
    arg = data.split(" ")
    if data == "":
        return "You cannot call manual roll with no inputs. Put in form xdy + m rollResult"
    # reusing the hasFudge helper function to check to see if the user has a roll Result 
    if not("d" in data):
        return "Input Error: Make sure that your input for roll is in the format xdy + m rollResult"
    # Even if everthing is spaced out with a rollResult, the max length of args is 6 
    if len(arg)>6:
        return "Too many inputs for the manual roll function"

    firstParam = arg[0]
    # spliting the first argument by "d"
    paramList = firstParam.split("d")
    if len(paramList) == 0:
        return "Input Error: Make sure that your input for roll is in the format xdy + m rollResult"
    numDie = paramList[0]
    if numDie == "": 
        return "Please input a value for the number of dice. Roll should be in format xdy+m rollResult where x is number of dice you want to roll. Please use help for more information"
    results.append(numDie)
    # Call to the helper function to get the side die 
    sideDie = getSideDie(data)
    # the case if they split x d y with spaces between each 
    if sideDie == "": 
        return "Please input a value for the side of dice. Roll should be in format xdy +m rollResult where y is the number of sides of the die you want to roll. Please use help for more information"
    sideDie = sideDie.strip()
    results.append(sideDie)

    # returns a bool if the user inputted a rollResult or not. sending data to the helper function 
    hasRollResult = hasFudge(data)

    # We are passing the whole string input to the helper function getModifier 
    modifier = getModifier(data, hasRollResult)

    # in case there is extra spaces in the modifier returned after the call to getModifier 
    modifier = modifier.strip()
    # No need to check if modifier is "" because if there is no user input for modifier, defaults to +0 
    results.append(modifier)
    # isFudgeRoll is a bool value to see if there is a fudgeroll in the input, if there is, add to the results list 

    if not hasRollResult: 
        return "Input Error: Make sure that your input for roll is in the format xdy + m rollResult"
    if hasRollResult:
        fudgeVal = getFudgeValue(data)
        results.append(fudgeVal)
    else: 
        return "Input Error: Make sure that your input for roll is in the format xdy + m rollResult"
    # returning the value 
    return(results)
        

# """
# The function needed to add macros 
# This function is spacing sensative, so the user needs to include all the spaces needed 
# The input should be in the form die q mod name 
# """
def addMacro(args):
    arguments = " ".join(args)
    inputs = arguments.split(" ")
    if len(inputs) < 4: 
        msg1 = "You are missing some inputs needed for the addMacro function."
        msg2 = "Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        return result  
    else: 
        return inputs

# """
# The method needed to delete a macro. The input is just a name. As such we will only look at the first argument passed 
# """
def delMacro(arg):
    argument = "".join(arg)
    if argument == "": 
        return "To delete a macro, you must input the name of the macro you wish to delete"
    else: 
        return argument

def callMacro(arg):
    argument = "".join(arg)
    if argument == "": 
        return "To call a macro, you must input the name of the macro you wish to call"
    else: 
       return argument

def viewMacro():
    return "Called the View Macro Function."

def deleteMacros():
   return "Called the Delete Macro File Function."

def join(arg):
    result = []
    if len(arg) < 2:
        return "To join initiative, the input must be in the form: [name] [initiative roll]."
    else:
        name = " ".join(arg[:-1])
        initRoll = arg[-1]
        result.append(name)
        result.append(initRoll)
        return result
    
def begin():
    return "Begin function called"

def end():
    return "End function called"
      
def next():
    return "Next function called"

def prev():
    return "Previous function called"

def showTracker():
    return "Show function called"

def search(args):
    arguments = " ".join(args)
    inputs = arguments.split(" ")
    result = []
    if len(inputs) < 2: 
        msg1 = "You are missing some inputs needed for the search function."
        msg2 = "Make sure that you are inputing at least two key words to search. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        return result 
    else: 
        return inputs 

# Helper functions for the parsing of user inputs for roll and manual roll 

"""
Get side die gets called with an input of the user turned into a string 
We do spliting in different cases in order to get the side die 
The side die should always come after the d if the dice roll is in the format xdy. 
In the cases of the user putting a modifier, the roll will be in format xdy + m. 
    The y will be sandwitched between the +/- and d. we do the spliting accordingly 
"""
def getSideDie(data):
    if not("+" in data or "-" in data): 
        params = data.split("d")
        sideDie = params[1].strip()
        return sideDie
    if "+" in data:
        params = data.split("d")
        params = params[1].strip()
        params = params.split("+")
        sideDie = params[0].strip()
        return sideDie
    if "-" in data:
        params = data.split("d")
        params = params[1].strip()
        params = params.split("-")
        sideDie = params[0].strip()
        return sideDie

"""
we are getting passed the whole data string as the input to this funciton 
Case 1: If there is no + or - in string, there is no modifier so default to +0 
Case 2: There is a modifier and there is a fudgeRoll: call the getModifierWithFudge funciton 
Case 3: There is a modifier but no fudgeRoll: split on either + or - and return the item in the first position 
"""
def getModifier(data, hasFudgeRoll): 
    if not("+" in data or "-" in data):
        modifier = "+0"
        return modifier
    if hasFudgeRoll: 
        return getModifierWithFudge(data)
    if not(hasFudgeRoll):
        if "+" in data:  
            modifier = data.split("+")[1]
            modifier = modifier.strip()
            modifier = "+" + modifier
            return modifier
        if "-" in data:  
            modifier = data.split("-")[1]
            modifier = modifier.strip()
            modifier = "-" + modifier
            return modifier

"""
If there is a fudge roll, getting the modifier is slightly more complicated 
Still have to split by either + or - 
The modifier after the split shoud be in the first position while the fudgeroll is on the second position 
"""
def getModifierWithFudge(data):
    if "+" in data: 
        rightSide = data.split("+")[1]
        rightSide = rightSide.strip().split(" ")
        # If the length is 2, then there is something in the modifier roll slot 
        if len(rightSide) > 1: 
            rightSide[0] = rightSide[0].strip()
            return "+" + rightSide[0]
    if "-" in data: 
        rightSide = data.split("-")[1]
        rightSide = rightSide.strip().split(" ")
        # If the length is 2, then there is something in the modifier roll slot 
        if len(rightSide) > 1: 
            rightSide[0] = rightSide[0].strip()
            return "-" + rightSide[0]

"""
Helper function to check if the user input has a fudge roll 
If there is no + or - then no fudge roll, becasue we need a modifier for users to be able to use fudgeroll 
If there is a +or -, we do a split on it then the fudge roll should be in the second position of the resulting array 
"""
def hasFudge(data):
    if not("+" in data or "-" in data):
        return False 
    if "+" in data: 
        rightSide = data.split("+")[1]
        rightSide = rightSide.strip().split(" ")

        # if the length is 1, it is not a fudge roll 
        if len(rightSide) == 1:
            return False
        # If the length is 2, then there is something in the fudge roll slot 
        if len(rightSide) > 1: 
            return True 
    if "-" in data: 
        rightSide = data.split("-")[1]
        rightSide = rightSide.strip().split(" ")

        # if the length is 1, it is not a fudge roll 
        if len(rightSide) == 1:
            return False
        # If the length is 2, then there is something in the fudge roll slot 
        if len(rightSide) > 1: 
            return True 
"""
Getting the fudgeValue if there is a fudge roll 
Similar process as hasFudge, but instead of returning a bool, we return the value 
"""
def getFudgeValue(data): 
    if "+" in data: 
        rightSide = data.split("+")[1]
        rightSide = rightSide.strip().split(" ")
        # if the length is 1, it is not a fudge roll 
        # If the length is 2, then there is something in the fudge roll slot 
        if len(rightSide) > 1: 
            result = rightSide[1].strip()
            return result
    if "-" in data: 
        rightSide = data.split("-")[1]
        rightSide = rightSide.strip().split(" ")
        # if the length is 1, it is not a fudge roll 
        # If the length is 2, then there is something in the fudge roll slot 
        if len(rightSide) > 1: 
            result = rightSide[1].strip()
            return result