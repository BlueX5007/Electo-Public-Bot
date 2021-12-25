from discord.ext import commands
import discord
import random
import asyncio
class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def sus(ctx, member: discord.Member):
    x = random.randrange(1, 100)
    await ctx.send(f'{member} is {x}% sus')
  @commands.command()
