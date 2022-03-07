
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
from colorama import init, Fore
import pickle

init()

r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
SLEEP_TIME = ()

class main():

    def banner():

        print(f"""==================================================================================================================        
     _____    _                                  _____                _  ___  ___                               
    |_   _|  | |                                /  ___|              | | |  \/  |                               
      | | ___| | ___  __ _ _ __ __ _ _ __ ___   \ `--.  ___ _ __   __| | | .  . | ___  ___ ___  __ _  __ _  ___ 
      | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \   `--. \/ _ \ '_ \ / _` | | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \ |
      | |  __/ |  __/ (_| | | | (_| | | | | | | /\__/ /  __/ | | | (_| | | |  | |  __/\__ \__ \ (_| | (_| |  __/
      \_/\___|_|\___|\__, |_|  \__,_|_| |_| |_| \____/ \___|_| |_|\__,_| \_|  |_/\___||___/___/\__,_|\__, |\___|
                      __/ |                                                                           __/ |     
                     |___/                                                                           |___/      

    =============================================================================================================
                                                            Sell Tool For MMO //. Design By khmerifix Animation 
                                                            Donate: ABA Account : 000851896   Name : SENG NET
                                                            Donate: AC Toanchet : 0888881716  Name : SENG NET
    =============================================================================================================
    """)
    def send_sms():

        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        for a in accounts:
            phn = a[0]
            print(f'{plus}{grey} Checking {lg}{phn}')
            client = TelegramClient(f'sessions/{phn}', 8072747 , 'c7ef5f7d25c4c42127c1fb8cc7722c0a')
            client.connect()
            banned = []
            if not client.is_user_authorized():
                try:
                    client.send_code_request(phn)
                    print('OK')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print(info+lg+' Banned account removed[Remove permanently using manager.py]'+rs)
            time.sleep(0.5)
            client.disconnect()
        
        # client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
         
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phn)
            os.system('clear')
            main.banner()
            client.sign_in(phn, input(gr+'[+] Enter the code: '+re))
        




main.send_sms()