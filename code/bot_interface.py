# bot_interface.py

import os
import discord
from discord.ext import commands
import discord.ext
import random
import string
import re
from initTracker import *
import rolling
# import compendium

TOKEN = "NzU5MTk0MTEyNjQwODExMDI4.X258nQ.fiBtEZuY4kcs8oiCj7KM7r4mqaM"
client = discord.Client()

description = '''D&D Bot to Meet Your Needs'''
bot = commands.Bot(command_prefix='!', description=description)

#making the initiative tracker object 
tracker = InitTracker()

# First few functions are welcoming a user when they join the same server as the bot and other pure UI things 
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# here is where we will start the bot commands 
@bot.command()
async def hello(ctx):
    username = ctx.message.author
    await ctx.send("Hey " f"{username.mention}, lets play some D&D!")

@bot.command()
async def helpMe(ctx):
    msg = "Thank you for using our D&D bot!"
    msg2 = "Please refer to this git hub"
    await ctx.send("SOME MESSAGE TO HELP: maybe a link to github")

"""
The command that takes care most roling functions including multiroll, standard roll, and fudgerolling 
Standard roll takes in no inputs and calls the rolling funciton with no inputs 
Multiroll takes in the inputs xdy + modifier. the modifier is optional 
Fudgeroll takes in xdy + modifier fudgeroll. all are necessary for a fudge roll 
"""

@bot.command()
async def roll(ctx, *arg):
    results = []
    data = " ".join(arg)
    # spliting the input by a space 
    arg = data.split(" ")
    #returns a bool if the user inputed a fudge roll 
    isFudgeRoll = hasFudge(data)
    if data == "":
        await ctx.send("You called default roll, rolling a d20.")
        await ctx.send(rolling.multiroll())
        return 
    if len(arg) > 6: 
        await ctx.send("Too many inputs for the roll function. Make sure the form is in xdy +m.")
        return 
    #fudge roll will never be in arg[0] because it is space sensative 
    firstParam = arg[0]

    paramList = firstParam.split("d")
    if len(paramList) == 0:
        await ctx.send("You did not input the right amount of inputs. Make sure the inputs are in form xdy +m.")
        return 
    numDie = paramList[0]
    if numDie == "": 
        await ctx.send("Please input a value for the num of dice. Roll should be in format xdy +m where y is the number of sides of the die you want to roll. Please use help for more information.")
        return
    results.append(numDie)
 
    sideDie = getSideDie(data)
    if sideDie == "": 
        await ctx.send("Please input a value for the size of dice. Roll should be in format xdy +m where y is the number of sides of the die you want to roll. Please use help for more information.")
        return
    sideDie = sideDie.strip()
    results.append(sideDie)
     
    # call to the helper function to get the modifier 
    modifier = getModifier(data, isFudgeRoll)
    modifier = modifier.strip()
    results.append(modifier)
    # if the roll is a fudge roll, get the fudge roll value 
    if isFudgeRoll:
        fudgeVal = getFudgeValue(data)
        results.append(fudgeVal)

    # Sending results.
    if len(results) == 3:
        await ctx.message.delete()
        await ctx.send(f'{ctx.message.author.mention} ' + rolling.multiroll(results[1], results[0], results[2]))
    else:
        await ctx.message.delete()
        await ctx.send(f'{ctx.message.author.mention} ' + rolling.multiroll(results[1], results[0], results[2], results[3]))
    return 

          
"""
Rolling adv takes in one input: a bool: a true or a false statement 
"""
@bot.command()
async def rollAdv(ctx, arg = ""):
    if arg == "":
        await ctx.send("You need a input for this command. Please input a bool as an input for this function. A true or false statement. Refer to helpMe command for more information :).")
        return
    # note we are not checking the validity of the person's input here: the checks for the input is done in the rolling module. 
    # I just have to check that the user passed a input with roll adv 
    else: 
        await ctx.send("Called rollAdv with input: " + arg)
        # Sending results.
        await ctx.send(f'{ctx.message.author.mention} ' + rolling.rollAdv(arg))
        return 

