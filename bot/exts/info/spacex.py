from textwrap import dedent

from discord import Embed, Colour
from discord.ext.commands import Cog, command, Context, group

from bot import Knowledge
from utils.helpers import http_get

from constants import Images
import async_rediscache

API_URLS = {
    "company_info": "https://api.spacexdata.com/v3/info",
    "api_info": "https://api.spacexdata.com/v3",
}


class SpaceX(Cog):
    def __init__(self, bot: Knowledge):
        self.bot = bot
        self.cache = async_rediscache.RedisCache(namespace="SpaceX")

    @group()
    async def spacex(self, ctx: Context):
        pass

    @spacex.command(name="company")
    async def company_info_command(self, ctx: Context) -> None:
        """Returns an embed the contains information about the SpaceX company"""
        async with ctx.typing():
            json_response = await http_get(ctx, url=API_URLS["company_info"])

            embed = Embed(
                title=json_response["name"],
                url=json_response["links"]["website"],
                description=json_response["summary"],
                colour=Colour.blurple()
            )

            embed.set_thumbnail(url=Images.SPACEX_LOGO)

            embed.add_field(name="__About:__", value=dedent(f"""
                 - **Founder**        `{json_response["founder"]}`
                 - **Founded In**     `{json_response["founded"]}`
                 - **Employees**      `{json_response["employees"]}`
                 - **Vehicles**       `{json_response["vehicles"]}`
                 - **Launch Sites**   `{json_response["launch_sites"]}`
                 - **Test Sites**     `{json_response["test_sites"]}`
            """))

            embed.add_field(name="__Chief Officers:__", value=dedent(f"""
                 - **CEO**            `{json_response["ceo"]}`
                 - **CTO**            `{json_response["cto"]}`
                 - **COO**            `{json_response["coo"]}`
                 - **CTO-P**          `{json_response["cto_propulsion"]}`
            """))

            embed.add_field(name="__Social Media:__", value=dedent(f"""
                 - [Flickr]({json_response["links"]["flickr"]})
                 - [Twitter]({json_response["links"]["twitter"]})
                 - [Elon's Twitter]({json_response["links"]["elon_twitter"]})
            """), inline=False)

            embed.set_image(url=Images.SPACEX_BANNER)

            await ctx.reply(embed=embed)

    @spacex.command()
    async def api_info(self, ctx: Context) -> None:
        """Returns an embed the contains information about the SpaceX API"""
        async with ctx.typing():
            json_response = await http_get(ctx, url=API_URLS["api_info"])
            print(json_response)
            embed = Embed(
                title=json_response["project_name"],
                url=json_response["project_link"],
                description=json_response["description"],
                colour=Colour.blurple()
            )

            embed.set_thumbnail(url=Images.SPACEX_LOGO)

            embed.add_field(name="__Info:__", value=dedent(f"""
                 - Version: `{json_response["version"]}`
                 - [Docs]({json_response["docs"]})
                 - [{json_response["organization"]}]({json_response["organization_link"]})            
            """))

            embed.set_image(url=Images.SPACEX_BANNER)

            await ctx.reply(embed=embed)


def setup(bot: Knowledge) -> None:
    """Loads the SpaceX cog."""
    bot.add_cog(SpaceX(bot))

