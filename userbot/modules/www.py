# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import wget
import os

from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Running high speed test . . .`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    getPathImg = wget.download(result['share'])

    result=f"""Started at `{result['timestamp']}`
Client :
    ISP      : `{result['client']['isp']}`
    Country  : `{result['client']['country']}`

Server :
    Name     : `{result['server']['name']}`
    country  : `{result['server']['country']}` , `{result['server']['cc']}`
    Latency  : `{result['server']['latency']}`

Info :
    Ping     : `{result['ping']}`
    Sent     : `{speed_convert_bit(result['bytes_sent'])}`
    Received : `{speed_convert_bit(result['bytes_received'])}`
    Download : `{speed_convert_byte(result['download']) }/s` (`{speed_convert_bit(result['download']) }/s`)
    Upload   : `{speed_convert_byte(result['upload']) }/s` (`{speed_convert_bit(result['upload']) }/s`)"""
    await spd.delete()
    await spd.client.send_file(spd.chat.id,
                             getPathImg,
                             caption=result)
    os.remove(getPathImg)

def speed_convert_bit(ukuran: float) -> str:
    """
    Hi human, you can't read bit?
    """
    if not ukuran:
        return ""
    totals_isi = {0: '', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    totals = 2**10
    no = 0
    while ukuran > totals:
        ukuran /= totals
        no += 1
    return "{:.2f} {}B".format(ukuran, totals_isi[no])


def speed_convert_byte(size: float) -> str:
    """
    Hi human, you can't read bytes?
    """
    total = size/8
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb', 2: 'Mb', 3: 'Gb', 4: 'Tb'}
    while total > power:
        total /= power
        zero += 1
    return f"{round(total, 2)} {units[zero]}"




@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`pooong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping`\
    \nUsage: Shows how long it takes to ping your bot.\
    \n\n`.speed`\
    \nUsage: Does a speedtest and shows the results."
})
