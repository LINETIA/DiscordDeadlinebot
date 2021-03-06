import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='//')
client = discord.Client()

prpr_cnt = 0
tql_cnt = 0
kusa_cnt = 0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='クラウ＝ソラス'))

@client.event
async def on_message(message):
    global prpr_cnt
    global tql_cnt
    global kusa_cnt

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
        if prpr_cnt == 1:
            await message.channel.send('この行為に何らかの不埒の意味は？')
        elif prpr_cnt == 2:
            await message.channel.send('おやめください。')
        elif prpr_cnt == 3:
            await message.channel.send('やっぱり何らかの不埒の意図が？')
        else:
            await message.channel.send('おやめください。')
            prpr_cnt = 0

    if message.content == 'tql':
        tql_cnt += 1
        if tql_cnt == 1:
            await message.channel.send('すごいです。')
        elif tql_cnt == 2:
            await message.channel.send('。。。すごいです。')
        elif tql_cnt == 3:
            await message.channel.send('ほえぇ。')
            tql_cnt = 0

    if message.content == '牛逼' or message.content == 'nb':
        await message.channel.send('ニュービーです。')
    if message.content == '草' or message.content == '艹' or message.content == 'cao':
        kusa_cnt += 1
        if kusa_cnt == 1:
            await message.channel.send('草です。')
        elif kusa_cnt == 2:
            kusa_cnt = 0

    if message.content == '我起了':
        await message.channel.send("おはようございます" + message.author.name + "さん。")
    if message.content == '睡了' or message.content == '我睡了' \
            or message.content == '我先睡了' or message.content == \
            '我要睡了' or message.content == '我也睡了' \
            or message.content == '我先睡觉了' or message.content == '我去睡觉了' or message.content == '我先去睡觉了':
        await message.channel.send('おやすみなさい。+ message.author.name + "さん。"')
    if message.content == '我太菜了' or message.content == '太菜了':
        await message.channel.send('弱いです。')

    await bot.process_commands(message)

client.run("token")
