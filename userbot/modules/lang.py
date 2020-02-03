# Copyright (C) 2020 ZyCromerZ
#
""" Userbot lang command """

import time
from userbot import CMD_HELP, SET_LANG, BOT_NAME
from userbot.events import register

# ================= List Lang Start =================
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
    "Aku pergi! \nAku tidak tahu kapan aku akan kembali! \nSangat beberapa menit dari sekarang!\n\nBy: {BOT_NAME}", 
    "Aku tidak tersedia sekarang jadi tolong tinggalkan nama, nomor, dan alamatmu dan aku akan menguntitmu nanti.\n\nBy: {BOT_NAME}", 
    "Maaf, aku tidak di sini sekarang. \nJangan ragu untuk berbicara dengan pengguna saya selama Anda mau. \nSaya akan menghubungi Anda nanti.\n\nBy: {BOT_NAME}", 
    "Aku yakin kamu mengharapkan pesan tandang!\n\nBy: {BOT_NAME}", 
    "Hidup ini sangat singkat, ada banyak hal yang harus dilakukan ... \nAku akan melakukan salah satunya\nNanti saya hubungi lagi\n\nBy: {BOT_NAME}", 
]
AFKSTR_EN = [
    "I'm busy right now. Please talk in a bag and when I come back you can just give me the bag!\n\nBy: {BOT_NAME}",
    "I'm away right now. If you need anything, leave a message after the beep:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!\n\nBy: {BOT_NAME}",
    "You missed me, next time aim better.\n\nBy: {BOT_NAME}",
    "I'll be back in a few minutes and if I'm not...,\nwait longer.\n\nBy: {BOT_NAME}",
    "I'm not here right now, so I'm probably somewhere else.\n\nBy: {BOT_NAME}",
    "Roses are red,\nViolets are blue,\nLeave me a message,\nAnd I'll get back to you.\n\nBy: {BOT_NAME}",
    "Sometimes the best things in life are worth waiting for…\nI'll be right back.\n\nBy: {BOT_NAME}",
    "I'll be right back,\nbut if I'm not right back,\nI'll be back later.\n\nBy: {BOT_NAME}",
    "If you haven't figured it out already,\nI'm not here.\n\nBy: {BOT_NAME}",
    "Hello, welcome to my away message, how may I ignore you today?\n\nBy: {BOT_NAME}",
    "I'm away over 7 seas and 7 countries,\n7 waters and 7 continents,\n7 mountains and 7 hills,\n7 plains and 7 mounds,\n7 pools and 7 lakes,\n7 springs and 7 meadows,\n7 cities and 7 neighborhoods,\n7 blocks and 7 houses...\n\nWhere not even your messages can reach me!\n\nBy: {BOT_NAME}",
    "I'm away from the keyboard at the moment, but if you'll scream loud enough at your screen, I might just hear you.\n\nBy: {BOT_NAME}",
    "I went that way\n---->\n\nBy: {BOT_NAME}",
    "I went this way\n<----\n\nBy: {BOT_NAME}",
    "Please leave a message and make me feel even more important than I already am.\n\nBy: {BOT_NAME}",
    "I am not here so stop writing to me,\nor else you will find yourself with a screen full of your own messages.\n\nBy: {BOT_NAME}",
    "If I were here,\nI'd tell you where I am.\n\nBut I'm not,\nso ask me when I return...\n\nBy: {BOT_NAME}",
    "I am away!\nI don't know when I'll be back!\nHopefully a few minutes from now!\n\nBy: {BOT_NAME}",
    "I'm not available right now so please leave your name, number, and address and I will stalk you later.\n\nBy: {BOT_NAME}",
    "Sorry, I'm not here right now.\nFeel free to talk to my userbot as long as you like.\nI'll get back to you later.\n\nBy: {BOT_NAME}",
    "I bet you were expecting an away message!\n\nBy: {BOT_NAME}",
    "Life is so short, there are so many things to do...\nI'm away doing one of them..\n\nBy: {BOT_NAME}",
    "I am not here right now...\nbut if I was...\n\nwouldn't that be awesome?\n\nBy: {BOT_NAME}",
]

# ================= List Lang End =================

# ================= Setup Class Start =================
class language:
    def __init__(self):
        self.language = SET_LANG

    def __str__(self):
        return self.language

    def change(self, lang):
        assert isinstance(lang, str)
        self.language = lang

Language = language()

class Afkstr:
    def __init__(self):
        self.afkstr = None

    def __str__(self):
        if lang == "id":
            self.afkstr = AFKSTR_ID
        else:
            self.afkstr = AFKSTR_EN
        return self.afkstr

AFKSTR = Afkstr()

class Helpstring:
    def __init__(self):
        self.isi = None
    
    def __str__(self):
        if lang == "id":
            self.afkstr = ".setlang: untuk mengubah bahasa bot"
        else:
            self.afkstr = ".setlang: for change bot language"
        return self.afkstr

helpstring = Helpstring()
# ================= Setup Class End =================
@register(outgoing=True, pattern="^.setlang(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    await event.edit("Getting List notes . . .")
    time.sleep(1)
    args = event.pattern_match.group(1).lower()
    if args == "en":
        Language.change("en")
        await event.edit(f"set lang to `en` success")
    elif args == "id":
        Language.change("id")
        await event.edit(f"ubah bahasa ke `id` berhasil")
    else:
        await event.edit(f"only supported `en` and `id` ")

CMD_HELP.update({"setlang": helpstring})