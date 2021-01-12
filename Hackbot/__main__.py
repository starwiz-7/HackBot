import os
from os import environ
import logging
from pathlib import Path
import discord
from discord.ext import commands

def main():
    token = "Nzk2NzI0MTkxNzUxNTY5NDc5.X_cFOQ.NYuv81J8cYlPBLic9L4d5UkyjSo"
    if not token:
        logging.error('Token missing')
        return
    
    # intents = discord.Intents.default()
    # intents.members = True

    bot = commands.Bot(command_prefix=commands.when_mentioned_or('!hack '))
    # cogs = [file.stem for file in Path('Hackbot', 'cogs').glob('*.py')]
    # for extension in cogs:
    #     print(extension)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    print(f'Cogs loaded: {", ".join(bot.cogs)}')

    def no_dm_check(ctx):
        if ctx.guild is None:
            raise commands.NoPrivateMessage('No Private Hacking!!')
        return True
    
    bot.add_check(no_dm_check)

    # @discord_common.on_ready_event_once(bot)
    bot.run(token)

if __name__ == '__main__':
    main()