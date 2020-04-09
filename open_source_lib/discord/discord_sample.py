import discord

# https://discordpy.readthedocs.io/en/latest/index.html
client = discord.Client()


@client.event
async def on_ready():
    print('ON_READY!')
    print(client.user)
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('살아니'):
        await message.channel.send('옙')


client.run('token')
