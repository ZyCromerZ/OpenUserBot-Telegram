# Copyright (C) 2020 ZyCromerZ
#
""" Userbot lang command """

import time
from userbot import CMD_HELP, GET_LANG
from userbot.events import register
from userbot.modules.afk import AFKSTR, HELP_STR as AFK_HELP

# ================= Setup Class Start =================
class Helpstring:
    def __init__(self):
        self.isi = None
    
    def __str__(self):
        if str(GET_LANG) == "id":
            self.isi = ".setlang: untuk mengubah bahasa bot"
        else:
            self.isi = ".setlang: for change bot language"
        return self.isi
HELP_STR = Helpstring()
# ================= Setup Class End =================
@register(outgoing=True, pattern="^.setlang(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    await event.edit("Getting List notes . . .")
    time.sleep(1)
    args = event.pattern_match.group(1).lower()
    if args == "en":
        GET_LANG.change("en")
        await event.edit(f"set lang to `en` success")
    elif args == "id":
        GET_LANG.change("id")
        await event.edit(f"ubah bahasa ke `id` berhasil")
    else:
        await event.edit(f"only supported `en` and `id` ")
    HELP_STR
    AFKSTR
    AFK_HELP

CMD_HELP.update({"setlang": str(Helpstring())})