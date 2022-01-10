from discord import colour
from discord.ext import commands
import discord
import random
import asyncio
import datetime
import humanfriendly
#Functions for the bot to work
def convert(time):
  pos = ["s","m","h","d"]

  time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2

  return val * time_dict[unit]

#The command listeners
class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        author_roles = ctx.author.roles
        member_roles = member.roles
        member_top_role = member_roles[-1]
        author_top_role = author_roles[-1]
        if ctx.author.id == ctx.guild.owner.id:
            member.kick(reason=f"{reason} | Action taken by {ctx.author}")
            embed = discord.Embed(title='Success', description='Successfully kicked member/user!', color=discord.Color.brand_green())
            await ctx.send(embed=embed)
        elif member_top_role > author_top_role or author_top_role == member_top_role:
            embed = discord.Embed(title='Error!', description='You are not allowed to kick that member/user', color=discord.Color.dark_red())
            await ctx.send(embed=embed)
        else:
            member.kick(reason=f"{reason} | Action taken by {ctx.author}")
            embed = discord.Embed(title='Success', description='Successfully kicked member/user!', color=discord.Color.brand_green())
            embed.add_field(name='Credits', value="       (This bot was forked from https://github.com/BlueX5007/Electo-Public-Bot)         ")
            await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        author_roles = ctx.author.roles
        member_roles = member.roles
        member_top_role = member_roles[-1]
        author_top_role = author_roles[-1]
        if ctx.author.id == ctx.guild.owner.id:
            await ctx.guild.ban(member, reason=f"{reason} | Action taken by {ctx.author}")
            embed = discord.Embed(title='Success', description='Successfully banned member/user!', color=discord.Color.brand_green())
            await ctx.send(embed=embed)
        elif member_top_role > author_top_role or author_top_role == member_top_role:
            embed = discord.Embed(title='Error!', description='You are not allowed to ban that member/user', color=discord.Color.dark_red())
            await ctx.send(embed=embed)
        else:
            await ctx.guild.ban(member, reason=f"{reason} | Action taken by {ctx.author}")
            embed = discord.Embed(title='Success', description='Successfully banned member/user!', color=discord.Color.brand_green())
            await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx,*, reason4 = 'No reason provided.'):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed=discord.Embed(title='Channel Locked!', description=f'{ctx.channel.mention} is successfully locked by {ctx.author.mention}!', colour=discord.Colour.red())
        embed.add_field(name='Reason', value=f'{reason4}')
        embed.add_field(name='Credits', value='(This bot was forked from https://github.com/BlueX5007/Electo-Public-Bot)')
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx,*, reason3 = 'No reason provided.'):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed=discord.Embed(title='Channel Unlocked!', description=f'{ctx.channel.mention} is successfully unlocked by {ctx.author.mention}!', colour=discord.Colour.green())
        embed.add_field(name='Reason', value=f'{reason3}')
        embed.add_field(name="Credits", value="(This bot was forked from https://github.com/BlueX5007/Electo-Public-Bot)")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def dm(self, ctx, member: discord.Member,*, rdm):
        embed=discord.Embed(title=f'You got a DM from {ctx.guild.name} ({ctx.guild.id})', description=f'{rdm}')
        embed.add_field(name='_ _', value=f'This was sent by {ctx.author} ({ctx.author.id})')
        await member.send(embed=embed)
        await ctx.send(f'DMed {member}   (This bot was forked from https://github.com/BlueX5007/Electo-Public-Bot)')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, time):
        pos = ["s","m","h"]
        unit = time[-1]
        if unit not in pos:
            await ctx.send('Invalid units, the units are **s, m, h**')
        else:
            seconds = convert(time)
            if seconds > 21600: 
                await ctx.send("Can't set slowmode over 6 hours!")
            else:
                await ctx.channel.edit(slowmode_delay=seconds)
                await ctx.send(f"Set the slowmode for this channel to {time}!")


    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx,member:discord.Member,timee,*,reason):
        pos = ["s","m","h","d"]
        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24} 
        now = datetime.datetime.now()
        roles_author = ctx.author.roles
        toprole_author = roles_author[-1]
        roles_member = member.roles
        toprole_member = roles_member[-1]
        if member.id == ctx.author.id:
            await ctx.send("Cannot mute yourself.")
        elif toprole_author < toprole_member:
            await ctx.send(f'{member} has a higher role than you!')
        elif toprole_author == toprole_member:
            await ctx.send(f'{member} has a equal role with you!')
        else:
            time = humanfriendly.parse_timespan(timee)
            await member.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=time), reason = f"{reason} | Action was taken by {ctx.author}")
            embed = discord.Embed(title='Muted user!', description=f"Muted {member} for {timee}!", colour=discord.Colour.dark_teal())
            embed.add_field(name='Credits', value='(This bot was forked from https://github.com/BlueX5007/Electo-Public-Bot)')
            await ctx.send()

def setup(bot):
    bot.add_cog(Mod(bot))
