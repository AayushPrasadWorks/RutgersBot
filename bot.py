# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Courses'):
        await message.channel.send('What is your major')
        if message.content.startswith('CS'):
            await message.channel.send('Do you have a time preference?')

    else:
        return        


client.run(TOKEN)