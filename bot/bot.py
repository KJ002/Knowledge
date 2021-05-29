import asyncio
import logging
from datetime import datetime

import aiohttp
import asyncpg
from metrics import graphite_metrics
from discord.ext.commands import Bot

from database import Database

log = logging.getLogger(__name__)


class Knowledge(Bot):
    def __init__(self, *args, **kwargs):
        self.loop = asyncio.get_event_loop()

        self.database = Database(self.loop)

        # self.redis_session = RedisSession(
        #     address=("redis://127.0.0.1:6379"),
        #     loop=loop
        # )
        # loop.run_until_complete(self.redis_session.connect())

        super().__init__(*args, **kwargs, command_prefix="!", loop=self.loop)

        # Creating session for http requests
        self.http_session = aiohttp.ClientSession(loop=self.loop)

        # Bots startup time
        self.startup_time = datetime.now()

    @staticmethod
    async def on_ready() -> None:
        print("Bot is ready")

    async def init_sql(self) -> None:
        pass



    # async def get_prefix(self, message: Message) -> str:
    #     if message.guild.id == :
    #         return "!"
    #     else:
    #         return "?"
