import discord
from datetime import datetime

from src.application.entity import GPTConversationInfo


async def get_pong(ctx):
    await ctx.send("Pong!")


async def get_gpt_answer(ctx, question):
    now = datetime.now()
    user = ctx.message.author

    info = GPTConversationInfo(
        user_id=user.id,
        user_name=user.name,
        request_time=now.strftime('%Y-%m-%d %H:%M:%S'),
        question=question
    )

    # Question on channel
    if ctx.message.channel.type != discord.ChannelType.public_thread:
        thread = await ctx.message.create_thread(
            name=f"A. {question}",
            auto_archive_duration=60    # minute 기준
        )
        info.thread_id = thread.id
        await thread.send(info.thread_id)
    # Question on thread
    else:
        info.thread_id = ctx.message.channel.id
        await ctx.send(info.thread_id)
