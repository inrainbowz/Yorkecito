from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix=',')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name='test')
async def saludo(ctx):
    response = 'No test'
    await ctx.send(response)

bot.run(TOKEN)