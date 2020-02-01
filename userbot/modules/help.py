# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"module `{args}` not found,please check .help again!!")
    else:
        await event.edit("List modules:")
        string = ""
        realno = 0
        TotalHelp = len(CMD_HELP)
        for i in CMD_HELP:
            realno += 1
            string += "`" + str(i)
            if realno == TotalHelp:
                string += f"`\n\n\nUsage: .help <module name>"
            else:
                string += f"`  `[0]`  "
        await event.reply(string)
