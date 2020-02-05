# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import time
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    await event.edit("Getting List notes . . .")
    time.sleep(1)
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"module `{args}` not found,please check .help again!!")
    else:
        Sorrted = []
        for a in CMD_HELP:
            Sorrted.append(str(a))

        Sorrted.sort()
        string = f"List modules:\n"
        realno = 0
        TotalHelp = len(CMD_HELP)
        
        for b in Sorrted:
            realno += 1
            string += "- `.help " + str(b) + "`\n"
            if realno == TotalHelp:
                string += f"\n\nUsage: just copy paste above "
        await event.edit(string)
