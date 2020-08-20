# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @100101110
#
"""Commands:
.tette"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern="tette", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "mattia":
    await event.edit("tette")
    animation_chars = [

            "Come_",

            "Disse_",

            "Padre_",

            "Pio_",
            
            "Tette_",
            
            "In_",
            
            "Chat_",
            
            "E_",
            
            "Premi_",
            
            "Invio_",
            
            "Come Disse Padre Pio Tette In Chat E Premi Invio 😍",
     
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])