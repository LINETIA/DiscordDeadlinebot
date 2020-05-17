import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='//')
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='クラウ＝ソラス'))

@client.event
async def on_message(message):

    prpr_cnt = 0

    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("hi") or message.content.startswith("Hi"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            if message.author.name == "Linetia":
                m = "おはようございます、教官。"
                await message.channel.send(m)
            else:
                # メッセージを書きます
                m = "おはようございます" + message.author.name + "さん。"
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await message.channel.send(m)

    if message.content == 'neko':
        await message.channel.send('にゃーん。')

    if message.content == 'prpr':
        prpr_cnt += 1
        if prpr_cnt % 2 == 1:
            await message.channel.send('この行為に何らかの不埒の意味は？')
        else:
            await message.channel.send('おやめください。')

    if message.content == 'tql':
        await message.channel.send('すごいです。')
    if message.content == '牛逼':
        await message.channel.send('ニュービーです。')
    if message.content == '草' or message.content == '艹' or message.content == 'cao':
        await message.channel.send('草です。')
    if message.content == '我起了':
        await message.channel.send("おはようございます" + message.author.name + "さん。")
    if message.content == '睡了' or message.content == '我睡了' \
            or message.content == '我先睡了' or message.content == \
            '我要睡了' or message.content == '我也睡了' \
            or message.content == '我先睡觉了' or message.content == '我去睡觉了':
        await message.channel.send('おやすみなさい。+ message.author.name + "さん。"')
    if message.content == '我太菜了' or message.content == '太菜了':
        await message.channel.send('弱いです。')

    await bot.process_commands(message)

client.run("NzEwOTcwMjkwOTE3NzM2NDY4.XsGzEA.CGgl1L6uhIGL0kCJuJ0AA3OrSXI")
