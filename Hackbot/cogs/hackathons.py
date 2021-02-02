import discord
from discord.ext import commands, tasks
from utils.db import *
import asyncio


class HackathonCogsError(commands.CommandError):
    pass

class Hackathons(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.check_if_new.start()
        self.server_count.start()

    def get_channel_id(self,ctx,channel):
        channels = ctx.guild.text_channels
        for i in channels:
            if i.name == channel:
                return i.id
        return False

    def save_channel_details(self, ctx, channel_id):
        server = is_guild(ctx.guild.id)
        if len(server) == 0:
            save_new_guild(ctx.guild.id, channel_id)
        else:
            update_channel(ctx.guild.id, channel_id)
        
    async def create_channel(self,ctx,channel):
        message = await ctx.send("```Creating channel "+channel+"```")
        await ctx.guild.create_text_channel(channel)
        channel_id = self.get_channel_id(ctx,channel)
        newcontent = "```Channel "+channel+" created and hacked for notifications.```"
        await message.edit(content=newcontent)

    async def validate_channel(self,ctx, channel):
        channel = channel[0]
        channel_id = self.get_channel_id(ctx,channel)
        if channel_id != False:
            self.save_channel_details(ctx,channel_id)
            await ctx.send(channel+" is hacked for notifications!!")
        else:
            await self.create_channel(ctx,channel)
    

    async def no_channel(self,ctx,channel):
        raise HackathonCogsError("The selected channel is not available.")

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True,read_messages=True,send_messages=True)
    @commands.command(brief="Hack a channel for upcoming hackathon notifications.")
    async def notify(self,ctx, *channel):
        await self.validate_channel(ctx,channel)

    @commands.guild_only()
    @commands.has_permissions(manage_channels=True,read_messages=True,send_messages=True)
    @commands.command(brief="Unsubscribe the channel.")
    async def unsub(self,ctx):
        delete_guild(ctx.guild.id)
        await ctx.send("Unsubscribed") 


    #Embedding max of 4 hackathons
    def parse_hackathons(self,hackathons):
        k = 1
        l = []
        sliced_list = []
        for i in hackathons:
            l.append(i)
            k+=1
            if(k %5 == 0):
                yield l
                k = 1
                l = []
        return sliced_list

    #Sending the embeds to all the guilds
    @commands.has_permissions(send_messages=True)
    async def send_notif(self,msg):
        servers = get_guilds()
        for i in servers:
            try:
                channel = self.bot.get_channel(i['channel'])
                await channel.send(embed=msg)
            except:
                continue
    

    #Embedding multiple hackathon in one embed
    async def multiple_embed(self,hackathons):
        website = hackathons[0]['website']
        hacks = self.parse_hackathons(hackathons)
        asset = get_asset(website)
        for i in hacks:
            msg = discord.Embed(title="New Hackathons")
            msg.set_thumbnail(url=asset[0]['thumbnail'])
            for j in i:
                msg.add_field(name=j['name'], value=j['url'],inline=False)
            await self.send_notif(msg)

    #Single hackathon embedding
    async def single_embed(self, hackathons):
        msg = discord.Embed(title="New Hackathon")
        hackathons = hackathons[0]
        asset = get_asset(hackathons['website'])
        msg.set_thumbnail(url = asset[0]['thumbnail'])
        msg.add_field(name=hackathons['name'], value=hackathons['url'])
        msg.add_field(name="Start Date",value=hackathons['start'], inline=False)
        msg.add_field(name="End Date",value=hackathons['end'], inline=False)
        msg.add_field(name="Mode", value=hackathons['mode'], inline=False)
        msg.add_field(name="Location", value=hackathons['location'], inline=False)
        await self.send_notif(msg)
        # return msg
        
    #Check the length of hackathons ordered by website
    async def check_list(self,hackathon):
        if len(hackathon) > 1:
            await self.multiple_embed(hackathon)
        elif len(hackathon) == 1:
            await self.single_embed(hackathon)

    #Check after 1 minute if a new hackathon is added
    @tasks.loop(seconds=1860.0)
    async def check_if_new(self):
        hackathon = new_hackathon()
        print("Running....")
        if len(hackathon) != 0:
            hackathon = sorted(hackathon, key=lambda x: x['website'])
            web_list = []
            k = hackathon[0]['website']
            for i in hackathon:
                update_hackathon(i['name'], i['website'])
                if i['website'] == k:
                    web_list.append(i)
                else:
                    await self.check_list(web_list)
                    k = i['website']
                    web_list = []
                    web_list.append(i)
            await self.check_list(web_list)
    
    @tasks.loop(seconds=60.0)
    async def server_count(self):
        print(len(self.bot.guilds))

    @check_if_new.before_loop
    @server_count.before_loop
    async def before_print(self):
        await self.bot.wait_until_ready()
    

def setup(bot):
    bot.add_cog(Hackathons(bot))

