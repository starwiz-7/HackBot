import discord
from discord.ext import commands
from utils.db import *


class ChannelCogsError(commands.CommandError):
    pass

class Channels(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def get_channel_id(self,ctx,channel):
        channels = ctx.guild.text_channels
        # channel = channel[0]
        print(channel)
        for i in channels:
            if i.name == channel:
                print(i.id)
                return i.id
        return False

    def save_channel_details(self, ctx, channel_id):
        server = is_guild(ctx.guild.id)
        if len(server) == 0:
            save_new_guild(ctx.guild.id, channel_id)
        else:
            update_channel(ctx.guild.id, channel_id)
        
    async def create_channel(self,ctx,channel):
        await ctx.send("`Creating channel "+channel+"`")
        await ctx.guild.create_text_channel(channel)
        channel_id = self.get_channel_id(ctx,channel)

    async def validate_channel(self,ctx, channel):
        channel = channel[0]
        print(channel)
        channel_id = self.get_channel_id(ctx,channel)
        if channel_id != False:
            self.save_channel_details(ctx,channel_id)
            await ctx.send(channel+" is hacked for notifications!!")
        else:
            await self.create_channel(ctx,channel)
        
    async def no_channel(self,ctx,channel):
        raise ChannelCogsError("The selected channel is not available.")


    @commands.command(brief="Hack a channel for further hackathon updates")
    async def channel(self,ctx, *channel):
        await self.validate_channel(ctx,channel)
        await ctx.send("Ruko zara")

    @commands.command(brief="Testing")
    async def test(self,ctx):
        servers = get_guilds()
        for i in servers:
            # print(i['channel'])
            channel = self.bot.get_channel(i['channel'])
            await channel.send("Kool guys!")

def setup(bot):
    bot.add_cog(Channels(bot))

