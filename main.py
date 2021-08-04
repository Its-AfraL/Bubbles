
# ╔╗ ┬ ┬┌┐ ┌┐ ┬  ┌─┐┌─┐
# ╠╩╗│ │├┴┐├┴┐│  ├┤ └─┐   A powerful and Opensource Nitro-Generator with proxies server
# ╚═╝└─┘└─┘└─┘┴─┘└─┘└─┘
# Created by AfraL - https://github.com/Its-AfraL       

import os
import string
import random
import colorama
import requests
import configparser
from pyfade import Fade, Colors
from colorama import Fore, Style
from discord_webhook import DiscordWebhook
from headers.headers import bubbles_header

config = configparser.RawConfigParser()
config.read('config\config.ini')

valid_code_file = open('output\valid_codes.txt', 'w')

global config_variable

config_variable = {

    'proxies_number_of_use': config.get('proxies', 'proxies_number_of_use'),
    'use_webhook': config.get('discord', 'use_webhook'),
    'discord_webhook': config.get('discord', 'discord_webhook'),
    'ping_everyone': config.get('discord', 'ping_everyone') 
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def variable_init():

    global proxy_number_of_use
    proxy_number_of_use = config_variable["proxies_number_of_use"]
    proxy_number_of_use = int(proxy_number_of_use)

    global proxies_file
    proxies_file = open('ressources\proxies.txt', 'r')

    global number_of_proxies
    number_of_proxies = sum(1 for line in open("ressources\proxies.txt"))

    print(Fore.BLUE + Style.BRIGHT + "[CONFIG] Number of proxies : " + Fore.WHITE + Style.BRIGHT + str(number_of_proxies))
    print(Fore.BLUE + Style.BRIGHT + "[CONFIG] Number of use for one proxy : " + Fore.WHITE + Style.BRIGHT + str(proxy_number_of_use))
    print(Fore.BLUE + Style.BRIGHT + "[CONFIG] Use a webhook is setup on : " + Fore.WHITE + Style.BRIGHT + str(config_variable['use_webhook']))
    print(Fore.BLUE + Style.BRIGHT + "[CONFIG] Ping Everyone is setup on  : " + Fore.WHITE + Style.BRIGHT + str(config_variable['ping_everyone']))

def nitro_checker(nitro_code):

        url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true'

        response = requests.get(url, proxies=proxies)
    
        if response.status_code == 200:
            print(Fore.BLUE + Style.BRIGHT + "Proxy : " + proxy_server.strip() + Fore.GREEN + Style.BRIGHT + "  [ VALID ] " + Fore.WHITE + Style.BRIGHT + "https://discord.gift/" + nitro_code.strip())
            
            if config_variable['use_webhook'] == "True":
                if config_variable['ping_everyone'] == "True":
                    DiscordWebhook( 
                                url = config_variable['discord_webhook'],
                                content = f"Valid Nito Code detected! @everyone \n{nitro_code}"
                            ).execute()
                    valid_code_file.write(nitro_code)
                else:
                    DiscordWebhook( 
                                url = config_variable['discord_webhook'],
                                content = f"Valid Nito Code detected! \n{nitro_code}"
                            ).execute()
                    valid_code_file.write(nitro_code)
            else:
                valid_code_file.write(nitro_code)
                pass
        
        else:
            print(Fore.BLUE + Style.BRIGHT + "Proxy : " + proxy_server.strip() + Fore.RED + Style.BRIGHT + "  [ INVALID ] " + Fore.WHITE + Style.BRIGHT + "https://discord.gift/" + nitro_code.strip())
    
global nitro_code

clear()


random_number = random.randint(1, 4)

print(Fade.Vertical(Colors.blue_to_green_reversed, bubbles_header()))

variable_init()

for proxy_server in proxies_file:
    print(Fore.BLUE + Style.BRIGHT + "\n[*] " + Fore.WHITE + Style.NORMAL + "Reroll proxy server\n")
    for i in range(proxy_number_of_use):
        nitro_code = "".join(random.choices( 
                        string.ascii_uppercase + string.digits + string.ascii_lowercase,
                        k = 16
                    ))
        global proxies
        proxies = {
            'http': proxy_server
        }
        nitro_checker(nitro_code)

print(Fore.BLUE + Style.BRIGHT + "\n[*] " + Fore.WHITE + Style.NORMAL + "All proxies servers has been used")
