import discord
import hide
import requests

get_api = hide.news_API

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents = intents)

URL = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={get_api}"
response = requests.get(URL)

@client.event
async def on_ready():
    print("Hello {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("hey") or message.content.startswith("hello") or message.content.startswith("hi"):
        await message.channel.send("Hello")
    elif message.content.startswith("!help"):
        await message.channel.send("You can use\n!explain\n!news")
    elif "!explain" in message.content:
        await message.channel.send("This is a Discord Bot created by Andrei Vince.\nIt's just a project, but if it's worth it, I will make updates.")        
    elif message.content.startswith("!news"):
        await message.channel.send("This is the news about Technology")
        articles = response.json()['articles'][:10]
        for article in articles:
            await message.channel.send(article['title'])

client.run(hide.Token)
