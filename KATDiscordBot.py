import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def sendMessage(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def multiPing(ctx, times: int,*, message: str):
    for _ in range(times):
        await ctx.send(message)

@bot.command()
async def userMessage(ctx, member: discord.Member, *, message: str):
    await member.send(message)
    await ctx.send(f"Sent a DM to {member.name}!")

@bot.command()
async def multiUserMessage(ctx, member: discord.Member, times: int, *, message: str):
    await ctx.send(f"Sent a DM to {member.name}!")
    for _ in range(times):
        await member.send(message)

bot.run(os.getenv('DISCORD_TOKEN'))