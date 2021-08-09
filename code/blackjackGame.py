import discord 
import random
from discord.ext import commands
from gameConfig import *
import os

#simple version of Blackjack
cards = [2,3,4,5,6,7,8,9,10,11,12,13,14] * 4

#'Jack' == 11
#'Queen' == 12
#'King' == 13
#'Ace' == 14


player = ""
playerdealt = ""
dealerup = ""
dealerdown = ""
dealerdealt = ""
dealer = ""

async def bigCards(ctx):
    global player
    global playerdealt
    global dealer
    global dealerdealt
    global cards
    global dealerup
    global dealerdown

    if playerdealt == 11:
        await ctx.send("You pulled a Jack. Its value is...")
        playerdealt = 10
    elif playerdealt == 12:
        await ctx.send("You pulled a Queen. Its value is...")
        playerdealt = 10
    elif playerdealt == 13:
        await ctx.send("You pulled a King. Its value is...")
        playerdealt = 10
    elif playerdealt == 14:
        await ctx.send("You pulled an Ace. Its value is...")
        if player <= 10:
            playerdealt = 11
        elif player > 10:
            playerdealt = 1
            
    if dealerup == 11:
        dealerup = 10
    elif dealerup == 12:
        dealerup = 10
    elif dealerup == 13:
        dealerup = 10
    elif dealerup == 14:
        if dealer <= 10:
            dealerup = 11
        elif dealer > 10:
            dealerup = 1

    if dealerdown == 11:
        dealerdown = 10
    elif dealerdown == 12:
        dealerdown = 10
    elif dealerdown == 13:
        dealerdown = 10
    elif dealerdown == 14:
        if dealer <= 10:
            dealerdown = 11
        elif dealer > 10:
            dealerdown = 1

@bot.command()
async def blackjack(ctx):

    global player
    global playerdealt
    global dealer
    global dealerdealt
    global cards
    global dealerup
    global dealerdown

    random.shuffle(cards)

    await ctx.send("Dealing out first wave of cards...")
    playerdealt = cards.pop() 
    await bigCards(ctx)
    await ctx.send(str(playerdealt))
    player = playerdealt
    await ctx.send("Dealing out second wave of cards...")
    playerdealt = cards.pop()
    await bigCards(ctx)
    await ctx.send(str(playerdealt)) 
    player = player + playerdealt
    await ctx.send('Your hand total is ' + str(player) + '.')
    dealerup = cards.pop()
    dealerdown = cards.pop()
    await bigCards(ctx)
    await ctx.send('The dealer hand has been dealt. He currently has ' + str(dealerup) + '.')
    await ctx.send('Would you like to **-hit** or **-stand**?')

@bot.command()
async def hit(ctx):

    global player
    global playerdealt
    global dealer
    global dealerdealt
    global cards
    global dealerup
    global dealerdown

    await ctx.send("Dealing out another card.")
    playerdealt = cards.pop()
    await bigCards(ctx)
    await ctx.send(str(playerdealt))
    player = player + playerdealt
    await ctx.send('Your hand total is ' + str(player) + '.')
    if player > 21:
        await ctx.send('You went over 21, you lose!')
    elif player <= 21:
        await ctx.send('You may **-hit** again, or choose to **-stand**.')

@bot.command()
async def stand(ctx):

    global player
    global playerdealt
    global dealer
    global dealerdealt
    global cards
    global dealerup
    global dealerdown

    dealer = dealerup + dealerdown
    
    await ctx.send('The second card is revealed: ' + str(dealerdown) + ' The dealer now has ' + str(dealer) + '.')

    if dealer < 17:
        await ctx.send('The dealer will begin to draw cards..')

    while dealer < 17:
        dealerdealt = cards.pop()
        dealer = dealer + dealerdealt
    else: 
        pass


    await ctx.send('You chose to stand with ' + str(player) + ' in your hand.')
    await ctx.send('The dealer has ' + str(dealer) + ' in their hand.')
    if player > dealer:
        await ctx.send('You win!')
    elif dealer <= 21 and dealer > player:
        await ctx.send('You lose!')
    elif dealer > 21:
        await ctx.send('Dealer hand went over 21! You win!')
    elif dealer == player:
        await ctx.send('The game ends in a tie!')


#reset command = bring user back to menu
@bot.command()
async def reset(ctx):
    await ctx.send("Resetting files...use **-menu** for the game menu")
    os.system('python startup.py')
    pass



bot.run(TOKEN, bot=True, reconnect=True)
client.run(TOKEN)
