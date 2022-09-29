# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import logging
import logging.handlers
import sys
from dotenv import load_dotenv
import os
from pathlib import Path
import typing
import controller

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
async def createCampaign(ctx, name):
    await ctx.send(controller.createCampaign(ctx.guild.id, name))

@bot.command()
async def selectCampaign(ctx, name):
    await ctx.send(controller.selectCampaign(ctx.guild.id, name))  

@bot.command()
async def getCampaign(ctx):
    await ctx.send(controller.getCampaign(ctx.guild.id))

@bot.command()
async def listCampaigns(ctx):
    await ctx.send(controller.listCampaigns(ctx.guild.id))  

@bot.command()
async def deleteCampaign(ctx, name):
    await ctx.send(controller.deleteCampaign(ctx.guild.id, name))      

@bot.command()
async def createCharacter(ctx, name):
    await ctx.send(controller.createCharacter(ctx.guild.id, name))
async def getCharacter(ctx):
    await ctx.send(controller.getCharacter(ctx.guild.id, ctx.author.id))

@bot.command()
async def listCharacters(ctx):
    await ctx.send(controller.listCharacters(ctx.guild.id))  

@bot.command()
async def deleteCharacter(ctx, name):
    await ctx.send(controller.deleteCharacter(ctx.guild.id, name))

@bot.command()
async def campaignOverview(ctx):
    await ctx.send(controller.campaignOverview(ctx.guild.id))

@bot.command()
async def campaignKills(ctx):
    await ctx.send(controller.campaignKills(ctx.guild.id))

@bot.command()
async def getKills(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getKills(ctx.guild.id, ctx.author.id, name))    

@bot.command()
async def addKill(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.addKills(ctx.guild.id, ctx.author.id, 1, name))

@bot.command()
async def setKills(ctx, kills: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setKills(ctx.guild.id, ctx.author.id, kills, name))    

@bot.command()
async def campaignDowns(ctx):
    await ctx.send(controller.campaignDowns(ctx.guild.id))

@bot.command()
async def getDowns(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getDowns(ctx.guild.id, ctx.author.id, name)) 

@bot.command()
async def addDown(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.addDown(ctx.guild.id, ctx.author.id, 1, name))

@bot.command()
async def setDowns(ctx, downs: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setDowns(ctx.guild.id, ctx.author.id, downs, name))    

@bot.command()
async def campaignDeaths(ctx):
    await ctx.send(controller.campaignDeaths(ctx.guild.id))

@bot.command()
async def getDeaths(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getDeaths(ctx.guild.id, ctx.author.id, name)) 

@bot.command()
async def addDeath(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.addDeath(ctx.guild.id, ctx.author.id, 1, name))

@bot.command()
async def setDeaths(ctx, deaths: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setDeaths(ctx.guild.id, ctx.author.id, deaths, name))    

@bot.command()
async def campaignDamageDealt(ctx):
    await ctx.send(controller.campaignDamageDealt(ctx.guild.id))

async def getDamageDealt(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getDamageDealt(ctx.guild.id, ctx.author.id, name)) 

@bot.command()
async def addDamageDealt(ctx, dmg: int, name: typing.Optional[str] = None):
    await ctx.send(controller.addDamageDealt(ctx.guild.id, ctx.author.id, dmg, name))

@bot.command()
async def setDamageDealt(ctx, dmg: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setDamageDealt(ctx.guild.id, ctx.author.id, dmg, name))    

@bot.command()
async def campaignDamageReceived(ctx):
    await ctx.send(controller.campaignDamageReceived(ctx.guild.id))

@bot.command()
async def getDamageReceived(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getDamageReceived(ctx.guild.id, ctx.author.id, name)) 

@bot.command()
async def addDamageReceived(ctx, dmg: int, name: typing.Optional[str] = None):
    await ctx.send(controller.addDamageReceived(ctx.guild.id, ctx.author.id, dmg, name))

@bot.command()
async def setDamageReceived(ctx, dmg: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setDamageReceived(ctx.guild.id, ctx.author.id, dmg, name))    

@bot.command()
async def campaignHealingPerformed(ctx):
    await ctx.send(controller.campaignHealingPerformed(ctx.guild.id))

@bot.command()
async def getHealingPerformed(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getHealingPerformed(ctx.guild.id, ctx.author.id, name)) 

@bot.command()
async def addHealingPerformed(ctx, hp: int, name: typing.Optional[str] = None):
    await ctx.send(controller.addHealingPerformed(ctx.guild.id, ctx.author.id, hp, name))

@bot.command()
async def setHealingPerformed(ctx, hp: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setHealingPerformed(ctx.guild.id, ctx.author.id, hp, name))    

@bot.command()
async def campaignHealingReceived(ctx):
    await ctx.send(controller.campaignHealingReceived(ctx.guild.id))

@bot.command()
async def getHealingReceived(ctx, name: typing.Optional[str] = None):
    await ctx.send(controller.getHealingReceived(ctx.guild.id, ctx.author.id, name)) 

@bot.command()
async def addHealingReceived(ctx, hp: int, name: typing.Optional[str] = None):
    await ctx.send(controller.addHealingReceived(ctx.guild.id, ctx.author.id, hp, name))

@bot.command()
async def setHealingReceived(ctx, hp: int, name: typing.Optional[str] = None):
    await ctx.send(controller.setHealingReceived(ctx.guild.id, ctx.author.id, hp, name))    

controller.connect()

# Assume bot refers to a discord.ext.command.Bot subclass...
# Suppress the default configuration since we have our own
bot.run(os.environ.get('discord_token'), log_handler=None)