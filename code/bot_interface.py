# bot_interface.py

import os
import discord
from discord.ext import commands
import discord.ext
import random
import string
import re
from initTracker import *

"""
Chnages that need to be made: 
the addMacro cannot check for each individual inputs as we do not know which input the user was trying to make. SO we now just have one error that 
says that the user does not have all of the correct inputs. same for the join, we cannot be certain of what filed the users were missing so we will 
just have one error. Same for search, we cannot tell which key word is missing. 
We decided to remove the emoji listener as calling the next and other things were easier 
"""

TOKEN = "NzU5MTk0MTEyNjQwODExMDI4.X258nQ.d1wBbHBr_QdyCg7Zun3eTUmRlyI"
client = discord.Client()

description = '''D&D Bot to Meet Your Needs'''
bot = commands.Bot(command_prefix='!', description=description)
tracker = InitTracker()

# First few functions are welcoming a user when they join the same server as the bot and other pure UI things 
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# here is where we will start the bot commands 
@bot.command()
async def hello(ctx):
     await ctx.send("Hey Stranger, lets play some D&D")

@bot.command()
async def helpMe(ctx):
     await ctx.send("SOME MESSAGE TO HELP: maybe a link to github")

@bot.command()
async def test(ctx, *arg):
     await ctx.send(arg)

"""
the command that takes care most roling functions including multiroll, standard roll, and fudgerolling 
Standard roll takes in no inputs and calls the rolling funciton with no inputs 
Multiroll takes in the inputs xdy + modifier. the modifier is optional 
Fudgeroll takes in xdy + modifier fudgeroll. all are necessary for a fudge roll 
"""

@bot.command()
async def roll(ctx, *arg):
     arguments = " ".join(arg)
     results = []
     fudgeRoll = "Temp String"
     # this is the default call 
     if arguments == "": 
        await ctx.send("You called default roll, rolling a d20")
        pass 
     elif not("d" in arguments):
        await ctx.send("Input Error: Make sure that your input for roll is in the format xdy + m")
        pass
     else: 
        elementList = arguments.split(" ")
        numDie = elementList[0].split("d")[0]
        if numDie == "":
            await ctx.send("Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information")
            pass
        results.append(numDie)
        # this case takes care of if the user just passses in xdy 
        if len(elementList) == 1: 
            sideDie = elementList[0].split("d")[1]

        # we are going to check if it is a fudge roll here, and do approate actions 
        if len(elementList) == 2: 
            if not elementList[0].endswith("+") and not elementList[0].endswith("-"):
                if not ("+" in elementList[1]):
                    print("I got here")
                    fudgeRoll = elementList[1]
        elif len(elementList) == 3:
            if elementList[1] != "+":
                fudgeRoll = elementList[2]
        elif len(elementList) == 4:
            fudgeRoll = elementList [3]
        # if there is a fudge roll, remove it from the argument string 
        if arguments.endswith(fudgeRoll):
            arguments = arguments[:-(len(fudgeRoll))]

        arguments = arguments.split("d")
        modifier = "+0"
        numDie = arguments[0]
        if "+" in arguments[1]:
            sideDie = arguments[1].split("+")[0]
            if sideDie == " ":
                await ctx.send("Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information")
                pass
            modifier = ''.join(arguments[1].split("+")[1:])
            if modifier == "":
                await ctx.send("You inputed no modifier after the +, defaulted to modifier +0")
                modifier = "+0"
            modifier = "+" + ''.join(arguments[1].split("+")[1:])
        elif "-" in arguments[1]:
            sideDie = arguments[1].split("-")[0]
            if sideDie == " ":
                await ctx.send("Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information")
                pass
            modifier =  arguments[1].split("-")[1:]
            if modifier == "":
                await ctx.send("You inputed no modifier after the -, defaulted to modifier +0")
                modifier = "+0"
            modifier = "-" + ''.join(arguments[1].split("-")[1:])

        sideDie = "".join(sideDie.split())
        modifier = "".join(modifier.split())
        results.append(sideDie)
        results.append(modifier)
        if fudgeRoll != "Temp String":
            results.append(fudgeRoll)
        await ctx.send(results)
        pass 
     
          
"""
Rolling adv takes in one input: a bool: a true or a false statement 
"""
@bot.command()
async def rollAdv(ctx, arg):
    if arg == "":
        await ctx.send("You need a input for this command. Please input a bool as an input for this function. A true or false statement. Refer to helpMe command for more information :)")
        pass
    # note we are not checking the validity of the person's input here: the checks for the input is done in the rolling module. 
    # I just have to check that the user passed a input with roll adv 
    else: 
        await ctx.send("Called rollAdv with input: " + arg)

