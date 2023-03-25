import discord
import hide
import requests

# Use a descriptive variable name for the API key
NEWS_API_KEY = hide.news_API

# Define constants for the API URL and number of articles to display
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={NEWS_API_KEY}"
NUM_ARTICLES = 10

# Set up the Discord client and intents
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

# Make the initial API request outside of the event handlers
# and handle any errors that might occur
try:
    response = requests.get(NEWS_API_URL)
    response.raise_for_status()
    articles = response.json()['articles'][:NUM_ARTICLES]
except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:
    print(f"Failed to fetch news articles: {e}")
    articles = []

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

# Define an event handler for when a message is received
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    # Respond to greetings
    elif message.content.startswith(("hey", "hello", "hi")):
        await message.channel.send("Hello")
    
    # Respond to help command
    elif message.content.startswith("!help"):
        await message.channel.send("You can use\n!explain\n!news")
    
    # Respond to explain command
    elif message.content.startswith("!explain"):
        await message.channel.send("This is a Discord Bot created by Andrei Vince.\nIt's just a project, but if it's worth it, I will make updates.")
    
    # Respond to news command
    elif message.content.startswith("!news"):
        if articles:
            await message.channel.send("Here are the top headlines in technology news:")
            for article in articles:
                await message.channel.send(article['title'])
        else:
            await message.channel.send("Sorry, I couldn't fetch any news articles. Please try again later.")

# Run the client with the Discord bot token
client.run(hide.Token)
