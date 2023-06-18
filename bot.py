import discord
import random
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def info(ctx):
    await ctx.send("I've been here the entire time........ 🤖\n\nYou can use the following commands to interact with me\n\t      /ping - I'll respond with 'pong'\n\t      /kill @someone - I'll kill the person you want me to, with one of my breathing forms......😈")


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("pong")

# @bot.command()
# async def test(ctx):
#     await ctx.send("Test successful")


@bot.event
async def on_ready():
    print("Successfully logged in! Logged in as ", bot.user.name)


@bot.event
async def on_message(message):
    text = str(message.content)
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
    if text[:5] == '/kill' and len(text[6:]) > 0:
        await message.channel.send('As you wish my master........\n')
        await message.channel.send(f'🌙Moon breathing🌙: {attacks[random.randint(0,10)]}\n')
        await message.channel.send(f'{str(message.author.mention)} killed {text[5:]}😵😵')
    await bot.process_commands(message)

bot.run("MTExOTU5MDA0MjI1MjM1NzY4Mg.GvF3kt.VAoyXH1eCqwRQbbzS3QC8UO56d1ab6Qt5BdVuM")
