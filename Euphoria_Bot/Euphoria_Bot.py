
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

@bot.command()
async def echo(ctx, *args):
    await ctx.send(' '.join(args))

bot.run('') #token needed