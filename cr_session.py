from telethon import TelegramClient, sync, events, functions, types, connection
from colorama import Fore
from telethon.errors.rpcerrorlist import *
from telethon.errors import *
import socks
from telethon.tl.functions.account import GetAuthorizationsRequest

import os
from time import sleep
#Bảng màu
R = Fore.RED 
B = Fore.BLUE
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
C = Fore.CYAN
BA = Fore.BLACK
api_id = 2182338
api_hash = 'fa411eff2ec7dcf61bdfadd2478e07bb'
if not os.path.exists("session"):
   os.makedirs("session")
def session():
    print(Y+"Input phone")
    phone = input("Nhập số điện thoại (+84367362942): "+M)
    random_proxy = {"host":"209.127.191.180",
    "port":9279,
    "username":"gfgnwred",
    "password": "763b9d9w7gx6"}
    #proxy = (socks.SOCKS5, '209.127.191.180', 9279, True, 'gfgnwred', '763b9d9w7gx6')
    #client = TelegramClient("session/"+phone,api_id,api_hash)
    #client = TelegramClient("session/" + phone, api_id,api_hash,
     #                                   connection=connection.ConnectionTcpMTProxyRandomizedIntermediate, 
      #                                  proxy=(Prox['host'], Prox['port']))
    proxy = {
    'proxy_type': 'socks5', # (mandatory) protocol to use (see above)
    'addr': '45.137.60.112',      # (mandatory) proxy IP address
    'port': 6640,           # (mandatory) proxy port number
    'username': 'gfgnwred',      # (optional) username if the proxy requires auth
    'password': '763b9d9w7gx6',      # (optional) password if the proxy requires auth
    'rdns': True            # (optional) whether to use remote or local resolve, default remote
}
    client = TelegramClient(f'session/{phone}', api_id,api_hash,
                        connection=connection.ConnectionTcpFull,
                        proxy=proxy)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone,input(M+"Code login : "))
            print(G+"Create success session")
            print("Tạo thành công session "+Y+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except SessionPasswordNeededError:
            client.start(phone,input(M+'Password 2FA: '))
            print(G+"Create success session")
            print("Tạo thành công session "+Y+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except Exception as e:
            print(R,e," ",phone)
        client.disconnect()
    else:
        sessions = client(GetAuthorizationsRequest())
        for ip in sessions.authorizations:
            print(ip.ip)

        print(B+"Session has been created ")
        print("Session đã tạo từ trước "+phone)
        sleep(100)
        client.disconnect()
    print(C+"="*40)
while(True):
    session()