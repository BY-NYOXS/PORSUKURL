import pyshorteners
import time
from colorama import Fore,Back,Style
import os

os.system('clear')

tool_isim='''

██████╗░░█████╗░██████╗░░██████╗██╗░░░██╗██╗░░██╗██╗░░░██╗██████╗░██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║██║░██╔╝██║░░░██║██╔══██╗██║░░░░░
██████╔╝██║░░██║██████╔╝╚█████╗░██║░░░██║█████═╝░██║░░░██║██████╔╝██║░░░░░
██╔═══╝░██║░░██║██╔══██╗░╚═══██╗██║░░░██║██╔═██╗░██║░░░██║██╔══██╗██║░░░░░
██║░░░░░╚█████╔╝██║░░██║██████╔╝╚██████╔╝██║░╚██╗╚██████╔╝██║░░██║███████╗
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝
                                                       |by NYOXS|v1|
'''

token='02ac7103731866efe15e9ded7c6b2fd244eac0be'

print(Fore.CYAN+tool_isim)

urlm=input(Fore.BLUE+"\n\nKISALTILACAK URL:")

a=input(Fore.RED+"\n\n\nFAKE DOMAİN İSTERMİSİNİZ(y,N):")


if a == 'y':
    method=pyshorteners.Shortener(api_key=token)
    b=input(Fore.BLUE+"\n\n\nFAKE DOMAİN:")

    kurl=method.bitly.short(urlm)
    yeniurl= kurl[:8] + b+'@' + kurl[8:]
    print(Fore.YELLOW+f"KISALTILMIŞ URL:",Fore.WHITE+f"{yeniurl}")
else :
    method=pyshorteners.Shortener(api_key=token)
    kurl=method.bitly.short(urlm)
    print(Fore.YELLOW+f"\n\n\nKISALTILMIŞ URL:",Fore.WHITE+f"{kurl}")
