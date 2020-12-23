import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '!')

#ready
@client.event
async def on_ready():
    print('online')

#clear
@client.command(pass_context = True)
async def cl(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)

#kick
@client.command (pass_context = True)
@commands.has_permissions(administrator =True)
async def kick (ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge ( limit = 1)
    await member.kick (reason  = reason)
    await ctx.send('{} kicked'.format(member.mention))


#ban 
@client.command(pass_context = True)
@commands.has_permissions(administrator =True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason = reason)
    await ctx.send('{} baned'.format(member.mention))


client.run('NzcxMzkyNzEwNjY5MzY5Mzg1.X5rdcg.kELzcKPZcDHbNc-XUMQncL8AypQ') 