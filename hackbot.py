import discord
import asyncio
 
client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discrod.Game(name='해킹봇 대화', type=1))

    @client.event
    async  def on_message(message):
        if message.content.startswith('!안녕하세요'):
            await client.send_message(message.channel, "안녕하세요.")

client.run('NTYxNTc4ODY3NDA4NTAyODA1.XJ-RLw.ByN0CsuHXxmduNJxZyN3DoTs9Ms')