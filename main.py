import discord
from discord.ext import commands
import os
import time

DISCORD_TOKEN = 'DISCORD_TOKEN'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!\nЯ расскажу тебе о глобальном потеплении. Задавай свои вопросы)\nКоманды: /Why, /For_what, /How')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)       

bot.run(DISCORD_TOKEN)