#Connecting to Discord.#
import discord
import colorscript as cs
import newton
from discord.ext import commands
import TopperBot as tb
import random
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "**********"
desc = '''Access spreadsheets and also get some fashionframe done, I guess.'''
bot = commands.Bot(command_prefix="|", description=desc)

@bot.event
async def on_ready():
    print("logged in as: ")
    print(bot.user.name)
    print(bot.user.id)
    print("_-`-_")

#Test command; delete later.
@bot.command()
async def fetch(ctx, arg1, arg2):
    await ctx.send("hey buddy {} and {}".format(arg1,arg2))

@bot.command()
async def whohas(ctx, arg1, arg2):
    await ctx.send("processing")
    results = tb.findusers(arg1, arg2)
    await ctx.send(results)
    await ctx.send("placeholder")

#Accept two players. First argument is room code.
#Up to two lobbies available.
@bot.command()
async def newton(ctx):
    await ctx.send("this command is still being programmed. sit tight.")
    #There needs to allow for a chain of commands to keep the game running.
    #Accept two player IDs in.
    #Check to make sure the right player is inputting a command.
    #Make sure they're not going out of turn.
    #Allow admin or moderator to cancel the game.
    #Otherwise, only one of two of those players can cancel the game.
    #Game will auto-wipe after 24 hours of no input.
    
@bot.command()
async def similarcolor(ctx, arg1, arg2, arg3):
    #Replace this with a reaction to the command.
    if (int(arg2) > 50):
        await ctx.send("you can't do that.")
    else:
        await ctx.send("searching...")
        results = cs.findcolor(arg1, int(arg2), arg3)
        await ctx.send(results)
        await ctx.send("done.")
    
#This was commented out for some reason.
@bot.command
async def on_message(message):
    #Bot doesn't reply to self.
    if message.author == bot.user:
        return

    if message.content.startswith("|test"):
        msg = "what is up matey {0.author.mention}".format(message)
        await bot.send_message(message.channel, msg)

    if message.content.startswith("|echo"):
        await bot.send_message(message.channel, message.content)
    
bot.run(TOKEN)