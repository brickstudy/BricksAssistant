import os
import discord
from discord.ext import commands

import src.message as msg


# env setting
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


# discord commands
@bot.command()
async def ping(ctx):
    await msg.get_pong(ctx)


@bot.command()
async def help1(ctx):
    await ctx.send("Pong!")


@bot.command()
async def GPT(ctx):
    await ctx.send("hi GPT!")


# discord setting
def run_bot():
    return bot.run(DISCORD_TOKEN)
