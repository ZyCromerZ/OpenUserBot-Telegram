# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version

from userbot import CMD_HELP, ALIVE_NAME, BOT_NAME
from userbot.events import register
from userbot.modules.lang import lang

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.sysd$")
async def sysdetails(sysd):
    """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await sysd.edit("`" + result + "`")
    except FileNotFoundError:
        if str(lang) == "id":
            await sysd.edit("`neofetch ga ada,Install dulu gih!`")
        else:
            await sysd.edit("`Install neofetch first !!`")


@register(outgoing=True, pattern="^.botver$")
async def bot_ver(event):
    """ For .botver command, get the bot version. """
    if which("git") is not None:
        invokever = "git describe --all --long"
        ver = await asyncrunapp(
            invokever,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        invokerev = "git rev-list --all --count"
        rev = await asyncrunapp(
            invokerev,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        if str(lang) == "id":
            await event.edit(f"Tentang BOT:\n"
                            f"Versi Userbot: `{verout}`\n"
                            f"Revisi: `{revout}`\n"
                            f"Telethon: ` {version.__version__} ` \n"
                            f"Python: ` {python_version()} ` \n"
                            f"")
        else:
            await event.edit(f"About BOT:\n"
                            f"Userbot Version: `{verout}`\n"
                            f"Revision: `{revout}`\n"
                            f"Telethon: ` {version.__version__} ` \n"
                            f"Python: ` {python_version()} ` \n"
                            f"")
    else:
        if str(lang) == "id":
            await event.edit(
                "Wew ga support git, lagi jalan di 5.0 - 'Extended'"
            )
        else:
            await event.edit(
                "Shame that you don't have git, You're running 5.0 - 'Extended' anyway"
            )


@register(outgoing=True, pattern="^.pip(?: |$)(.*)")
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`"
                           f"{pipout}"
                           "`")
        else:
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`No Result Returned/False`")
    else:
        await pip.edit("`Use .help pip to see an example`")


@register(outgoing=True, pattern="^.on$")
async def amireallyalive(on):
    """ For .on command, check if the bot is running.  """
    if str(lang) == "id":
        await on.edit(f"Dah Siap boss \n\n"
                    f"`------------------------------------` \n"
                    f"User: ` {DEFAULTUSER} ` \n"
                    f"NamaBot: `{BOT_NAME}` \n"
                    f"Bahasa: `{lang}`\n"
                    f"`------------------------------------` \n"
                    f" \n\n"
                    f"Santuy . . .")
    else:
        await on.edit(f"I'm Ready \n\n"
                    f"`------------------------------------` \n"
                    f"User: ` {DEFAULTUSER} ` \n"
                    f"Botname: `{BOT_NAME}` \n"
                    f"lang: `{lang}`\n"
                    f"`------------------------------------` \n"
                    f" \n\n"
                    f"Enjoy . . .")



@register(outgoing=True, pattern="^.aliveu")
async def amireallyaliveuser(username):
    """ For .aliveu command, change the username in the .alive command. """
    message = username.text
    if str(lang) == "id":
        output = '.aliveu [user baru] tidak boleh kosong'
    else:
        output = '.aliveu [new user without brackets] nor can it be empty'
    if not (message == '.aliveu' or message[7:8] != ' '):
        newuser = message[8:]
        global DEFAULTUSER
        DEFAULTUSER = newuser
        if str(lang) == "id":
            output = 'berhasil mengubah user ke ' + newuser + '!'
        else:
            output = 'Successfully changed user to ' + newuser + '!'
    await username.edit("`" f"{output}" "`")


@register(outgoing=True, pattern="^.resetalive$")
async def amireallyalivereset(ureset):
    """ For .resetalive command, reset the username in the .alive command. """
    global DEFAULTUSER
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    if str(lang) == "id":
        await ureset.edit("berhasil reset user untuk `alive`!")
    else:
        await ureset.edit("Successfully reset user for `alive`!")

@register(outgoing=True, pattern="^.bcname(?: |$)(.*)")
async def cbotname(btname):
    """ For .bcname command, change botname """
    BOT_NAME.reset()
    if str(lang) == "id":
        await dbname.edit(f"ubah nama bot ke `{botName}` berhasil")
    else:
        await dbname.edit(f"change botname to `{botName}` success")

@register(outgoing=True, pattern="^.brname")
async def rbotname(dbname):
    """ For .brname command, change botname """
    botName = dbname.pattern_match.group(1)
    if botName:
        BOT_NAME.change(botName)
        if str(lang) == "id":
            await dbname.edit(f"ubah nama bot ke `{botName}` berhasil")
        else:
            await dbname.edit(f"change botname to `{botName}` success")
    else:
        if str(lang) == "id":
            await dbname.edit(f"nama bot tidak ditemukan,sialahkan check di ``.help botname` buat detailnya")
        else:
            await dbname.edit(f"botname notfound,check `.help botname` for more details")

    
class Helpstring:
    def __init__(self):
        self.string = None;
    def get(self):
        if str(lang) == "id":
            return [
                ".sysd\
                \nGunanya: liat info system pake neofetch.",

                ".botver\
                \nGunanya: liat userbot version.",

                ".pip <module(s)>\
                \nGunanya: buat nyari pip modules(s).",
                
                ".on\
                \nGunanya: ketik .on buat liat bot nyala ato mati.\
                \n\n.aliveu <text>\
                \nGunanya: buat ganti 'user' di alive ke yg lu mau.\
                \n\n.resetalive\
                \nGunanya: Reset  `user` ke default.",

                ".bcname <namabot> \
                \nUsage: Ketik .bcname <namabot> buat ubah nama bot \
                \n.brname \
                \nUsage: buat reset nama bot nya ke default"
            ]
        else:
            return [
                ".sysd\
                \nUsage: Shows system information using neofetch.",

                ".botver\
                \nUsage: Shows the userbot version.",

                ".pip <module(s)>\
                \nUsage: Does a search of pip modules(s).",

                ".on\
                \nUsage: Type .on to see wether your bot is working or not.\
                \n\n.aliveu <text>\
                \nUsage: Changes the 'user' in alive to the text you want.\
                \n\n.resetalive\
                \nUsage: Resets the user to default.",

                ".bcname <botname> \
                \nUsage: Type .bcname <botname> to change bot name \
                \n.brname \
                \nUsage: To reset botname to default"
            ]
            
CMD_HELP.update({
    "sysd": Helpstring().get()[0]
})
CMD_HELP.update({
    "botver": Helpstring().get()[1]
})
CMD_HELP.update({
    "pip": Helpstring().get()[2]
})
CMD_HELP.update({
    "on": Helpstring().get()[3]
})
CMD_HELP.update({
    "botname": Helpstring().get()[4]
})