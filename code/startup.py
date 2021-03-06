import discord 
import random
from discord.ext import commands
import datetime
from datetime import datetime
from discord.utils import get
import os
from gameConfig import *


@bot.command(pass_context=True)
async def tips(ctx):
        embed0 = discord.Embed(
            title = "Commandsπ»",
            description = '**-tips**: where you are now \n **-menu**: opens the start menu to select games \n **-reset**: brings players back to start menu',
            url = 'https://github.com/',
            color = discord.Color.red(),
            timestamp = datetime.now()
        )
        await ctx.channel.purge(limit=3)
        msg = await ctx.send(embed=embed0)
    
#game menu = users can select what type of game to play by reacting to the emojis
@bot.command(pass_context=True)
async def menu(ctx):
        embed1 = discord.Embed(
            title = "MiniCasinoBot",
            description = 'React with π² to start a LRC game \n React with π° to start a Coinflip game \n React with π to start a Simple Blackjack game \n React with π° to start a Slots game \n React with π to start a Race game',
            url = 'https://github.com/',
            color = discord.Color.teal(),
            timestamp = datetime.now()
        )
        await ctx.channel.purge(limit=3)
        msg = await ctx.send(embed=embed1)
        #Game Selection Menu
        await msg.add_reaction('π²')
        await msg.add_reaction('π°')
        await msg.add_reaction('π') 
        await msg.add_reaction('π°')
        await msg.add_reaction('π')

        def checkReaction(reaction, user):
            return user != bot.user and (str(reaction.emoji) == 'π²' or str(reaction.emoji) == 'π°' or str(reaction.emoji) == 'π' or str(reaction.emoji) == 'π°' or str(reaction.emoji) == 'π')
        reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check = checkReaction)

        #LRC Game Menu
        if str(reaction.emoji) == 'π²':
            embed2 = discord.Embed(
                title = "Welcome to Left, Right, Center!",
                description = 'React to a number below to select the amount of players',
                color = discord.Color.purple()
            )
            await ctx.channel.purge(limit=3)
            msg = await ctx.send(embed=embed2)
            await msg.add_reaction('3οΈβ£')
            await msg.add_reaction('4οΈβ£')
            await msg.add_reaction('5οΈβ£')
            await msg.add_reaction('6οΈβ£')

            def checkLRCReaction(reaction, user):
                return user != bot.user and (str(reaction.emoji) == '3οΈβ£' or str(reaction.emoji) == '4οΈβ£' or str(reaction.emoji) == '5οΈβ£' or str(reaction.emoji) == '6οΈβ£')
            reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check = checkLRCReaction)

            #Selecting the amount of players for LRC Game:
            if str(reaction.emoji) == '3οΈβ£':
                await ctx.send("Game 3 will now start...")
                await ctx.send("Use **-LRC** and @ yourself with 2 other players to start the game")
                os.system('python LRCThree.py')
                pass
            elif str(reaction.emoji) == '4οΈβ£':
                await ctx.send("Game 4 will now start...")
                await ctx.send("Use **-LRC** and @ yourself with 3 other players to start the game")
                os.system('python LRCFour.py')
                pass
            elif str(reaction.emoji) == '5οΈβ£':
                await ctx.send("Game 5 will now start...")
                await ctx.send("Use **-LRC** and @ yourself with 4 other players to start the game")
                os.system('python LRCFive.py')
                pass
            elif str(reaction.emoji) == '6οΈβ£':
                await ctx.send("Game 6 will now start...")
                await ctx.send("Use **-LRC** and @ yourself with 5 other players to start the game")
                os.system('python LRCSix.py')
                pass

        #Coinflip Game
        elif str(reaction.emoji) == 'π°':
            await ctx.send("Coinflip game will now start...")
            await ctx.send("Use **-coinflip** to start the game")
            os.system('python coinflipGame.py')
            pass

        #Blackjack Game
        elif str(reaction.emoji) == 'π':
            await ctx.send("Blackjack game will now start...")
            await ctx.send("Use **-blackjack** to start the game")
            os.system('python blackjackGame.py')
            pass

        #Slots 
        elif str(reaction.emoji) == 'π°':
            await ctx.send("Slots will now start...")
            await ctx.send("Use **-slots** to start the game")
            os.system('python slotsGame.py')
            pass

        #Emoji Racing
        elif str(reaction.emoji) == 'π':
            embed3 = discord.Embed(
                title = "Welcome to Emoji Racing!",
                description = 'Select how many players want to race',
                color = discord.Color.blurple(),
            )
            await ctx.channel.purge(limit=5)
            msg = await ctx.send(embed=embed3)
            await msg.add_reaction('2οΈβ£')
            await msg.add_reaction('3οΈβ£')
            await msg.add_reaction('4οΈβ£')
            await msg.add_reaction('5οΈβ£')

            def checkRaceReaction(reaction, user):
                return user != bot.user and (str(reaction.emoji) == '2οΈβ£' or str(reaction.emoji) == '3οΈβ£' or str(reaction.emoji) == '4οΈβ£' or str(reaction.emoji) == '5οΈβ£')
            reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check = checkRaceReaction)

            #Selecting amount of players for emoji racing 
            if str(reaction.emoji) == '2οΈβ£':
                await ctx.send("Race 2 will now start...")
                await ctx.send("Use **-race** and @ yourself with 1 other player to start the game")
                os.system('python RaceTwo.py')
                pass
            elif str(reaction.emoji) == '3οΈβ£':
                await ctx.send("Race 3 will now start...")
                await ctx.send("Use **-race** and @ yourself with 2 other players to start the game")
                os.system('python RaceThree.py')
                pass
            elif str(reaction.emoji) == '4οΈβ£':
                await ctx.send("Race 4 will now start...")
                await ctx.send("Use **-race** and @ yourself with 3 other players to start the game")
                os.system('python RaceFour.py')
                pass
            elif str(reaction.emoji) == '5οΈβ£':
                await ctx.send("Race 5 will now start...")
                await ctx.send("Use **-race** and @ yourself with 4 other players to start the game")
                os.system('python RaceFive.py')
                pass


bot.run(TOKEN, bot=True, reconnect=True)
client.run(TOKEN)
