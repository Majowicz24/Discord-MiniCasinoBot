import discord 
import random
from discord.ext import commands
from gameConfig import *
import os

coin = [0, 1]

@bot.command()
async def coinflip(ctx):
        embed = discord.Embed(
            title = "Coinflip💰",
            description = 'React with the emoji below to choose heads or tails \nHeads: 💸 \nTails: 🦨',
            color = discord.Color.gold(),
        )
        await ctx.channel.purge(limit=5)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('💸')
        await msg.add_reaction('🦨')

        def checkReaction(reaction, user):
            return user != bot.user and (str(reaction.emoji) == '💸' or str(reaction.emoji) == '🦨')
        reaction, user = await bot.wait_for("reaction_add", check = checkReaction)

        #Heads roll
        if str(reaction.emoji) == '💸':
            await ctx.send("You chose *Heads*, good luck! Flipping....")
            if random.choice(coin) == 0:
                await ctx.send("Coin lands on **Heads**")
                await ctx.send("Congrats! You win!!🏆 (Use **-reset** to leave game)")
            elif random.choice(coin) == 1:
                await ctx.send("Coin lands on **Tails**")
                await ctx.send("Sorry, you lost💩 (Use **-reset** to leave game)")

        #Tails roll
        elif str(reaction.emoji) == '🦨':
            await ctx.send("You chose *Tails*, good luck! Flipping....")
            if random.choice(coin) == 1:
                await ctx.send("Coin lands on **Tails**")
                await ctx.send("Congrats! You win!!🏆 (Use **-reset** to leave game)")
            elif random.choice(coin) == 0:
                await ctx.send("Coin lands on **Heads**")
                await ctx.send("Sorry, you lost💩 (Use **-reset** to leave game)")

@bot.command()
async def reset(ctx):
    await ctx.send("Resetting files...use **-menu** for the game menu")
    os.system('python startup.py')
    pass

bot.run(TOKEN, bot=True, reconnect=True)
client.run(TOKEN)
