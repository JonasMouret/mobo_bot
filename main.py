import hikari

bot = hikari.GatewayBot(token="OTkxMjg4Njk1OTU1MTMyNTE4.GTOTc5.0CqLmwVYTBozrcct_ddM7KHAwtoGU-ZC8B-7yw")

print('Starting bot...')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.message.content)
    print("Message")
    print(event.content)


bot.run()