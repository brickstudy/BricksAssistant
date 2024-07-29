import os
import pytest
from dotenv import load_dotenv

import discord
from discord.ext import commands


load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    # 봇이 보낸 메시지는 무시
    if message.author == bot.user:
        return

    # 메시지에서 멘션된 사용자가 있는지 확인
    if bot.user.mentioned_in(message):
        await message.channel.send(f'You mentioned me, {message.author.mention}!')

    # 커맨드 처리를 위해 on_message 이벤트 안에 command 처리기를 호출해야 합니다.
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(DISCORD_TOKEN)
