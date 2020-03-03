import discord
from random import randint
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('leonidas mouzalas')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    general = client.get_channel(250295196166782979)
    if message.content.lower().startswith('eae'):
        await general.send("salve")

@client.event
async def on_message(message):
    general = client.get_channel(250295196166782979)
    if message.content.lower().startswith('quantas vezes o leonidas deu a bunda hoje?'):
        bunda_leonidas = randint(1, 10)
        if bunda_leonidas == 1:
            await general.send('só uma.. ta virando macho')
        else:
            await general.send('leonidas deu a bunda {} vezes'.format(bunda_leonidas))
        if bunda_leonidas > 4:
            await general.send('mlk eh viado man kkkkkkk')
        if 4 > bunda_leonidas > 1:
            await general.send('deu pouco hj slc..')

@client.event
async def on_message(message):
    general = client.get_channel(250295196166782979)
    cuzao = banido
    if message.content.lower().startswith('!ban')
        await general.send('banir quem man')
        if mensage.content.lower().startswith(!)


client.run('Njg0NDY2NjI0Mzc1Njg1MjI2.Xl64Xg.p319Sbl34YWyT0lZetgnrk6EgvI')
