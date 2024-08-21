# Coded by 7b3087

import requests
import colorama
import os
from colorama import Fore
from colorama import Fore

vert = Fore.GREEN

class IpInfo():
    def __init__(self,url):
        self.url = url

    def check_status(self):
        query_check = requests.get(self.url)
        self.query_check_json = query_check.json()
        if self.query_check_json['status'] == 'success' :
            return 'success'
        else:
            print(Fore.RED,'IP invalid !',Fore.RESET)
            return 'failed'

    def get_info(self):
        info = self.query_check_json
        print("")
        print('Target :    ',Fore.CYAN,info['query'],Fore.RESET)
        print('Country :   ',Fore.CYAN,info['country'],Fore.RESET)
        print('RegionName :',Fore.CYAN,info['regionName'],Fore.RESET)
        print('City :      ',Fore.CYAN,info['city'],Fore.RESET)
        print('TimeZone :  ',Fore.CYAN,info['timezone'],Fore.RESET)
        print('ISP :       ',Fore.CYAN,info['isp'],Fore.RESET)
        print("")
        print('Location based on lat and lon in google map :')
        google_map_prefix = 'https://www.google.com/maps/place/'
        lat_and_lon = str(info['lat']) + "," + str(info['lon'])
        google_map_location = google_map_prefix + lat_and_lon
        print(Fore.GREEN,google_map_location,Fore.RESET)
        print("")

url_prefix = 'http://ip-api.com/json/'
yes_list = ['oui','y','yes','yep']

while True :
    print("""
           
 ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
    ░  ░    ░ ░      ░ ░  ░  ░      ░                             
              """)
    print(Fore.YELLOW,"Si vous souhaitez obtenir vos informations IP, tapez /moi",Fore.RESET)
    print ('')
    target = input(' IP address: ').lower().strip()

    if target == '/moi' :
        target = ''
    elif target == '' :
         print(Fore.YELLOW,'Vous n’avez rien saisi pour que votre adresse IP soit vérifiée ! ',Fore.RESET)

    url = url_prefix + target
    target_ip_info = IpInfo(url)
    target_status = target_ip_info.check_status()

    if target_status == 'success' :
        target_ip_info.get_info()
        again_or_not = input('again (y)? :').lower().strip()
        if again_or_not in yes_list:
            continue
        else:
            break

    elif target_status == 'failed' :
        again_or_not = input('again (y)? :').lower().strip()
        if again_or_not in yes_list :
            continue
        else:
            break

print(Fore.CYAN,'A bientot !',Fore.RESET)
exit()