"""
The function that takes care of manual rolls. we want to make sure that the format for manual rolls is the same as the one for normal rolls. 
As such, we will have almost all the similar checks as the ones used in roll 
"""
@bot.command()
async def mroll(ctx, *arg):
    results = []
    data = " ".join(arg)
    # spliting the input by a space 
    arg = data.split(" ")
    if data == "":
        await ctx.send("You cannot call manual roll with no inputs. Put in form xdy + m rollResult.")
        return 
    # reusing the hasFudge helper function to check to see if the user has a roll Result 
    # returns a bool if the user inputted a rollResult or not. sending data to the helper function 
    hasRollResult = hasFudge(data)
    if not hasRollResult: 
        await ctx.send("Input Error: Make sure that your input for roll is in the format xdy + m rollResult.")
        return 
    if not("d" in data):
        await ctx.send("Input Error: Make sure that your input for roll is in the format xdy + m rollResult.")
        return 
    # Even if everthing is spaced out with a rollResult, the max length of args is 6 
    if len(arg)>6:
        await ctx.send("Too many inputs for the manual roll function. Call helpMe for more info.")
        return 

    firstParam = arg[0]
    # spliting the first argument by "d"
    paramList = firstParam.split("d")
    if len(paramList) == 0:
        await ctx.send("Input Error: Make sure that your input for roll is in the format xdy + m rollResult.")
        return 
    numDie = paramList[0]
    if numDie == "": 
        await ctx.send("Please input a value for the number of dice. Roll should be in format xdy+m rollResult where x is number of dice you want to roll. Please use help for more information.")
        return 
    results.append(numDie)
    # Call to the helper function to get the side die 
    sideDie = getSideDie(data)
    # the case if they split x d y with spaces between each 
    if sideDie == "": 
        await ctx.send("Please input a value for the size of dice. Roll should be in format xdy +m rollResult where y is the number of sides of the die you want to roll. Please use help for more information.")
        return 
    
    sideDie = sideDie.strip()
    results.append(sideDie)
 
    # We are passing the whole string input to the helper function getModifier 
    modifier = getModifier(data, hasRollResult)
 
    # in case there is extra spaces in the modifier returned after the call to getModifier 
    modifier = modifier.strip()
    # No need to check if modifier is "" because if there is no user input for modifier, defaults to +0 
    results.append(modifier)
    # isFudgeRoll is a bool value to see if there is a fudgeroll in the input, if there is, add to the results list 
    rollVal = getFudgeValue(data)
    results.append(rollVal)
    # Sending results.
    await ctx.send(f'{ctx.message.author.mention} ' + rolling.manualRoll(results[1], results[0], results[2], results[3]))
        
# """
# The function needed to add macros 
# This function is spacing sensative, so the user needs to include all the spaces needed 
# The input should be in the form die q mod name 
# """

@bot.command()
async def addMacro(ctx, *args):
    arguments = " ".join(args)
    inputs = arguments.split(" ")
    # if the user did not put enough inputs, send an error message 
    if len(inputs) < 4: 
        await ctx.send("You are missing all of the inputs needed for the addMacro function.")
        await ctx.send("Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information.")
        return  
    else: 
        await ctx.send("Processing your request to addMacro")
        # Sending results.
        print(" ".join(args[3:]))
        await ctx.send(f'{ctx.message.author.mention} ' + rolling.addMacro(args[0], args[1], args[2], " ".join(args[3:])))

"""
The method needed to delete a macro. The input is just a name. 
The output is what is returned by the delMacro function 
"""
@bot.command()
async def delMacro(ctx, *arg):
    argument = " ".join(arg)
    # need to have the name of the macro user wants to delete 
    if argument == "": 
        await ctx.send("To delete a macro, you must input the name of the macro you wish to delete.")
        return  
    else: 
        await ctx.send("Attempting to delete the macro with the name: " + argument)
        # Sending results.
        await ctx.send(f'{ctx.message.author.mention} ' + rolling.delMacro(argument))

