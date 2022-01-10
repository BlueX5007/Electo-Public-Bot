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
    await ctx.send(f"{member} is {x}% sus.")
  @commands.command()
  async def howgay(ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    x = random.randrange(1, 100)
    await ctx.send(f"{member} is {x}% gay.")
  @commands.command()
  async def _8ball(ctx, question):
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don't count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes, definitely.", "You may rely on it."]
    response = random.choice(responses)
    embed = discord.Embed(title="My Response", color=discord.Color.dark_magenta())
    embed.add_field(name="Your question", value=f"{question}")
    embed.add_field(name="My Response", value=f"{response} _")
    await ctx.send(embed=embed)
