
# This is a file that has copied all of the code from the actual bot interface code, however, for testing sake, 
# instead of making the bot listen to messages from chat, the functions are changed to allow for string inputs 
# and thus we can check correctness of the functions automatically using python unittesting 

def helpMe(): 
    return "SOME MESSAGE TO HELP: maybe a link to github"

def roll(arg):
    arguments = "".join(arg)
    print("this is new")
    results = []
    fudgeRoll = "Temp String"
    #this is the default roll 
    if arguments == "":
        return "You called default roll, rolling a d20"
    elif not("d" in arguments):
        return "Input Error: Make sure that your input for roll is in the format xdy + m"
    else: 
        elementList = arguments.split(" ")
        numDie = elementList[0].split("d")[0]
        if numDie == "":
            return "Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information"
        else:
            results.append(numDie)
        
        # this case is to take care of when user just passes in xdy 
        if len(elementList) == 1: 
            sideDie = elementList[0].split("d")[1]
        elif len(elementList) == 2: 
            if (not elementList[0].endswith("+")) and (not elementList[0].endswith("-")):
                if not ("+" in elementList[1]):
                    fudgeRoll = elementList[1]
        elif len(elementList) == 3:
            if elementList[1] != "+":
                fudgeRoll = elementList[2]
        elif len(elementList) == 4:
            fudgeRoll = elementList[3]
        # if there is a fudge roll, remove it 
        if arguments.endswith(fudgeRoll):
            arguments = arguments[:-(len(fudgeRoll))]

        arguments = arguments.split("d")
        modifier = "+0"
        numDie = arguments[0]
        if "+" in arguments[1]:
            sideDie = arguments[1].split("+")[0]
            if sideDie == " " or sideDie == "":
                return "Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information"
            modifier = "".join(arguments[1].split("+")[1:])
            if modifier == "" or modifier == " ":
                # You inputed no modifier after the +, defaulted to modifier +0
                modifier = "+0"
            modifier = "+" + "".join(arguments[1].split("+")[1:])
        elif "-" in arguments[1]:
            sideDie = arguments[1].split("-")[0]
            if sideDie == " " or sideDie == "":
                return "Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information"
            modifier = "".join(arguments[1].split("-")[1:])
            if modifier == "" or modifier == " ":
                # You inputed no modifier after the +, defaulted to modifier +0
                modifier = "+0"
            print("this is modifier:")
            print("".join(arguments[1].split("-")[1:]))
            modifier = "-" + "".join(arguments[1].split("-")[1:])
        
        sideDie = "".join(sideDie.split())
        modifier = "".join(modifier.split())
        results.append(sideDie)
        results.append(modifier)
        if fudgeRoll != "Temp String":
            results.append(fudgeRoll)
        return results
"""
Rolling adv takes in one input: a bool: a true or a false statement 
"""
def rollAdv(arg):
    if arg == "":
        return "You need a input for this command. Please input a bool as an input for this function. A true or false statement. Refer to helpMe command for more information :)"
    # note we are not checking the validity of the person's input here: the checks for the input is done in the rolling module. 
    # I just have to check that the user passed a input with roll adv 
    else: 
        return "Called rollAdv with input: " + arg

# """
# The function that takes care of manual rolls. we want to make sure that the format for manual rolls is the same as the one for normal rolls. 
# As such, we will have almost all the similar checks as the ones used in roll 
# """
def mRoll(args):
     arguments = " ".join(args)
     results = []
     if arguments == "": 
        return "Not Valid. You called manual roll with no inputs. Manual roll needs to be in the format xdy + modifier. Refer to helpMe for more information :)"
     elif not ("d" in arguments):
        return "Input Error: Make sure that your input for roll is in the format xdy + m"
     else: 
        arguments = arguments.split("d")
        modifier = "+0"
        numDie = arguments[0]
        if numDie == "":
            return "Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information"
        results.append(numDie)
        if "+" in arguments[1]:
            sideDie = arguments[1].split("+")[0]
            if sideDie == " ":
                return "Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information"
            modifier = arguments[1].split("+")[1]
            if modifier == "":
                # "You inputed no modifier after the +, defaulted to modifier +0"
                modifier = "+0"
            modifier = "+" + arguments[1].split("+")[1]
        elif "-" in arguments[1]:
            sideDie = arguments[1].split("-")[0]
            if sideDie == " ":
                return "Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information"
            modifier =  arguments[1].split("-")[1]
            if modifier == "":
                # "You inputed no modifier after the -, defaulted to modifier +0")
                modifier = "+0"
            modifier = "-" + arguments[1].split("-")[1]
        sideDie = "".join(sideDie.split())
        modifier = "".join(modifier.split())
        results.append(sideDie)
        results.append(modifier)
        print(results)
        return results 
        

# """
# The function needed to add macros 
# This function is spacing sensative, so the user needs to include all the spaces needed 
# The input should be in the form die q mod name 
# """
def addMacro(args):
     arguments = " ".join(args)
     inputs = arguments.split(" ")
     if len(inputs) < 4: 
        msg1 = "You are missing all of the inputs needed for the addMacro function."
        msg2 = "Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        return result  
     elif len(inputs) > 4: 
        msg1 = "You have too many inputs for the funciton addMacro."
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
      return "End function is called"
      
def next():
    return "Next function is called"

def prev():
    return "Previous function is called"

def showTracker():
    return "Show function is called"

def search(ctx, *args):
    arguments = " ".join(args)
    inputs = arguments.split(" ")
    result = []
    if len(inputs) < 2: 
        msg1 = "You are missing all of the inputs needed for the search function."
        msg2 = "Make sure that you are inputing two key words to search. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        return result 
    elif len(inputs) > 2: 
        msg1 = "You have too many inputs for the funciton search."
        msg2 = "We are using your first two keywords to perform the search. Refer to helpMe command for more information"
        result.append(inputs[0])
        result.append(inputs[1]) 
        return result
    else: 
        result.append(inputs[0])
        result.append(inputs[1]) 
        return result

# # the simple diceroller
# def diceRoll(x):
#     return random.randint(1,x)
