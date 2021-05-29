from discord.ext.commands import Cog, command, Context

from bot import Knowledge


class Setup(Cog):
    def __init__(self, bot: Knowledge):
        self.bot = bot

    @command()
    async def set_prefix(self, ctx: Context, prefix: str) -> None:
        pass


def setup(bot: Knowledge) -> None:
    """Loads the SpaceX cog."""
    bot.add_cog(Setup(bot))