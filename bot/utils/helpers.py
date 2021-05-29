from typing import Any

from discord.ext.commands import Context


async def http_get(ctx: Context, url: str) -> Any:
    """Helper function that returns a json from an url"""
    async with ctx.bot.http_session.get(url) as response:
        return await response.json()
