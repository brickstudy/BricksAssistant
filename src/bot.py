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
async def test_msg(ctx):
    await msg.get_test_msg(ctx)


@bot.command()
async def GPT(ctx):
    await ctx.send("hi GPT!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(message)
    print()
    print(message.author)

    await bot.process_commands(message)


# discord setting
def run_bot():
    return bot.run(DISCORD_TOKEN)
