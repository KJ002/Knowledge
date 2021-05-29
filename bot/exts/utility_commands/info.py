from textwrap import dedent

from discord import Embed, Colour
from discord.ext.commands import Cog, command, Context

from bot import Knowledge


class Information(Cog):
    def __init__(self, bot: Knowledge):
        self.bot = bot

    @command(name="server", aliases=("server_info", "guild", "guild_info"))
    async def server_command(self, ctx: Context) -> None:
        """Returns embed containing server information."""
        embed = Embed(title=ctx.guild.name, colour=Colour.blurple(), timestamp=ctx.message.created_at)

        embed.set_thumbnail(url=ctx.guild.icon_url)

        # Embed Description
        created = ctx.guild.created_at.strftime("%A, %B %d, %Y %H:%M:%S UTC")
        guild_owner = f"<@{ctx.guild.owner_id}>"
        member_count = ctx.guild.member_count

        embed.description = textwrap.dedent(f"""
            Created:    `{created}`
            Members:    `{member_count}`
            Guild Owner: {guild_owner}
        """)

        # Channels
        voice_channels = len(ctx.guild.voice_channels)
        text_channels = len(ctx.guild.channels)
        stage_channels = len(ctx.guild.stage_channels)
        voice_region = ctx.guild.region
        afk_channel = f"<#{ctx.guild.afk_channel.id}>"
        afk_timeout = round(ctx.guild.afk_timeout / 60)
        bitrate_limit = round(ctx.guild.bitrate_limit / 1000)
        max_video_channel_users = ctx.guild.max_video_channel_users

        text_channels = len(ctx.guild.channels)

        embed.add_field(name="Channel Info", value=dedent(f"""
            **Voice**
            Voice Channels:          `{voice_channels}`
            Stage Channels:          `{stage_channels}`
            Voice Region:            `{voice_region}`
            AFK Channel:              {afk_channel}
            AFK Timeout:             `{afk_timeout} minutes`
            Bitrate Limit:           `{bitrate_limit}kbps`
            Max Video Channel Users: `{max_video_channel_users}`
            
            **Text**
            Text Channels:           `{text_channels}`
            
        """), inline=True)

        # Server
        max_members = ctx.guild.max_members
        chunked = ctx.guild.chunked
        shard_id = ctx.guild.shard_id
        emoji = len(ctx.guild.emojis)
        emoji_limit = ctx.guild.emoji_limit
        roles = len(ctx.guild.roles)
        default_role = ctx.guild.default_role
        default_notifications = ctx.guild.default_notifications

        if default_notifications == "NotificationLevel.only_mentions":
            default_notifications = "Only Mentions"
        else:
            default_notifications = "All Mentions"

        try:
            nitro_booster_role = ctx.guild.premium_subscriber_role.mention
        except AttributeError:
            nitro_booster_role = "`None`"

        nitro_boosters = ctx.guild.premium_subscription_count
        server_boost_tier = ctx.guild.premium_tier

        embed.add_field(name="Server", value=textwrap.dedent(f"""
            Max Members:           `{member_count}/{max_members}`
            Chunked:               `{chunked}`
            Shard ID:              `{shard_id}`
            Emojis:                `{emoji}/{emoji_limit}`
            Roles:                 `{roles}`
            Default Role:           {default_role}
            Default Notifications: `{default_notifications}`
            
            **Nitro**
            Nitro Role:             {nitro_booster_role}
            Nitro Boosts:          `{nitro_boosters}`
            Server Boost Tier:     `{server_boost_tier}`
        """), inline=True)

        await ctx.send(embed=embed)


def setup(bot: Knowledge) -> None:
    """Loads the Information cog."""
    bot.add_cog(Information(bot))
