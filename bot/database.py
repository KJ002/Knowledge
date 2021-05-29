from asyncio import AbstractEventLoop
import asyncpg


class Database:
    def __init__(self, loop: AbstractEventLoop):
        self.loop = loop
        self.pool = self.loop.run_until_complete(self.create_postgres_pool())

    @staticmethod
    async def create_postgres_pool():
        credentials = {"user": "postgres", "password": "postgres", "host": "database"}
        try:
            return await asyncpg.create_pool(**credentials)
        except ConnectionRefusedError:
            print("Yo shit don't work sir")
