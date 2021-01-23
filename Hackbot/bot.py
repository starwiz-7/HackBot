import os
from os import environ
import logging
from pathlib import Path
import discord
from discord.ext import commands
from discord.utils import find
from utils.db import new_hackathon
def main():
    DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
    if not DISCORD_TOKEN:
        logging.error('Token missing')
        return

    bot = commands.Bot(command_prefix=commands.when_mentioned_or(';hack '), case_sensitive=False)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    print(f'Cogs loaded: {", ".join(bot.cogs)}')

    def no_dm_check(ctx):
        if ctx.guild is None:
            raise commands.NoPrivateMessage('No Private Hacking!!')
        return True
    
    bot.add_check(no_dm_check)
    @bot.event
    async def on_ready():
        await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name='with Hackathons' )
    )
    @bot.event
    async def on_guild_join(guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send("```Hello guyss! HackBot is here to notify you all about the upcoming hackathons\nCommand Prefix: !hack\nFor help in commands type: !hack help```")
                break

    @bot.event
    async def on_command_error(ctx,error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Please type `;hack help` for list of commands")
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()