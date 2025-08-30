import discord
from today import today

# Creating a client instance
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():                           # Print a message when the bot turns on
    print(f'We have logged in as {client.user}')

@client.event                                   
async def on_message(message):                  
    if message.author == client.user:           # Check if the message was sens by the bot
        return

    if message.content.startswith("edt?"):      # Check if the message starts with 'edt', which is the command we defined to view the timetable.
        await message.channel.send(today())

client.run("PUT YOUR TOKEN HERE")

