import requests
import time
import os
import sys
from termcolor import colored

os.system("cls" if os.name == "nt" else "clear")



title = '🚀 DISCORD WEBHOOK SPAMMER 🚀(Beta Version 0.1) 2025  Created By JavaD  🔞!'
os.system(f'title {title}')

print("\033[1;32m DISCORD WEBHOOK SPAMMER \033[0m")

print("\033[1;31m Creator : JavaD \033[0m")
print("\033[1;31m Discord : javadsd.04 \033[0m")
print("\033[1;31m TeamSpeak Address : BT69.IR \033[0m")


ascii_art = """ 

 ▄▄▄██▀▀ ▄▄▄      ██▒   █▓ ▄▄▄      ▓█████▄ 
   ▒██  ▒████▄   ▓██░   █▒▒████▄    ▒██▀ ██▌
   ░██  ▒██  ▀█▄  ▓██  █▒░▒██  ▀█▄  ░██   █▌
▓██▄██▓ ░██▄▄▄▄██  ▒██ █░░░██▄▄▄▄██▒░▓█▄   ▌
 ▓███▒  ▒▓█   ▓██   ▒▀█░  ▒▓█   ▓██░░▒████▓ 
 ▒▓▒▒░  ░▒▒   ▓▒█   ░ ▐░  ░▒▒   ▓▒█░ ▒▒▓  ▒ 
 ▒ ░▒░  ░ ░   ▒▒    ░ ░░  ░ ░   ▒▒   ░ ▒  ▒ 
 ░ ░ ░    ░   ▒        ░    ░   ▒    ░ ░  ░ 
 ░   ░        ░        ░        ░      ░    
                                
                                            
"""


while True:
    print(colored(ascii_art, 'red'))
    webhook_url = input("\033[1;36m🔗 Enter Webhook URL: \033[0m")
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        break
    else:
        print("\033[1;31m❌ Invalid Webhook URL. Please make sure it starts with https://discord.com/api/webhooks/\033[0m")


message = input("\033[1;33m💬 Enter Message to Spam: \033[0m")


while True:
    try:
        count = int(input("\033[1;32m🔢 Enter Number of Messages: \033[0m"))
        if count > 0:
            break
        else:
            print("\033[1;31m❌ The number of messages must be greater than 0.\033[0m")
    except ValueError:
        print("\033[1;31m❌ Please enter a valid number.\033[0m")

print("\n\033[1;35m🔥 Spamming Started! Press Ctrl+C to Stop...\033[0m\n")
success = 0

for i in range(count):
    try:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            success += 1
           
            sys.stdout.write(f"\r\033[1;32m✅ Sent {i+1}/{count}\033[0m")
            sys.stdout.flush()
        else:
            print(f"\n\033[1;31m❌ Error {response.status_code}: {response.text}\033[0m")
            break
    except Exception as e:
        print(f"\n\033[1;31m⚠️ Error: {e}\033[0m")
        break
    time.sleep(0.001)  

print(f"\n\033[1;34m🎯 Done! {success}/{count} Messages Sent Successfully.\033[0m")
