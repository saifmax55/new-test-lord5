import discord
import asyncio

# قم بتعيين توكن البوت الخاص بك هنا
TOKEN = 'MTIzOTE5NzgxOTM4MzA1NDM2Ng.GijoUw.aJN7Ghn7k2d9MXQpIlOnH3d2dRIWlMd12hoDNY'
# قم بتعيين ID القناة التي تريد إرسال الرسالة إليها هناf5
CHANNEL_ID = 1239194381186105408

# إنشاء عميل البوت مع تعيين الـ intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    # تعيين الحالة إلى "Watching" وتحديد اسم البث والرابط والصورة المتحركة
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='(=ﾟ㉨ﾟ=) ▄︻┻┳━ ·.`.`.`. shadow lord', url='https://twitch.tv/mychannel', details='Streaming on Twitch', state='Hunter,s 🃏', large_image='https://media.discordapp.net/attachments/1239235113716416655/1239239389033271388/5eb89355092c5009ace003e148d6c7b5.gif?ex=6642331e&is=6640e19e&hm=0e464aec0f7bce90437f5410a60422df9eb55db91415080c5eb01af48a43fce2&'))

    # يقوم البوت بإرسال رسالة بنص عادي بدلاً من Embed بشكل متكرر
    channel = client.get_channel(CHANNEL_ID)
    while True:
        await channel.send('مرحبا، كيف يمكنني مساعدتك؟')
        await asyncio.sleep(1)  # تأخير لمدة ثانية واحدة قبل إرسال الرسالة التالية

client.run(TOKEN)