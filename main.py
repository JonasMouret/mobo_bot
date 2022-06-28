import hikari
import os

bot = hikari.GatewayBot(token=os.environ['DISCORD_TOKEN'])

print('Starting bot...')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.message.content)
    print("Message")
    print(event.content)


bot.run()