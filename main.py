import discord
import secrets
from discord.ext import commands


def get_prefix(client, message):
    prefixes = ['ed.']
    if not message.guild:
        prefixes = ['!', 'ed.']
    return prefixes


cogs = ['cogs.basic']

bot = commands.Bot(
    command_prefix=get_prefix,
    description='a emoji spamming dude',
    owner_id=412235309204635649,
    case_insensitive=True
)


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    for s in bot.users:
        print(" - %s (%s)" % (s.name, s.id))
    bot.remove_command('help')
    await bot.change_presence(
        activity=discord.Streaming(
            name="Happily this aren't shown. :)",
            details="nobody beats me in emoting",
            url="https://www.youtube.com/watch?v=AvIdEoLiNk",
            type=discord.ActivityType.streaming))

    for cog in cogs:
        bot.load_extension(cog)


bot.run(secrets.TOKEN, bot=True, reconnect=True)
