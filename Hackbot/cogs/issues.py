import discord
from github import Github
from discord.ext import commands, tasks
import asyncio
import os
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
g = Github(GITHUB_TOKEN)

repo = g.get_repo("starwiz-7/HackBot")


class IssueError(commands.CommandError):
    pass

class Issue(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def create_issue(self,*issue):
        issue = issue[1]
        title = ""
        description =  ""
        if len(issue) >1:
            title = issue[0]
            description = issue[1]
            repo.create_issue(title=title, body=description)
        else:
            title = issue[0]
            repo.create_issue(title=title)
        

    @commands.guild_only()
    @commands.command(brief="Request a feature, or report an issue.")
    async def issue(self,ctx, *issue):
        self.create_issue(ctx, issue)
        await ctx.send("Reported to HackBot developer.\nhttps://github.com/starwiz-7/HackBot")

def setup(bot):
    bot.add_cog(Issue(bot))