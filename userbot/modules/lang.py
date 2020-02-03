# Copyright (C) 2020 ZyCromerZ
#
""" Userbot lang command """

import time
from userbot import CMD_HELP, SET_LANG
from userbot.events import register

lang = SET_LANG
AFKSTR_ID = [
    "Saya sedang sibuk sekarang. Tolong bicara dalam tas dan ketika aku kembali kamu bisa memberikan tas itu padaku!\n\nBy: {BOT_NAME}", 
    "Aku pergi sekarang. Jika kamu butuh sesuatu, tinggalkan pesan setelah bunyi bip: \n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!\n\nBy: {BOT_NAME}", 
    "Kamu merindukanku, waktu berikutnya bertujuan lebih baik.\n\nBy: {BOT_NAME}", 
    "Aku akan kembali dalam beberapa menit dan jika aku tidak ..., tunggu sebentar.\n\nBy: {BOT_NAME}", 
    "Aku tidak di sini sekarang, jadi aku mungkin di tempat lain.\n\nBy: {BOT_NAME}", 
    "Mawar merah, \nPelindung berwarna biru, \nTinggalkan aku pesan, \nDan aku akan membalasmu.\n\nBy: {BOT_NAME}", 
    "Terkadang hal-hal terbaik dalam hidup layak untuk ditunggu ... aku akan segera kembali.\n\nBy: {BOT_NAME}", 
    "Aku akan segera kembali, tetapi jika aku tidak kembali, aku akan kembali nanti.\n\nBy: {BOT_NAME}", 
    "Jika Anda belum menemukan jawabannya, \nsaya tidak di sini.\n\nBy: {BOT_NAME}", 
    "Halo, selamat datang di pesan tandang saya, bagaimana saya bisa mengabaikan Anda hari ini?\n\nBy: {BOT_NAME}", 
    "Saya berada di 7 laut dan 7 negara, \n7 perairan dan 7 benua, \n7 gunung dan 7 bukit, \n7 dataran dan 7 gundukan, \n7 kolam dan 7 danau, \n7 mata air dan 7 padang rumput, \n7 kota dan 7 lingkungan, \n7 blok dan 7 rumah ... \n\nDimana bahkan pesan Anda tidak dapat menghubungi saya! \n\nBy: {BOT_NAME}", 
    "Aku sedang jauh dari keyboard saat ini, tetapi jika kamu akan menjerit cukup keras di layarmu, aku mungkin akan mendengarmu.\n\nBy: {BOT_NAME}", 
    "Aku pergi ke sana \n ---->\n\nBy: {BOT_NAME}", 
    "Aku pergi ke sini \n <----\n\nBy: {BOT_NAME}", 
    "Tolong tinggalkan pesan dan buat aku merasa lebih penting daripada aku.\n\nBy: {BOT_NAME}", 
    "Aku tidak di sini jadi berhentilah menulis kepadaku, atau kamu akan menemukan dirimu dengan layar penuh dengan pesanmu sendiri.\n\nBy: {BOT_NAME}", 
    "Jika aku ada di sini, aku akan memberitahumu di mana aku berada. \n\nTapi aku tidak, tanyakan padaku ketika aku kembali ...\n\nBy: {BOT_NAME}", 
    "Aku pergi! \NAku tidak tahu kapan aku akan kembali! \NSangat beberapa menit dari sekarang!\n\nBy: {BOT_NAME}", 
    "Aku tidak tersedia sekarang jadi tolong tinggalkan nama, nomor, dan alamatmu dan aku akan menguntitmu nanti.\n\nBy: {BOT_NAME}", 
    "Maaf, aku tidak di sini sekarang. \nJangan ragu untuk berbicara dengan pengguna saya selama Anda mau. \nSaya akan menghubungi Anda nanti.\n\nBy: {BOT_NAME}", 
    "Aku yakin kamu mengharapkan pesan tandang!\n\nBy: {BOT_NAME}", 
    "Hidup ini sangat singkat, ada banyak hal yang harus dilakukan ... \nAku akan melakukan salah satunya\nNanti saya hubungi lagi\n\nBy: {BOT_NAME}", 
]
AFKSTR_EN = [
    "I'm still afk\n\n{BOT_NAME}"
]
if lang == "id":
    AFKSTR = AFKSTR_ID
else:
    AFKSTR = AFKSTR_EN

@register(outgoing=True, pattern="^.setlang(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    await event.edit("Getting List notes . . .")
    time.sleep(1)
    global lang
    global AFKSTR
    args = event.pattern_match.group(1).lower()
    if args == "en":
        lang = args
        AFKSTR = AFKSTR_EN
        await event.edit(f"set lang to `en` success")
    if args == "id":
        lang = args
        AFKSTR = AFKSTR_ID
        await event.edit(f"ubah bahasa ke `id` berhasil")
    else:
        await event.edit(f"only supported `en` and `id` ")

if lang == "en":
    CMD_HELP.update({".setlang": "for change bot lang."})
if lang == "id":
    CMD_HELP.update({".setlang": "untuk mengubah bahasa bot."})