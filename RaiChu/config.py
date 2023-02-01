## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOKABu04UkwWIwdUgXP9mNNl1JfvgaAz2-gkcrf1sUGR0xZcea_OQEXadH0kqjqkpM6QpSvGubV8POzhekcrQjaibFS-_sJtToz4O4rhv3ckdcfUkyOp_d9Nyomblf0N9rSxPzOVhrXxW95pAmSpVfnpZ8sVJUXjgPdkqA0DODaMrYwQMxslqWJxII0c_n2ew8xDM9hLmFWM9mKPsw-NbKTzYkEBM03lPjDOKDHRMfnqbqNxjJ27OPYMH1D1I_dY7PNDjVnKiezgDeMjq1Eb4rXsZjW9G2lxO_ldhvwUGIf1EnTPv5sbhWXTaqY7ulMnIdneasUaOnli8klY2_dBqXFGX_d0=")
BOT_TOKEN = getenv("6137050988:AAEWkICs2JRgDamdzivAHze64yscA2a4UJk")
BOT_NAME = getenv("RDX MUSIC")
API_ID = int(getenv("API_ID", "20137765"))
API_HASH = getenv("API_HASH", "461d1c1a84566a810b38145947b29e83")
OWNER_NAME = getenv("OWNER_NAME", "Dreamdestroyer")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Mine_forever1bot")
BOT_USERNAME = getenv("@SHUBH_MUSIC11BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("https://t.me/D3NV1L")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("5404078241").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
