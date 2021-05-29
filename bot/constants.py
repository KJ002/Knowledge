import os
from typing import NamedTuple

from dotenv import load_dotenv

__all__ = ("Config")

load_dotenv()


class Config(NamedTuple):
    TOKEN = os.environ.get("TOKEN")
    PREFIX = "!"

class Images(NamedTuple):
    SPACEX_LOGO = "https://cdn.discordapp.com/attachments/847875752988639272/847905818904887386/external-content.duckduckgo.png"
    SPACEX_BANNER = "https://cdn.discordapp.com/attachments/847875752988639272/847893473364672572/851806.png"
