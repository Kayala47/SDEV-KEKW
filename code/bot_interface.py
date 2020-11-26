# bot_interface.py

import os
import discord
from discord.ext import commands
import discord.ext
import random
import string
import re
# import initTracker

"""
Chnages that need to be made: 
the addMacro cannot check for each individual inputs as we do not know which input the user was trying to make. SO we now just have one error that 
says that the user does not have all of the correct inputs. same for the join, we cannot be certain of what filed the users were missing so we will 
just have one error. Same for search, we cannot tell which key word is missing 
"""

TOKEN = "TOKEN"

description = '''D&D Bot to Meet Your Needs'''
bot = commands.Bot(command_prefix='!', description=description)

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
     # we are going to check if it is a fudge roll here, and do approate actions 
     elementList = arguments.split(" ")
     if len(elementList) == 2: 
        if not elementList[0].endswith("+") or not elementList[0].endswith("-"):
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
     if numDie == "":
        await ctx.send("Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information")
        pass
     results.append(numDie)
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
     if fudgeRoll != "Temp String":
        results.append(fudgeRoll)
     print(results)
     await ctx.send(results)
     
@bot.command()
async def rollAdv(ctx):
     await ctx.send("")

@bot.command()
async def mRoll(ctx, *args):
     await ctx.send("")

@bot.command()
async def addMacro(ctx):
     await ctx.send("")

@bot.command()
async def delMacro(ctx):
     await ctx.send("")

@bot.command()
async def callMacro(ctx):
     await ctx.send("")

@bot.command()
async def join(ctx):
     await ctx.send("")

@bot.command()
async def begin(ctx):
     await ctx.send("")

@bot.command()
async def end(ctx):
     await ctx.send("")

@bot.command()
async def search(ctx):
     await ctx.send("")

# the simple diceroller
def diceRoll(x):
    return random.randint(1,x)

bot.run(TOKEN)

