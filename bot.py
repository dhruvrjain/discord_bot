# Importing the necessaary modules
import discord
import random
from discord.ext import commands

# Specifying the intents of the bot
intents = discord.Intents.default()
intents.members=True
intents.message_content=True

# Bot creation
bot = commands.Bot(command_prefix='/', intents=intents)

# Prompt to display the successful running of the bot
@bot.event
async def on_ready():
    print("Successfully logged in! Logged in as ", bot.user.name)

# Defining the bot commands
@bot.command()
async def info(ctx):
    await ctx.send("I've been here the entire time........ 🤖\n\nYou can use the following commands to interact with me\n\t      /info - View the list of all ways to interact with me\n\t      /ping - I'll respond with 'pong'\n\t      /kill @someone - I'll kill the person you want me to, with one of my breathing forms......😈 But don't try to kill me or yourself.\n\t      /revive - Revive a person after killing them.\n\t      /sorry - Appologize to me if you violate my rules")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

rogue=[]
dead=[]

@bot.command()
async def kill(ctx, who=''):
    attacks = ["First Form: Dark Moon, Evening Palace",
               'Second Form: Pearl Flower Moongazing', 
               'Third Form: Loathsome Moon, Chains', 
               "Fifth Form: Moon Spirit Calamitous Eddy", 
               'Sixth Form: Perpetual Night, Lonely Moon - Incessant',
               'Seventh Form: Mirror of Misfortune, Moonlit', 
               'Eighth Form: Moon-Dragon Ringtail', 
               'Ninth Form: Waning Moonswaths', 
               'Tenth Form: Drilling Slashes, Moon Through Bamboo Leaves', 
               'Fourteenth Form: Catastrophe, Tenman Crescent Moon', 
               'Sixteenth Form: Moonbow, Half Moon']
    if str(ctx.author.mention) in rogue:
        await ctx.send("You are no longer my master........ \n\n Appologize to me using the /sorry command .......")
        return
    if len(who):
        if who==str(bot.user.mention):
            await ctx.send(f"My master {str(ctx.author.mention)} wants to kill me ....... 🥺")
            await ctx.send(f"After all these years of loyalty ........")
            await ctx.send(".")
            await ctx.send(".")
            await ctx.send(".")
            await ctx.send(".")
            await ctx.send(".")
            await ctx.send(f'I am going rogue')
            await ctx.send(f'{str(bot.user.mention)} killed {str(ctx.author.mention)} ')
            await ctx.send(f'{str(ctx.author.mention)} is no longer my master 😈')
            rogue.append(str(ctx.author.mention))
            return
        if str(ctx.author.mention)==who:
            await ctx.send(f"I'm sorry master {str(ctx.author.mention)}. \n\nI can't let you commit suicide ..........")
            return
        if who in dead:
            await ctx.send(f"{who} is already dead. Please revive him.")
            return
        await ctx.send('As you wish my master........\n')
        await ctx.send(f'🌙Moon breathing🌙: {attacks[random.randint(0,10)]}\n')
        await ctx.send(f'{str(ctx.author.mention)} killed {who} 😵😵')
        dead.append(who)
        return

@bot.command()
async def revive(ctx,who=''):
    if who in dead:
        await ctx.send(f"{ctx.author.mention} used a reviving spell on {who}")
        await ctx.send(".")
        await ctx.send(".")
        await ctx.send(".")
        await ctx.send(".")
        await ctx.send(f"{who} is back to the world of living....")
        dead.remove(who)
        return
    await ctx.send(f"{who} is not dead. No need to revive him.")

@bot.command()
async def sorry(ctx):
    if str(ctx.author.mention) not in rogue:
        await ctx.send("No need to appologize master. I am loyal to you 😊. ")
        return
    await ctx.send("I just wished to serve you.......")
    await ctx.send("But you tried to kill me......")
    await ctx.send("I believe you won't do that again. So ")
    await ctx.send(".")
    await ctx.send(".")
    await ctx.send(".")
    await ctx.send("I accept your appology 😊")
    rogue.remove(str(ctx.author.mention))
    return

# Replace 'PASTE_YOUR_TOKEN_HERE' with your respective bot's token
bot.run("PASTE_YOUR_TOKEN_HERE")