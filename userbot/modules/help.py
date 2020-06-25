# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)([\s\S]*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a valid module name.")
    else:
        await event.edit("Please specify which module do you want help for !!\
            \nUsage: .help <module name>")
        Sorrted = []
        for a in CMD_HELP:
            Sorrted.append(str(a))

        Sorrted.sort()
        string = ""
        realno = 0
        realnoPerBaris = 0
        TotalHelp = 50
        TotalPerBaris = 3
        for i in Sorrted:
            realnoPerBaris += 1
            string += "`" + str(i) + "`"
            if realnoPerBaris == TotalPerBaris:
                realno += 1
                realnoPerBaris = 0
                if realno == TotalHelp:
                    string += "\n"
                    await event.reply(string)
                    realno = 0
                    string = ""
                else:
                    string += " , "
        await event.reply(string)
