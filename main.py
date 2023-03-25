import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents = intents)

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
        await message.channel.send("You can use\n!explain")
    elif "!explain" in message.content:
        await message.channel.send("This is a Discord Bot created by Andrei Vince.\nIt's just a project, but if it's worth it, I will make updates.")        






client.run("MTA4OTIyNDIxNDg2ODkyMjQ4MA.GJPy_o.wld7rCM0Hlk1aKkA6Qzc6V7rUnnxFg4N-E7API")