"""
The function that takes care of manual rolls. we want to make sure that the format for manual rolls is the same as the one for normal rolls. 
As such, we will have almost all the similar checks as the ones used in roll 

This function needs to get fixed
"""
@bot.command()
async def mRoll(ctx, *args):
     arguments = " ".join(args)
     results = []
     rollResult = "Temp String"
     if arguments == "": 
          await ctx.send("Not Valid. You called manual roll with no inputs. Manual roll needs to be in the format xdy + modifier. Refer to helpMe for more information :)")
     elif not ("d" in arguments):
        await ctx.send("Input Error: Make sure that your input for roll is in the format xdy + m rollResult")
        pass 
     else: 
        elementList = arguments.split(" ")
        numDie = elementList[0].split("d")[0]
        if numDie == "":
            await ctx.send("Please input a value for the number of dice. Roll should be in format xdy+m rollResult where x is number of dice you want to roll. Please use help for more information")
            pass
        results.append(numDie)
        # the case where they just pass in xdy 
        if len(elementList) == 1: 
            await ctx.send("Input Error: Make sure that your input for roll is in the format xdy + m rollResult")
            pass 
        


        if "+" in arguments[1]:
            sideDie = arguments[1].split("+")[0]
            if sideDie == " ":
                await ctx.send("Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information")
                pass
            modifier = arguments[1].split("+")[1]
            if modifier == "":
                await ctx.send("You inputed no modifier after the +, defaulted to modifier +0")
                modifier = "+0"
            modifier = "+" + arguments[1].split("+")[1]
        elif "-" in arguments[1]:
            sideDie = arguments[1].split("-")[0]
            if sideDie == " ":
                await ctx.send("Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information")
                pass
            modifier =  arguments[1].split("-")[1]
            if modifier == "":
                await ctx.send("You inputed no modifier after the -, defaulted to modifier +0")
                modifier = "+0"
            modifier = "-" + arguments[1].split("-")[1]
        sideDie = "".join(sideDie.split())
        modifier = "".join(modifier.split())
        results.append(sideDie)
        results.append(modifier)
        print(results)
        await ctx.send(results)
        

"""
The function needed to add macros 
This function is spacing sensative, so the user needs to include all the spaces needed 
The input should be in the form die q mod name 
"""
@bot.command()
async def addMacro(ctx, *args):
     arguments = " ".join(args)
     inputs = arguments.split(" ")
     if len(inputs) < 4: 
        await ctx.send("You are missing all of the inputs needed for the addMacro function.")
        await ctx.send("Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information")
        pass 
     elif len(inputs) > 4: 
         await ctx.send("You have too many inputs for the funciton addMacro.")
         await ctx.send("Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information")
         pass 
     else: 
         await ctx.send("Processing your request to addMacro")
         await ctx.send(inputs)

"""
The method needed to delete a macro. The input is just a name. As such we will only look at the first argument passed 
"""
@bot.command()
async def delMacro(ctx, arg):

    argument = "".join(arg)

    if argument == "": 
        await ctx.send("To delete a macro, you must input the name of the macro you wish to delete")
        pass 
    else: 
        await ctx.send("Attempting to delete the macro with the name: " + argument)

@bot.command()
async def callMacro(ctx, arg):
    argument = "".join(arg)

    if argument == "": 
        await ctx.send("To call a macro, you must input the name of the macro you wish to call")
        pass 
    else: 
        await ctx.send("Attempting to call the macro with the name: " + argument)

@bot.command()
async def join(ctx, *arg):
    if len(arg) < 2:
        await ctx.send("To join initiative, the input must be in the form: [name] [initiative roll].")
    else:
        username = ctx.message.author
        name = " ".join(arg[:-1])
        initRoll = arg[-1]

        msg = tracker.join(username, name, initRoll)
        await ctx.send(username.mention + " " + msg)

@bot.command()
async def begin(ctx):
    msg = tracker.begin()
    await ctx.send(msg)

@bot.command()
async def end(ctx):
    msg = tracker.end()
    await ctx.send(msg)

@bot.command()
async def next(ctx):
    msg = tracker.next()
    username = tracker.trackerInfo[tracker.currentPlayer][0]
    await ctx.send(username.mention + "\n" + msg)

@bot.command()
async def prev(ctx):
    msg = tracker.prev()
    username = tracker.trackerInfo[tracker.currentPlayer][0]
    await ctx.send(username.mention + "\n" + msg)

@bot.command()
async def show(ctx):
    msg = tracker.printTracker()
    await ctx.send(msg)

@bot.command()
async def search(ctx, *args):
     arguments = " ".join(args)
     inputs = arguments.split(" ")
     result = []
     if len(inputs) < 2: 
        await ctx.send("You are missing all of the inputs needed for the search function.")
        await ctx.send("Make sure that you are inputing two key words to search. Refer to helpMe command for more information")
        pass 
     elif len(inputs) > 2: 
         await ctx.send("You have too many inputs for the funciton search.")
         await ctx.send("We are using your first two keywords to perform the search. Refer to helpMe command for more information")
         result.append(inputs[0])
         result.append(inputs[1]) 
         await ctx.send(result)
         pass 
     else: 
         await ctx.send("Processing your search request")
         result.append(inputs[0])
         result.append(inputs[1]) 
         await ctx.send(result)
         pass

# the simple diceroller
def diceRoll(x):
    return random.randint(1,x)

bot.run(TOKEN)

