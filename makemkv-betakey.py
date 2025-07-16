import requests
from bs4 import BeautifulSoup

#
# MakeMKV - BetaKey Activator v1.0
# KlimasTech.eu.org
#

# MakeMKV - Beta Key
url = "https://forum.makemkv.com/forum/viewtopic.php?t=1053"

# Przeszukiwanie strony 
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

code_tag = soup.find("code")

if code_tag:
    key = code_tag.text.strip()
    print("Znaleziono klucz MakeMKV Beta: ") 
    print(key)

# Zapis do pliku .reg
    reg_content = f'''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\\Software\\MakeMKV]
"app_Key"="{key}"
'''
    with open("makemkv-betakey.reg", "w", encoding="utf-8") as f:
        f.write(reg_content)
# Informacja o bledzie
else:
    print("Nie znaleziono znacznika <code>.")
