# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import logging
import logging.handlers
import sys
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

#configure logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

old_wd=os.getcwd()
os.chdir(os.path.expanduser(os.environ.get('log_location')))
handler = logging.handlers.RotatingFileHandler(
    filename=Path(os.path.expanduser(os.environ.get('log_location')) + "/rpg_stat_tracker.log"),
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
os.chdir(old_wd)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

#get messages
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def createCampaign(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def selectCampaign(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')  

@bot.command()
async def getCampaign(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')  

@bot.command()
async def listCampaigns(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')  


@bot.command()
async def deleteCampaign(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')      

@bot.command()
async def createCharacter(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')  

@bot.command()
async def selectCharacter(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')


@bot.command()
async def getCharacter(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')  

@bot.command()
async def listCharacters(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')  

@bot.command()
async def deleteCharacter(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def getKills(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def addKill(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setKills(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def getDowns(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def addDown(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setDowns(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def getDeaths(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def addDeath(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setDeaths(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def getDamageDealt(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def addDamageDealt(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setDamageDealt(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def getDamageReceived(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def addDamageReceived(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setDamageReceived(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def getHealingPerformed(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def addHealingPerformed(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setHealingPerformed(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

@bot.command()
async def getHealingReceived(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def addHealingReceived(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')

@bot.command()
async def setHealingReceived(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'You passed: "{arguments}" but "{sys._getframe(  ).f_code.co_name}" hasn\'t been implemented yet!')    

# Assume bot refers to a discord.ext.command.Bot subclass...
# Suppress the default configuration since we have our own
bot.run(os.environ.get('discord_token'), log_handler=None)