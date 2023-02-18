import requests
import colorama
from colorama import Fore
import time
import pyshorteners
import tqdm
from tqdm import tqdm
from os import system
import os

TARJETA1="https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-4070-ti-12gb-gaming-x-trio-12gb-ddr6x-pci-express-4-0-graphics-card/6528410.p?skuId=6528410&intl=nosplash"
TARJETA2="https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-4090-gaming-x-trio-24g-24gb-ddr6x-pci-express-4-0-graphics-card/6528915.p?skuId=6528915&intl=nosplash"
TARJETA3="https://www.bestbuy.com/site/msi-nvidia-geforce-gtx-1660-super-ventus-xs-oc-6gb-gddr6-pci-express-3-0-graphics-card/6518174.p?skuId=6518174&intl=nosplash"


TAG_HTML="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"

PRODUCTOS =[
    ("RTX 4070 Ti",TARJETA1),
    ("RTX 4090",TARJETA2),
    ("GTX 1660 Super",TARJETA3),
   ]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
  "Accept": "*/*"
}



def guardar(contenido: str, nombre: str = "res.html") -> None:
  with open(nombre, "w",encoding="utf-8") as f:
    f.write(contenido)

def pagina(url: str) -> str:
  res = requests.get(url, headers=HEADERS)
  return res.text


def ext(html:str) -> bool:
    return TAG_HTML in html

def acortar(link:str) -> str:
    
    url_a = pyshorteners.Shortener()
    url_s = url_a.tinyurl.short(link)
    return url_s

def main() -> None:
    for nombre, url in PRODUCTOS:
        html = pagina(url)
        if ext(html):
            print(Fore.GREEN + f"SE ENCONTRÓ "+Fore.YELLOW + f"{nombre}"+  Fore.GREEN + f" EN {acortar(url)}")
        else:
            print(Fore.RED + f"NO HAY EXISTENCIAS DE: {nombre}")



   

def index() -> None:
    CONTADOR =1
    while True:
        if __name__ == "__main__":
            print(Fore.YELLOW + f"Ciclo {CONTADOR} ")
            main()

        for i in tqdm (range(150),desc="Renovando Ciclo...",ascii=False, ncols=75):
            time.sleep(.8)
        CONTADOR += 1
        os.system("cls")
        
index()


html =  pagina(VALIDADOR)
guardar(html)