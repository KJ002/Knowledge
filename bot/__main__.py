from discord import Intents, Message
from dotenv import load_dotenv

from bot import Knowledge
from constants import Config

load_dotenv()

bot = Knowledge(
    help_command=None,
    intents=Intents(
        guilds=True,
        members=True,
        bans=True,
        emojis=True,
        integrations=False,
        webhooks=False,
        invites=True,
        voice_states=True,
        presences=True,
        messages=True,
        reactions=True,
        typing=False
    )
)

initial_extensions = [
    # APIs
    "exts.info.spacex",

    "exts.utility_commands.info"

]

for extension in initial_extensions:
    bot.load_extension(extension)

bot.run(Config.TOKEN)
