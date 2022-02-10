import discord
import os, random

anekdotList = ['Однажды мужчина пришел к старцу, который жил 200 лет. И спросил: '
               '"Старец, в чем Ваш секрет? Почему Вы так долго живете?'
               'Старец отвечает: "Всё просто, я просто никогда ни с кем не спорил."'
               '- Но как? Это же не возможно.'
               '- Возможно.'
               'И сдох Н@хуй']


TOKEN = 'OTQxMzg3NzgwNjMyNzM5OTMw.YgVNsQ.7IO0vfC5iKoI1LlhbiaU66ZkMGY'



class MyClient(discord.Client):

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('!anekdot'):
            await message.channel.send(random.choice(list(anekdotList)))


client = MyClient()
client.run('OTQxMzg3NzgwNjMyNzM5OTMw.YgVNsQ.zRg3bunaXH2qzYjgTVQU6k7Qs20')
