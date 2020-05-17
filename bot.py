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

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(ctx.message.author.id)

@bot.command()
async def public(ctx, *args):

    data.read_data('data.txt')
    data.sort_kadai()
    tem = []

    await ctx.send('皆様の最近の課題は以下になります。')

    if not data.kadai:
        await ctx.send('虚無です。')
    else:
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
                pass

        for i in tem:
            data.delete(i, 'data.txt')
            await ctx.send('ターゲット ' + i + ' が締切ました。目標を殲滅しました。')

@bot.command()
async def allpublic(ctx, *args):

    data.read_data('data.txt')
    data.sort_kadai()
    tem = []

    await ctx.send('皆様のすべての課題は以下になります。')

    if not data.kadai:
        await ctx.send('虚無です。')
    else:
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
            data.delete(i, 'data.txt')
            await ctx.send('ターゲット ' + i + ' が締切ました。目標を殲滅しました。')

@bot.command(pass_context=True)
async def show(ctx):

    data.read_data('Users/' + str(ctx.message.author.id) + '.txt')
    data.sort_kadai()
    tem = []

    await ctx.send(ctx.message.author.name + 'さんの最近の課題は以下になります。')

    if not data.kadai:
        await ctx.send('虚無です。')
    else:
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
                pass

        for i in tem:
            data.delete(i, 'Users/' + str(ctx.message.author.id) + '.txt')
            await ctx.send('ターゲット ' + i + ' が締切ました。目標を殲滅しました。')

@bot.command(pass_context=True)
async def showall(ctx):

    data.read_data('Users/' + str(ctx.message.author.id) + '.txt')
    data.sort_kadai()
    tem = []

    await ctx.send(ctx.message.author.name + 'さんのすべての課題は以下になります。')

    if not data.kadai:
        await ctx.send('虚無です。')
    else:
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
            data.delete(i, 'Users/' + str(ctx.message.author.id) + '.txt')
            await ctx.send('ターゲット ' + i + ' が締切ました。目標を殲滅しました。')

@bot.command()
async def addpublic(ctx,  *, args):

    data.add(args, 'data.txt')
    print('added', args)

    await ctx.send('確かに受け取りました。')

@bot.command()
async def add(ctx,  *, args):

    data.add(args, 'Users/' + str(ctx.message.author.id) + '.txt')
    print('added', args, 'to ' + str(ctx.message.author.id))
    await ctx.send(ctx.message.author.name + 'さんの課題を確かに受け取りました。')

@bot.command()
async def done(ctx, a: str):
    if data.delete(a, 'Users/' + str(ctx.message.author.id) + '.txt') == 1:
        await ctx.send(ctx.message.author.name + 'さんは ' + a + ' を完成しましたね。お疲れ様でした。')
        await ctx.send('目標を殲滅しました。')
    else:
        await ctx.send(a + 'という課題が見つかりませんでした。')

@bot.command()
async def plus(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def dm(ctx, a: str, b: int):
    channel = bot.get_channel(b)
    await channel.send(a)

@bot.command()
async def delete(ctx, a: str):
     if data.delete(a, 'data.txt') == 1:
         await ctx.send('ターゲット ' + a + ' を確認しました。')
         await ctx.send('目標を殲滅しました。')
     else:
         await ctx.send('ターゲット ' + a + ' を見つかりませんでした。')

bot.run('NzEwOTcwMjkwOTE3NzM2NDY4.XsHBCw.-Nx5peUgGIOFl1HL5fwY12Ljf0o')