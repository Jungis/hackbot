import discord
import asyncio
import os

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

        access_token = os.environ["BOT_TOKEN"]
        
client.run(access_token)
