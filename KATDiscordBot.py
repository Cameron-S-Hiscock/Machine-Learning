import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
import info

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Welcome to {member.guild.name}, {member.mention}!')

@bot.command()
async def serverPing(ctx, times: int,*, message: str):
    for _ in range(times):
        await ctx.send(message)

@bot.command()
async def userPing(ctx, member: discord.Member, times: int, *, message: str):
    await ctx.send(f"Sent a DM to {member.name}!")
    for _ in range(times):
        await member.send(message)

@bot.command()
async def sendPic(ctx, url: str):
    await ctx.send(url)

@bot.command()
async def roast(ctx, member: discord.Member):
    await ctx.send(f"{member.mention}, {random.choice(info.roasts)}")

bot.run(os.getenv('BOT_TOKEN'))