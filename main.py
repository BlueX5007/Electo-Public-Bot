import discord
from discord.ext import commands
import asyncio
from config import token, prefix, owner_id
import time

intents=discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def restart(ctx):
  if ctx.author.id == owner_id:
    message = await ctx.send('Checking files...')
    time.sleep(3)
    await message.edit(content='Unloading packages...')
    time.sleep(2)
    await message.edit(content='Restarting...')
    bot.unload_extension('cogs.fun')
    bot.unload_extension('cogs.mod')
    time.sleep(10)
    bot.load_extension('cogs.fun')
    bot.load_extension('cogs.mod')
    await message.edit(content='Restarted')
  else:
    await ctx.send("You aren't the owner!")
   
@bot.command()
async def shutdown(ctx):
  if ctx.author.id == owner_id:
    await ctx.send('Shutting down...')
    bot.unload_extension('cogs.fun')
    bot.unload_extension('cogs.mod')
    
@bot.command()
async def start(ctx):
  if ctx.author.id == owner_id:
    message = await ctx.send('Starting Electro...')
    bot.load_extension('cogs.fun')
    bot.load_extension('cogs.mod')
    await message.edit(content='Started!')

bot.load_extension('cogs.fun')
bot.load_extension('cogs.mod')

bot.run(token)
