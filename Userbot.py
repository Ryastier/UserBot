#pip install colorama
#pip install parogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import random
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

owner = "████   ███  ███  █  █  ████  ████  █  █  ███  ████\n█  ██   █   █    █  █  █  █  █  █  █ █   █    █  █\n█  ██   █   ███  ████  ████  █     ██    ███  ████\n█  ██   █     █  █  █  █  █  █  █  █ █   █    █ █\n████   ███  ███  █  █  █  █  ████  █  █  ███  █ █\n"
os.system('cls||clear')
print(Fore.RED + owner)
print(Fore.CYAN + "Создатель бота telegram: @dishacker vk: @dishackeryt1")

app = Client("my_account")

@app.on_message(filters.command("t", prefixes=".") & filters.me)
def t(_, msg):
    orig_text = msg.text.split(".t ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 2)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 4)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@app.on_message(filters.command("zag", prefixes=".") & filters.me)
def zag(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "😒 Загрузка ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 2)
            sleep(0.3)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("😉 Загрузка завершена")
 
@app.on_message(filters.command("osk", prefixes=".") & filters.me)
def osk(_, msg):
    msg.edit("Лох")
    sleep(0.15)
    msg.edit("долбаеб")
    sleep(0.15)
    msg.edit("Не кто по жизни")
    sleep(0.15)
    msg.edit("пидрила")
    sleep(0.15)
    msg.edit("хуила")
    sleep(0.15)
    msg.edit("ссанина")
    sleep(0.15)
    msg.edit("пердун")
    sleep(0.15)
    msg.edit("вагина")
    sleep(0.15)
    msg.edit(".")

@app.on_message(filters.command("love", prefixes=".") & filters.me)
def love(_, msg):
	msg.edit("☁☁☁☁☁☁☁☁☁\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
	sleep(0.3)
	msg.edit("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
	sleep(0.3)
	msg.edit("☁☁☁☁☁☁☁☁☁\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
	sleep(0.3)
	msg.edit("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")

@app.on_message(filters.command("vzlom", prefixes=".") & filters.me) 

def vzlom(_, msg):
    try:
        for x in range(0, 10):
            msg.edit("🌑 Взлом аккаунта.")
            sleep(0.2)
            msg.edit("🌑 Взлом аккаунта..")
            sleep(0.2)
            msg.edit("🌑 Взлом аккаунта...")
            sleep(0.2)
            msg.edit("🌑 Взлом аккаунта....")
            sleep(0.2)
    except:
        print("Error")
    
    cheslovzlom = 0
    while (cheslovzlom < 100):
    	msg.edit("⚠Загрузка данных_" + str(cheslovzlom) + "%")
    	sleep(0.07)
    	cheslovzlom += random.randint(1, 3)
    msg.edit("✔Аккаунт взломан данные загружены в файл✔")
    sleep(3)
    msg.delete()

@app.on_message(filters.command("zag2", prefixes=".") & filters.me)
def zag2(_, msg):
    msg.edit("Loading… [][][][][][][][][][] 0%")
    sleep(0.7)
    msg.edit("Loading… █[][][][][][][][][] 10%")
    sleep(0.7)
    msg.edit("Loading… ██[][][][][][][][] 20%")
    sleep(0.7)
    msg.edit("Loading… ███[][][][][][][] 30%")
    sleep(0.7)
    msg.edit("Loading… ████[][][][][][] 40%")
    sleep(0.7)
    msg.edit("Loading… █████[][][][][] 50%")
    sleep(0.7)
    msg.edit("Loading… ██████[][][][] 60%")
    sleep(0.7)
    msg.edit("Loading… ███████[][][] 70%")
    sleep(0.7)
    msg.edit("Loading… ████████[][] 80%")
    sleep(0.7)
    msg.edit("Loading… █████████[] 90%")
    sleep(0.7)
    msg.edit("Loading… ██████████] 99%")
    sleep(0.7)
    msg.edit("Loading… ███████████ 100%")
    sleep(0.7)
    msg.edit("✔ Загрузка завершена")

@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(_, msg):
    try:
        cheslospam = msg.text.split()[1]
        for x in range(0, int(cheslospam)):
            idspam = msg.text.split()[2]
            textspam = msg.text.split()[3]
            app.send_message(idspam, textspam)
        
        app.send_message("me", "Спам завершен: " + cheslospam + " сообщений")

    except:
        print(Fore.RED + "Error: Используйте .spam (сколько смс спама) (@id) (текст)")

app.run()