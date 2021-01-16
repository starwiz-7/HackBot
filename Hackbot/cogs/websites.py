import discord
from discord.ext import commands
from utils.db import *

class SourceCogError(commands.CommandError):
    pass

class Source(commands.Cog):
    def __inti__(self,bot):
        self.bot = bot

    def parse_hackathons(self,hackathons):
        k = 1
        l = []
        sliced_list = []
        for i in hackathons:
            l.append(i)
            k+=1
            if(k %5 == 0):
                # print(l)
                yield l
                k = 1
                l = []
        return sliced_list
        
    @commands.command(brief="Fetch hackathons from source")
    async def web(self,ctx, *string):
        if len(string) == 0:
            await ctx.send("```Add a website to the command to show the listed hackathons\nSupported Websites:\nMLH\nDevpost\nDevfolio```")
        else:
            website = string[0].upper()
            hackathons = get_hackathon(website)
            print(hackathons)
            if len(hackathons[0])>0:
                hackathons = list(self.parse_hackathons(hackathons))
                asset = get_asset(website)
                for i in hackathons:
                    
                    msg = discord.Embed(title=f'Hackathons listed on {website}')
                    # print(asset)
                    msg.set_thumbnail(url=asset[0]['thumbnail'])
                    # print(i[0])
                    for j in i:
                        # print(j)
                        msg.add_field(name=j['name'],value=j['url'])
                    await ctx.send(embed=msg)


def setup(bot):
    bot.add_cog(Source(bot))