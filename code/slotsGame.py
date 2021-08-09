import discord
import random
from discord.ext import commands
from gameConfig import *
import os

tokens = 15

@bot.command(pass_context=True)
async def slots(ctx):
    
    global tokens
    global slotMachine

    embed = discord.Embed(
        title = "Slots, Baby!🎰",
        description = 'Welcome to slots! React with ❓ for your balance/winning conditions, 🎰 to run some slots, and 🏳️ to reset the game and return to the main menu.',
        color = discord.Color.gold(),
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('❓')
    await msg.add_reaction('🎰')
    await msg.add_reaction('🏳️')



    def checkReaction(reaction, user):
        return user != bot.user and (str(reaction.emoji) == '❓' or str(reaction.emoji) == '🎰' or str(reaction.emoji) == '🏳️')
    reaction, user = await bot.wait_for("reaction_add", check = checkReaction)

    if str(reaction.emoji) == '❓':
        await ctx.send('It costs 5 tokens to play slots. You currently have ' + str(tokens) + ' tokens.')
        await ctx.send('Horizontal or diagonal rows of 7s land you a jackpot of +20 tokens!')
        await ctx.send('Landing a money bag grants grants you +1 token per bag!')
        await ctx.send('Horizontal or diagonal rows of Ladybugs grants +5 tokens!')

    elif str(reaction.emoji) == '🎰':

        if tokens >= 5:

            tokens = tokens - 5

            values = ['7️⃣', '❌', '💰', '🐞']

            pot = '7️⃣'
            cash = '💰'
            bug = '🐞'

            x1 = random.choice(values)
            x2 = random.choice(values)
            x3 = random.choice(values)
            x4 = random.choice(values)
            x5 = random.choice(values)
            x6 = random.choice(values)
            x7 = random.choice(values)
            x8 = random.choice(values)
            x9 = random.choice(values)

            slotMachine =[x1, x2, x3,
                    x4, x5, x6,
                    x7, x8, x9]

            line = ""
            for x in range(len(slotMachine)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + slotMachine[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + slotMachine[x]

            #the winning conditions:
            if x1 == pot and x2 == pot and x3 == pot:
                tokens = tokens + 20
            if x4 == pot and x5 == pot and x6 == pot:
                tokens = tokens + 20
            if x7 == pot and x8 == pot and x9 == pot:
                tokens = tokens + 20
            if x1 == pot and x5 == pot and x9 == pot:
                tokens = tokens + 20
            if x3 == pot and x5 == pot and x7 == pot:
                tokens = tokens + 20
            if x1 == pot and x4 == pot and x7 == pot:
                tokens = tokens + 20
            if x2 == pot and x5 == pot and x8 == pot:
                tokens = tokens + 20
            if x3 == pot and x6 == pot and x9 == pot:
                tokens = tokens + 20
            if x1 == cash:
                tokens = tokens + 1
            if x2 == cash:
                tokens = tokens + 1
            if x3 == cash:
                tokens = tokens + 1
            if x4 == cash:
                tokens = tokens + 1
            if x5 == cash:
                tokens = tokens + 1
            if x6 == cash:
                tokens = tokens + 1
            if x7 == cash:
                tokens = tokens + 1
            if x8 == cash:
                tokens = tokens + 1
            if x9 == cash:
                tokens = tokens + 1
            if x1 == bug and x2 == bug and x3 == bug:
                tokens = tokens + 5
            if x4 == bug and x5 == bug and x6 == bug:
                tokens = tokens + 5
            if x7 == bug and x8 == bug and x9 == bug:
                tokens = tokens + 5
            if x1 == bug and x5 == bug and x9 == bug:
                tokens = tokens + 5
            if x3 == bug and x5 == bug and x7 == bug:
                tokens = tokens + 5
            if x1 == bug and x4 == bug and x7 == bug:
                tokens = tokens + 5
            if x2 == bug and x5 == bug and x8 == bug:
                tokens = tokens + 5
            if x3 == bug and x6 == bug and x9 == bug:
                tokens = tokens + 5
        
        elif tokens <= 5:
            await ctx.send("Sorry you ran out of tokens, reset the game to play again!")

    elif str(reaction.emoji) == '🏳️':
        await ctx.send("Resetting files...use **-menu** for the game menu")
        os.system('python startup.py')
        pass



bot.run(TOKEN, bot=True, reconnect=True)
client.run(TOKEN)
