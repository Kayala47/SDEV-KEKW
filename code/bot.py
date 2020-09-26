# bot.py
import os
import discord
from discord.ext import commands
import random
import string
import re

TOKEN = "NzU5MTk0MTEyNjQwODExMDI4.X258nQ.s-WVF5ohZ3Z8tpo0VBGMeOTD09Y"
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, we were waiting for you!'
    )

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!roll'):
        msg = diceRoll(6)
        await message.channel.send(msg)

def diceRoll(x):
    return random.randint(1,x)

client.run("NzU5MTk0MTEyNjQwODExMDI4.X258nQ.s-WVF5ohZ3Z8tpo0VBGMeOTD09Y")
