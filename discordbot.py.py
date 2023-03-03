import discord 
from discord.ext import commands


from discord import Intents


intents = discord.Intents.all()


bot = discord.Bot(Intents=intents)

TOKEN = '(PASTE BOT TOKEN HERE)'



bot.run(TOKEN) 