"""
The method needed to call a macro. The input is just a name. 
The output is what is returned by the callMacro function 
"""     
@bot.command()
async def callMacro(ctx, *arg):
    argument = " ".join(arg)
    # cannot call a macro with no name 
    if argument == "": 
        await ctx.send("To call a macro, you must input the name of the macro you wish to call.")
        return  
    else: 
        # Delete once debugging is complete.
        await ctx.send("Attempting to call the macro with the name: " + argument)
        # Sending results.
        await ctx.send(f'{ctx.message.author.mention} ' + rolling.callMacro(argument))

"""
A method used to view the macros the users have stored in the csv file 
No inputs. The output is what is sent by the viewMacro function in the rolling module 
"""
@bot.command()
async def viewMacros(ctx):
    await ctx.send(rolling.viewMacros())

"""
Method used to delete the file that stores the macros that the users have created. 
"""
@bot.command()
async def deleteMacros(ctx):
    await ctx.send(rolling.deleteMacroFile())

"""
Method used to call the initive tracker join function 
Inputs need to be the name and the initive roll 
"""
@bot.command()
async def join(ctx, *arg):
    # missing the necessary arguments to join 
    if len(arg) < 2:
        await ctx.send("To join initiative, the input must be in the form: [name] [initiative roll].")
    else:
        username = ctx.message.author
        name = " ".join(arg[:-1])
        initRoll = arg[-1]

        msg = tracker.join(username, name, initRoll)
        await ctx.send(username.mention + " " + msg)

"""
Method used to start the initive tracker 
Takes no inputs 
"""
@bot.command()
async def begin(ctx):
    msg = tracker.begin()
    username = tracker.trackerInfo[tracker.currentPlayer][0]
    await ctx.send(username.mention + "\n" + msg)

"""
Method used to end the initive tracker 
Takes no inputs 
"""
@bot.command()
async def end(ctx):
    msg = tracker.end()
    await ctx.send(msg)

"""
Method used to call next on the initive tracker 
Takes no inputs 
"""
@bot.command()
async def next(ctx):
    msg = tracker.next()
    username = tracker.trackerInfo[tracker.currentPlayer][0]
    await ctx.send(username.mention + "\n" + msg)

"""
Method used to call previous on the initive tracker 
Takes no inputs 
"""
@bot.command()
async def prev(ctx):
    msg = tracker.prev()
    username = tracker.trackerInfo[tracker.currentPlayer][0]
    await ctx.send(username.mention + "\n" + msg)

"""
Method used to show initive tracker 
Takes no inputs 
"""
@bot.command()
async def show(ctx):
    msg = tracker.printTracker()
    await ctx.send(msg)

"""
Method used to search  
Takes in an input of at least two keywords. Returns the result of the search into the chat 
"""
@bot.command()
async def search(ctx, *args):
    arguments = " ".join(args)
    inputs = arguments.split(" ")
    if len(inputs) < 2: 
        await ctx.send("You are missing all of the inputs needed for the search function.")
        await ctx.send("Make sure that you are inputing two key words to search. Refer to helpMe command for more information.")
        return  
    else: 
        await ctx.send("Processing your search request")
        await ctx.send(inputs)
        return 

# Helper functions for the parsing of user inputs for roll and manual roll 

"""
Get side die gets called with an input of the user turned into a string 
We do spliting in different cases in order to get the side die 
The side die should always come after the d if the dice roll is in the format xdy. 
In the cases of the user putting a modifier, the roll will be in format xdy + m. 
    The y will be sandwitched between the +/- and d. we do the spliting accordingly 
"""
def getSideDie(data):
    # if the user did not put a modifier 
    if not("+" in data or "-" in data): 
        params = data.split("d")
        sideDie = params[1].strip()
        return sideDie
    # positive modifier
    if "+" in data:
        params = data.split("d")
        params = params[1].strip()
        params = params.split("+")
        sideDie = params[0].strip()
        return sideDie
    # negative modifier 
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
Case 3: There is a modifier but no fudgeRoll: split on either + or - and return the item in the first position without the spaces 
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

bot.run(TOKEN)

