# bot.py
import os

import discord
import http.client
import requests
import urllib
import re

from pprint import pprint
from dotenv import load_dotenv
from urllib.parse import urlencode, urlunparse
from bs4 import BeautifulSoup
from test import classes_by_major, classes_by_dep_course_level, classes_by_dep_course_number




load_dotenv()
TOKEN = os.getenv('TOKEN')

subscriptionKey = '574acb6b-b948-4ae8-99aa-2e5e34f20017'
host = 'api.bing.microsoft.com'
path = '/v7.0/entities'
endpoint = "https://management.azure.com/"+"/bing/v7.0/search"
mkt = 'en-US'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Help Me!":
        channel = message.channel
        def check(m):
            return (m.content != ' ' and m.content != None) and m.channel == channel

        await message.channel.send('What do you need help in? \n if you need to view courses, say !Courses')
        msg = await client.wait_for('message', check=check)

        if msg.content == '!Courses':

            await message.channel.send('State your Major')
            def c(m):
                string = m.content.upper()
                if classes_by_major(string) == None:
                    return 0
                return (m.content != ' ' and m.content != None) and m.channel == channel

            major = await client.wait_for('message', check=c)
            await message.channel.send('Want to be more specfic? Respond yes/no')
            
            def ch(m):
                
                if m.content != 'yes' and m.content != 'no':
                    return 0
                return (m.content != ' ' and m.content != None) and m.channel == channel
            
            conform = await client.wait_for('message', check=ch)

            if conform.content == 'no':
                print("Successfull")
                await message.channel.send('Here are your filtered Courses')
                list = classes_by_major(major.content.upper())
                for course in list:
                  await message.channel.send(course)
                return
            else: 
                await message.channel.send('Do you want your courses sorted by year?')
                def chk(m):
                    if m.content != 'yes' and m.content != 'no':
                        return 0
                    return (m.content != ' ' and m.content != None) and m.channel == channel
                con = await client.wait_for('message', check=chk)

                if con.content == 'yes':

                   await message.channel.send('State Your year: 100 for freshman, 200 for sophmore, 300 for junior, 400 for senior')
                   def ck(m):
                     if m.content.isnumeric():
                       if classes_by_dep_course_number(major.content.upper(), m.content) == None:
                          return 0
                       return 1
                     return 0

                   number = await client.wait_for('message', check=ck)
                   await message.channel.send('Here are your filtered Courses')
                   list = classes_by_dep_course_level(major.content.upper(), number.content)
                   print(list)
                   for course in list:
                      await message.channel.send(course)
                   return
                else:
                    await message.channel.send('State Course Code')

                    def ck(m):
                     if m.content.isnumeric():
                       if classes_by_dep_course_number(major.content.upper(), m.content) == None:
                          return 0
                       return 1
                     return 0

                    number = await client.wait_for('message', check=ck)
                    await message.channel.send('Here are your filtered Courses')
                    list = classes_by_dep_course_level(major.content.upper(), number.content)
                    for course in list:
                      await message.channel.send(course)
                    return
                     
                return


            



        else: 
            await message.channel.send('I hope these links help!')
            list = search(msg)
            for i in range(5):
                await message.channel.send(list[i])
            return 
       


    

def search(query):
    thislist = []
    page = requests.get("https://www.google.com/search?q="+query.content)
    soup = BeautifulSoup(page.content)
    links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
    for link in links:
        thislist.append(re.split(":(?=http)",link["href"].replace("/url?q=","")))
    return thislist

client.run(TOKEN)