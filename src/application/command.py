import os
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


async def get_info(ctx, arg: str):
    application_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
    info_path = os.path.abspath(os.path.join(application_path, "info"))
    # Check arg
    if not arg:
        await ctx.send("사용 가능한 명령어:\n\n!intro 소개\n!intro 권한\n!intro 인프라")
    elif arg == "소개":
        try:
            with open(info_path + "/소개.txt", 'r', encoding="utf-8") as f:
                content = f.read()
                await ctx.send(content)
        except FileNotFoundError:
            await ctx.send("소개 파일을 찾을 수 없습니다. 관리자에게 문의해주세요.")
    elif arg == "권한":
        try:
            with open(info_path + "/권한.txt", 'r', encoding="utf-8") as f:
                content = f.read()
                await ctx.send(content)
        except FileNotFoundError:
            await ctx.send("권한 파일을 찾을 수 없습니다. 관리자에게 문의해주세요.")
    else:
        await ctx.send("잘못된 명령어입니다. !intro 만 입력하여 사용 가능한 명령어를 확인하세요.")
