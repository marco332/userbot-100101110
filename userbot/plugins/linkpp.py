"""
Commandi:
.link
"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("link?(.*)", outgoing=True))
async def sup(e):
    await e.edit(
        "\nPaypal ufficiale di @MaRcOiSmAd: \nhttps://www.paypal.me/pefavore")