import discord
from datetime import datetime

from src.adapter.gpt import GPTFactory
from src.adapter.database import DatabaseFactory
from src.application.entity import GPTConversationInfo
from src.application.service.request_answer import GPTRequestService

async def get_pong(ctx):
    await ctx.send("Pong!")


async def get_gpt_answer(ctx, question: str):
    now = datetime.now()
    user = ctx.message.author

    info = GPTConversationInfo(
        user_id=user.id,
        user_name=user.name,
        request_time=now.strftime('%Y-%m-%d %H:%M:%S'),
        question=question
    )

    client = GPTFactory.create_client(gpt_type="chatgpt")
    db = DatabaseFactory.create_database_gpt("dynamodb")
    service = GPTRequestService()

    # Question on channel
    if ctx.message.channel.type != discord.ChannelType.public_thread:
        thread = await ctx.message.create_thread(
            name=f"A. {question}",
            auto_archive_duration=60    # minute 기준
        )
        info.thread_id = thread.id

        result = service.request_answer(client, db, info)
        await thread.send(result.answer)
    # Question on thread
    else:
        info.thread_id = ctx.message.channel.id

        result = service.request_answer(client, db, info)
        await ctx.send(result.answer)
