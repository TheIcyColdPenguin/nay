import os
from discord.ext.commands import Bot, CommandNotFound


from dotenv import load_dotenv
load_dotenv()


bot = Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(bot.user.name, 'has logged in!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


bot.run(os.getenv('TOKEN'))
