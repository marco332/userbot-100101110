# Copyright © 2020 di @D3PRESS3D telegram, <https://github.com/d3press3d>.
#
# Tutti i diritti riservati.
# 
# Crediti: @d3press3d

import asyncio
import time
import random, re
import os
import shutil

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon import events
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot import bot, AUTONAME, DEFAULT_BIO, CMD_HELP
from userbot.system import dev_cmd, command

# ================= CONSTANT =================
DEFAULTUSER = str(AUTONAME) 
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
# ============================================

@bot.on(dev_cmd(pattern="on"))  # pylint:disable=E0602
async def _(event):
    await event.edit(f"Online settato.") 
    while True:
        Online = time.strftime("[𝖔𝖓𝖑𝖎𝖓𝖊]")
        name = f"诶𝗔.𝗦.𝗗 MaRcO [𝖔𝖓𝖑𝖎𝖓𝖊]"
        logger.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        await asyncio.sleep(DEL_TIME_OUT)
        
        import asyncio
import time
import random, re
import os
import shutil

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon import events
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot import bot, AUTONAME, DEFAULT_BIO, CMD_HELP
from userbot.system import dev_cmd, command

@bot.on(dev_cmd(pattern="off"))  # pylint:disable=E0602
async def _(event):
    await event.edit(f"Offline settato.") 
    while True:
        Online = time.strftime("[𝖔𝖋𝖋𝖑𝖎𝖓𝖊]")
        name = f"诶𝗔.𝗦.𝗗 MaRcO [𝖔𝖋𝖋𝖑𝖎𝖓𝖊]"
        logger.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        await asyncio.sleep(DEL_TIME_OUT)