from discord import message
import qrcode
from PIL import Image
from enum import auto
import discord
from discord import player
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from discord import TextChannel
from youtube_dl import YoutubeDL
import youtube_dl
import asyncio
import os
from test import Music
import platform
import datetime

from youtube_dl.utils import DateRange, dict_get
bot = commands.Bot(command_prefix='==')

bot.add_cog(Music(bot))
 
@bot.event
async def on_ready():
    activity = discord.Game(name="Netflix", type=3)
    await bot.change_presence(status=discord.Status.dnd ,activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep."))
    print("Bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)

@bot.command(name='qrmake',aliases=['qrm'])
async def qrmake(ctx, *, stuff:str):
    os.remove("boomerbot.jpg")
    img = qrcode.make(stuff)
    img.save("boomerbot.jpg")
    await ctx.send(file=discord.File('boomerbot.jpg'))
    await ctx.message.delete()

@bot.command(name='qrsend',aliases=['qrs'])
async def qrsend(ctx):
    await ctx.send(file=discord.File('boomerbot.jpg'))

@bot.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send("Messages have been cleared", delete_after=5)


@bot.command()
async def ping(ctx):
    await ctx.reply(f'Ping is {round(bot.latency * 1000)} ms')
























bot.run('ODkwOTc3NzAzNDU1NTEwNTc4.YU3ppg.VrCU_RtOrMyaAuV1XLSmnI-zvZY')
