import discord
import data
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='$$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    data.read_data()

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def show(ctx, *args):
    data.read_data()
    for i in data.kadai:
        await ctx.send(str(i.name) + ' ' + str(i.year) + ' ' + str(i.month)
              + ' ' + str(i.day) + ' ' + str(i.hour) + ' ' + str(i.minute)
              + ' ' + str(i.timestamp))

@bot.command()
async def add(ctx,  *, args):

    def inpl(): return list(map(str, args.split()))

    tem = inpl()
    data.add(tem)
    data.save_data()
    print('added', tem)

    await ctx.send('確かに受け取りました。')

@bot.command()
async def plus(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def dm(ctx, a: str, b: int):
    channel = bot.get_channel(b)
    await channel.send(a)

@bot.command()
async def delete(ctx, a: str):
    for i in data.kadai:
        if i.name == a:
            await ctx.send('ターゲット ' + i.name + ' を確認しました。')
            data.kadai.remove(i)
            await ctx.send('目標を殲滅しました。')

bot.run('NzEwOTcwMjkwOTE3NzM2NDY4.Xr9gWg.Bq3Pdp8E_HadJlFR2whwtL883hc')

