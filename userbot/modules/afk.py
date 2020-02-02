# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module which contains afk-related commands """

from random import choice, randint
from asyncio import sleep

from telethon.events import StopPropagation

from userbot import (AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG,
                     BOTLOG_CHATID, USERS, PM_AUTO_BAN, BOT_NAME)
from userbot.events import register

# ========================= CONSTANTS ============================
global BOT_NAME
AFKSTR = [
    "Saya sedang sibuk sekarang. Tolong bicara dalam tas dan ketika aku kembali kamu bisa memberikan tas itu padaku!\n\nBy: {BOT_NAME}", 
    "Aku pergi sekarang. Jika kamu butuh sesuatu, tinggalkan pesan setelah bunyi bip: \ n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!\n\nBy: {BOT_NAME}", 
    "Kamu merindukanku, waktu berikutnya bertujuan lebih baik.\n\nBy: {BOT_NAME}", 
    "Aku akan kembali dalam beberapa menit dan jika aku tidak ..., tunggu sebentar.\n\nBy: {BOT_NAME}", 
    "Aku tidak di sini sekarang, jadi aku mungkin di tempat lain.\n\nBy: {BOT_NAME}", 
    "Mawar merah, \ nPelindung berwarna biru, \ nTinggalkan aku pesan, \ nDan aku akan membalasmu.\n\nBy: {BOT_NAME}", 
    "Terkadang hal-hal terbaik dalam hidup layak untuk ditunggu ... aku akan segera kembali.\n\nBy: {BOT_NAME}", 
    "Aku akan segera kembali, tetapi jika aku tidak kembali, aku akan kembali nanti.\n\nBy: {BOT_NAME}", 
    "Jika Anda belum menemukan jawabannya, \ n saya tidak di sini.\n\nBy: {BOT_NAME}", 
    "Halo, selamat datang di pesan tandang saya, bagaimana saya bisa mengabaikan Anda hari ini?\n\nBy: {BOT_NAME}", 
    "Saya berada di 7 laut dan 7 negara, \ n7 perairan dan 7 benua, \ n7 gunung dan 7 bukit, \ n7 dataran dan 7 gundukan, \ n7 kolam dan 7 danau, \ n7 mata air dan 7 padang rumput, \ n7 kota dan 7 lingkungan, \ n7 blok dan 7 rumah ... \ n \ nDimana bahkan pesan Anda tidak dapat menghubungi saya! \n\nBy: {BOT_NAME}", 
    "Aku sedang jauh dari keyboard saat ini, tetapi jika kamu akan menjerit cukup keras di layarmu, aku mungkin akan mendengarmu.\n\nBy: {BOT_NAME}", 
    "Aku pergi ke sana \ n ---->\n\nBy: {BOT_NAME}", 
    "Aku pergi ke sini \ n <----\n\nBy: {BOT_NAME}", 
    "Tolong tinggalkan pesan dan buat aku merasa lebih penting daripada aku.\n\nBy: {BOT_NAME}", 
    "Aku tidak di sini jadi berhentilah menulis kepadaku, atau kamu akan menemukan dirimu dengan layar penuh dengan pesanmu sendiri.\n\nBy: {BOT_NAME}", 
    "Jika aku ada di sini, aku akan memberitahumu di mana aku berada. \ N \ nTapi aku tidak, tanyakan padaku ketika aku kembali ...\n\nBy: {BOT_NAME}", 
    "Aku pergi! \ NAku tidak tahu kapan aku akan kembali! \ NSangat beberapa menit dari sekarang!\n\nBy: {BOT_NAME}", 
    "Aku tidak tersedia sekarang jadi tolong tinggalkan nama, nomor, dan alamatmu dan aku akan menguntitmu nanti.\n\nBy: {BOT_NAME}", 
    "Maaf, aku tidak di sini sekarang. \ NJangan ragu untuk berbicara dengan pengguna saya selama Anda mau. \ NSaya akan menghubungi Anda nanti.\n\nBy: {BOT_NAME}", 
    "Aku yakin kamu mengharapkan pesan tandang!\n\nBy: {BOT_NAME}", 
    "Hidup ini sangat singkat, ada banyak hal yang harus dilakukan ... \ nAku akan melakukan salah satunya\nNanti saya hubungi lagi\n\nBy: {BOT_NAME}", 
]
# =================================================================


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global BOT_NAME
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"I'm AFK right now.\
                        \n-> {AFKREASON}\n\nBy: {BOT_NAME}")
                else:
                    await mention.reply(str(choice(AFKSTR).format(BOT_NAME=BOT_NAME)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if AFKREASON:
                    await mention.reply(f"I'm still AFK.\
                        \n-> {AFKREASON}\n\nBy: {BOT_NAME}")
                else:
                    await mention.reply(str(choice(AFKSTR).format(BOT_NAME=BOT_NAME)))
                USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                COUNT_MSG = COUNT_MSG + 1
                


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global BOT_NAME
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"I'm AFK right now.\
                    \n-> {AFKREASON}\n\nBy: {BOT_NAME}")
                else:
                    await sender.reply(str(choice(AFKSTR).format(BOT_NAME=BOT_NAME)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if AFKREASON:
                    await sender.reply(f"I'm still AFK.\
                    \n-> {AFKREASON}\n\nBy: {BOT_NAME}")
                else:
                    await sender.reply(str(choice(AFKSTR).format(BOT_NAME=BOT_NAME)))
                USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                COUNT_MSG = COUNT_MSG + 1


@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global BOT_NAME
    if string:
        AFKREASON = string
        await afk_e.edit(f"Going AFK!\
        \n-> {string}\n\nBy: {BOT_NAME}")
    else:
        await afk_e.edit(f"Going AFK!\n\nBy: {BOT_NAME}")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
    ISAFK = True
    raise StopPropagation

@register(outgoing=True, pattern=r"^[bB][rR][bB](?: |$)(.*)", disable_errors=True)
async def set_brb(brb_e):
    """ For brb command, allows you to inform people that you are afk when they message you """
    message = brb_e.text
    string = brb_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global BOT_NAME
    if string:
        AFKREASON = string
        await brb_e.edit(f"Going AFK!\
        \n-> {string}\n\nBy: {BOT_NAME}")
    else:
        await brb_e.edit(f"Going AFK!\n\nBy: {BOT_NAME}")
    if BOTLOG:
        await brb_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
    ISAFK = True
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    if ISAFK:
        ISAFK = False
        await notafk.respond("I'm no longer AFK.")
        await sleep(2)
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "You've recieved " + str(COUNT_MSG) + " messages from " +
                str(len(USERS)) + " chats while you were away",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "(" + str(i) + ")](tg://user?id=" + str(i) + ")" +
                    " sent you " + "`" + str(USERS[i]) + " messages`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


CMD_HELP.update({
    "afk":
    ".afk [Optional Reason]\
\nUsage: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere.\
    .brb \
\nUsage: same as afk"
})
