import discord


async def get_pong(ctx):
    await ctx.send("Pong!")


async def get_gpt_answer(ctx, query):
    if ctx.message.channel.type == discord.ChannelType.public_thread:
        thread_id = ctx.message.channel.id
        print(ctx.message)  # channel > parent
        print(f'Thread ID: {thread_id}')    # Thread id
        await ctx.send("hello thread!")
    else:
        author = ctx.message.author
        author_info = (
            f"User ID: {author.id}\n"
            f"Name: {author.name}\n"
            f"Discriminator: {author.discriminator}\n"
            f"Mention: {author.mention}\n"
        )
        print(ctx.message)  # channel > name
        print(author_info)

        thread = await ctx.message.create_thread(
            name=f"A. {query}",
            auto_archive_duration=60
        )
        # TODO : thread id 기준 관리
        print(thread.id)
        await thread.send("This response is thread.")
