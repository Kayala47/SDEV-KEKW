# bot_interface.py

import os
import discord
from discord.ext import commands
import discord.ext
import random
import string
import re


TOKEN = "NzU5MTk0MTEyNjQwODExMDI4.X258nQ.A4YJfVztgI-qgTQQfhxzLxFDJyI"
client = discord.Client()

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
[5, 20+5]
@bot.command()
async def roll(ctx, *arg):
     arguments = "".join(arg)
     if arguments == "": 
          await ctx.send("You called default roll, rolling a d20")
     arguments = arguments.split("d")
     modifier = "+0"
     numDie = arguments[0]
     if numDie == "":
          await ctx.send("Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information")
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
     await ctx.send("Your inputs: " + numDie + " " + sideDie + " " + modifier)

@bot.command()
async def froll(ctx):
     arguments = " ".join(arg)
     if arguments == "": 
          await ctx.send("You called default roll, rolling a d20")
     arguments = arguments.split("d")
     modifier = "+0"
     numDie = arguments[0]
     if numDie == " ":
          await ctx.send("Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information")
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
     elif "-" in arguments[1]:
          sideDie = arguments[1].split("-")[0]
          if sideDie == " ":
               await ctx.send("Please input a value for the side of dice. Roll should be in format xdy+m where y is the number of sides of the die you want to roll. Please use help for more information")
               pass
          modifier =  arguments[1].split("-")[1]
          if modifier == "":
               await ctx.send("You inputed no modifier after the -, defaulted to modifier +0")
               modifier = "+0"
     await ctx.send("Your inputs: " + numDie + " " + sideDie + " " + modifier)

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

bot.run("NzU5MTk0MTEyNjQwODExMDI4.X258nQ.A4YJfVztgI-qgTQQfhxzLxFDJyI")
client.run("NzU5MTk0MTEyNjQwODExMDI4.X258nQ.A4YJfVztgI-qgTQQfhxzLxFDJyI")
