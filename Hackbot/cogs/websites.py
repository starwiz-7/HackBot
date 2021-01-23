import discord
from discord.ext import commands
from utils.db import *

class SourceCogError(commands.CommandError):
    pass

class Source(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

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

    @commands.guild_only()
    @commands.has_permissions(read_messages=True,send_messages=True)  
    @commands.command(brief="Fetch hackathons from source")
    async def web(self,ctx, *string):
        if len(string) == 0:
            await ctx.send("```Add a website to the command to show the listed hackathons\nSupported Websites:\nMLH\nDevpost\nDevfolio```")
        else:
            website = string[0].upper()
            hackathons = get_hackathon(website)
            print(hackathons)
            if len(hackathons[0])>0:
                hackathon = list(self.parse_hackathons(hackathons))
                asset = get_asset(website)
                for i in hackathon:
                    print(i)
                    msg = discord.Embed(title=f'Hackathons listed on {website}')
                    msg.set_thumbnail(url=asset[0]['thumbnail'])
                    for j in i:
                        await msg.add_field(name=j['name'],value=j['url'],inline=False)
                    


def setup(bot):
    bot.add_cog(Source(bot))