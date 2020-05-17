import discord
import data
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='//')

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

    data.sort_kadai()
    tem = []
    for i in data.kadai:

        now = datetime.now()
        difference = i.timestamp - now.timestamp()
        if difference < 0:
            tem.append(i.name)
            await ctx.send(str(i.name).ljust(12, '　') + '    締切：' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(data.append_zero(i.minute)))

        elif difference <= 259200:
            await ctx.send(str(i.name).ljust(12, '　') + '    締切:' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(data.append_zero(i.minute)) + '   '
                           + '締切まであと' + str(round(difference / 60 / 60, 1)) + '時間です。頑張ってください。')
        elif difference <= 604800:
            await ctx.send(str(i.name).ljust(12, '　') + '    締切：' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(data.append_zero(i.minute)))
        else:
            pass

    for i in tem:
        data.delete(i)
        await ctx.send('ターゲット ' + i + ' が締切ました。目標を殲滅しました。')

@bot.command()
async def showall(ctx, *args):

    data.sort_kadai()
    tem = []
    for i in data.kadai:

        now = datetime.now()
        difference = i.timestamp - now.timestamp()
        if difference < 0:
            tem.append(i.name)
            await ctx.send(str(i.name).ljust(12, '　') + '    締切：' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(
                data.append_zero(i.minute)))

        elif difference <= 259200:
            await ctx.send(str(i.name).ljust(12, '　') + '    締切:' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(
                data.append_zero(i.minute)) + '   '
                           + '締切まであと' + str(round(difference / 60 / 60, 1)) + '時間です。頑張ってください。')
        elif difference <= 604800:
            await ctx.send(str(i.name).ljust(12, '　') + '    締切：' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(
                data.append_zero(i.minute)))
        else:
            await ctx.send(str(i.name).ljust(12, '　') + '    締切：' + str(i.year) + '-' + str(i.month)
                           + '-' + str(i.day) + ' ' + str(data.append_zero(i.hour)) + ':' + str(
                data.append_zero(i.minute)))

    for i in tem:
        data.delete(i)
        await ctx.send('ターゲット ' + i + ' が締切ました。目標を殲滅しました。')

@bot.command()
async def add(ctx,  *, args):

    def inpl(): return list(map(str, args.split()))

    tem = inpl()
    data.add(tem)
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
     if data.delete(a) == 1:
         await ctx.send('ターゲット ' + a + ' を確認しました。')
         await ctx.send('目標を殲滅しました。')
     else:
         await ctx.send('ターゲット ' + a + ' を見つかりませんでした。')

bot.run('NzEwOTcwMjkwOTE3NzM2NDY4.XsAqDQ.d3NDhAhooe3Bdz3msfhHMxbCF5s')

