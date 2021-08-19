# Discord-MiniCasinoBot
A Discord Bot for playing your favorite casino games. Select which game you want to play from the main menu and enjoy! 

# How to Run in Your Discord Server:

## Notes before starting:
* You need to go to the Discord Developer Portal and create your own Discord bot following the instructions here: https://discord.com/developers/docs/intro
* After you create your bot, invite it to your server and follow the steps below
* Find your bot's token and replace the 'YOUR_TOKEN_HERE' with it in the *gameConfig.py* file

# 1. Download all the files from this GitHub repository
  * Make sure to put the files in a directory where you will remember
  * Run *startup.py* from the directory where you stored the downloaded files in your terminal 
  
# 2. Once the bot is running in the terminal, make sure it is online in your Discord server
  * Use the bot commands in Discord chat in order to run:
    * Type *-tips* for command help  
    * Type *-menu* for the game menu, react to the menu's reactions to choose a game
    * Type *-reset* to leave the current game and go back to the menu

## Bot Games and How to Play:
* LRC - Left, Right, Center - can be played with 3-6 users. The goal is to be the last one standing with chips. Each user will take turns rolling up to 3 "dice" at a time. If you have less than 3 chips, you will roll that amount of dice. If a user rolls an L or R, the chips will be given to whatever user is on the left or right of them in the rotation of the game. If you roll a C, the chips will be put into the center pot where they will no longer be used. If you roll a '*', the chips stay with you. After everyone loses their chips to the center, whover has chips remaining wins the game!
* Coinflip - Select heads or tails and if the coin flips on the one you chose, you win!
* Simple Blackjack - Traditional blackjack..without doubling down or insurance. 
* Slots - Run some slots and earn tokens depending on how your roll is!
* Race - work in progress
