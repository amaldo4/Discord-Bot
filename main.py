from discord.ext.commands import Bot
import datetime
import collections

TOKEN = 'pfffft'

client = Bot('!')
birthDict = collections.defaultdict(str)


@client.event
async def on_ready():
    print("We have logged in as {0.user}" .format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'bot-shit':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello, {username}! Whats up?')
            return
        if user_message.lower() == 'date':
            currentDate = datetime.datetime.now()
            test = currentDate.strftime('%m-%d-%y')
            await message.channel.send(f'Current date is {test}!')
            return
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return

@client.command()
async def addbday(ctx):
    await ctx.send("Enter birthdate in form MM-DD-YY")
    def check(m):
        return m.author.id == ctx.author.id

    msg = await client.wait_for('message', check=check)
    await ctx.send(f'birthday is {msg}')
    


client.run(TOKEN)
