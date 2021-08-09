
import discord 
import random
from discord.ext import commands
from gameConfig import *
import os

dice = ['*', '*', '*', 'L', 'R', 'C']
values = {
    '*': 0,
    'L': 1,
    'R': 1,
    'C': 1
}

async def gambler(ctx):
    global chips 
    global pot
    global rotatedL
    global rotatedR
    response = random.choice(dice)
    await ctx.send(response)         
    if response == 'L':
        chips = chips - 1
        rotatedL = rotatedL + 1
    elif response == 'R':
        chips = chips - 1
        rotatedR = rotatedR + 1
    elif response == 'C':
        chips = chips - 1
        pot = pot + 1
    elif response == '*':
        chips = chips

async def turnswap(ctx):
    global turn
    global player1
    global player2
    global player3
    global chips
    global chipsp1
    global chipsp2
    global chipsp3
    global rotatedL

    if chips == 0:
        await ctx.send('You are out of chips...')

    if turn == player1:
        chipsp3 = chipsp3 + rotatedL
        chipsp1 = chips
        turn = player2
        await ctx.send("Roll the dice, <@" + str(player2.id) + ">.")
    elif turn == player2:
        chipsp1 = chipsp1 + rotatedL
        chipsp2 = chips
        turn = player3
        await ctx.send("Roll the dice, <@" + str(player3.id) + ">.")
    elif turn == player3:
        chipsp2 = chipsp2 + rotatedL
        chipsp3 = chips
        turn = player1
        await ctx.send("Roll the dice, <@" + str(player1.id) + ">.")

#each player starts with 3 chips
chips = 0
chipsp1 = 3
chipsp2 = 3
chipsp3 = 3
rotatedR = 0
rotatedL = 0

#center money pot
pot = 0

player1 = ""
player2 = ""
player3 = ""
turn = ""
gameOver = True
response = 0


@bot.command(pass_context=True)
async def LRC(ctx, p1 : discord.Member, p2 : discord.Member, p3 : discord.Member):
    global player1
    global player2
    global player3
    global turn
    global gameOver
    global count

    if gameOver:
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2
        player3 = p3

        #player turn randomizer 
        num = random.randint(1, 3)
        if num == 1:
            turn = player1
            await ctx.send("Roll the dice, <@" + str(player1.id) + ">.")
            await ctx.send("Everyone else, please wait for me to @ you before you take your turn!")
        elif num == 2:
            turn = player2
            await ctx.send("Roll the dice, <@" + str(player2.id) + ">.")
            await ctx.send("Everyone else, please wait for me to @ you before you take your turn!")
        elif num == 3:
            turn = player3
            await ctx.send("Roll the dice, <@" + str(player3.id) + ">.")
            await ctx.send("Everyone else, please wait for me to @ you before you take your turn!")

    else:
        await ctx.send("Game is currently in progress.")


@bot.command(pass_context=True)
async def roll(ctx):

    global turn
    global player1
    global player2
    global player3
    global chips
    global pot
    global chipsp1
    global chipsp2
    global chipsp3
    global rotatedR
    global rotatedL
    global count
    global gameOver

    if not gameOver:

        if turn == ctx.author:
            if turn == player1:
                chips = chipsp1 
            elif turn == player2:
                chips = chipsp2 
            elif turn == player3:
                chips = chipsp3

            chips = chips + rotatedR 
            rotatedR = 0
            rotatedL = 0
            if chips >= 3:
                
                await gambler(ctx)

                if chips == 0:
                    await ctx.send('You are out of chips...you lose!')
                

                await gambler(ctx)

                if chips == 0:
                    await ctx.send('You are out of chips...')


                await gambler(ctx)

                await ctx.send('You now have ' + str(chips) + ' chip(s) left.')
                await ctx.send('The pot now has ' + str(pot) + ' chip(s) total.')

                await turnswap(ctx)

            elif chips == 2:

                await gambler(ctx)

                if chips == 0:
                    await ctx.send('You are out of chips...')


                await gambler(ctx)

                await ctx.send('You now have ' + str(chips) + ' chip(s) left.')
                await ctx.send('The pot now has ' + str(pot) + ' chip(s) total.')

                await turnswap(ctx)

            elif chips == 1:

                await gambler(ctx)

                await ctx.send('You now have ' + str(chips) + ' chip(s) left.')
                await ctx.send('The pot now has ' + str(pot) + ' chip(s) total.')            

                await turnswap(ctx)
            
            elif chips == 0:
                await ctx.send('Have fun sitting around, poorboy.')

                await turnswap(ctx)

            if chipsp1 == 0 and chipsp2 == 0:
                gameOver = True
                await ctx.send("Congratulations, <@" + str(player3.id) + ">, you win!.")
                await ctx.send("Please use **-reset** to return to the menu and start a new game.")
            elif chipsp2 == 0 and chipsp3 == 0: 
                gameOver = True
                await ctx.send("Congratulations, <@" + str(player1.id) + ">, you win!.")
                await ctx.send("Please use **-reset** to return to the menu and start a new game.")
            elif chipsp3 == 0 and chipsp1 == 0:
                gameOver = True
                await ctx.send("Congratulations, <@" + str(player2.id) + ">, you win!.")
                await ctx.send("Please use **-reset** to return to the menu and start a new game.")

        else:
            await ctx.send("Please wait for your turn.")
    else: 
        await ctx.send("There is currently no game being played at the moment. Start one up!")

@bot.command()
async def reset(ctx):
    await ctx.send("Resetting files...use **-menu** for the game menu")
    os.system('python startup.py')
    pass

bot.run(TOKEN, bot=True, reconnect=True)
client.run(TOKEN)
