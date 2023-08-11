import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import signal
from os import _exit
DRIVER_PATH='./chromedriver'
try:
    tt=open("os.txt","r").read().strip()
    if tt=="linux":
        DRIVER_PATH='./chromedriver'
        print("your system is linux/mac/android (remove \"os.txt\" file if you need to change this)")
    else:
        DRIVER_PATH='./chromedriver.exe'
        print("your system is windows (remove \"os.txt\" file if you need to change this)")
except:
    tt=open("os.txt","w")
    ttt=input("your system is windows ? y/n :")
    if ttt.lower()=="n" or ttt=="":
        tt.write("linux")
        tt.close()
    else:
        tt.write("windows")
        tt.close()
    tt=open("os.txt","r").read().strip()
    if tt=="linux":
        DRIVER_PATH='./chromedriver'
        print("your system is linux/mac/android")
    else:
        DRIVER_PATH='./chromedriver.exe'
        print("your system is windows")

def interaption_handler(signum,func):
    print("program terminated")
    _exit(1)

signal.signal(signal.SIGINT,interaption_handler)



ar_url=[
    'https://aminoapps.com/explore/lshy-ln/19d9981c-24ac-4214-83fe-fb85e4172a73',
    "https://aminoapps.com/explore/lthqf-lasywy/f96a93f9-2bdf-4414-9a3e-36476d9baa33",
    "https://aminoapps.com/explore/dhk-wsdqt/ee85c244-0c2e-4028-b8b3-a3fabce5227a",
    "https://aminoapps.com/explore/nmy/e06c2263-2578-4653-a6a2-5adc6d4d20c0",
    "https://aminoapps.com/explore/ryd/26cf7195-7dcf-4fcc-8899-bfed1a356e7e",
    "https://aminoapps.com/explore/l-b-lktrwny/31bff6b9-3ab3-4d9a-9a50-01d03befdd77",
    "https://aminoapps.com/explore/mqh-lmthqfyn/81605ff3-ddfe-4353-bf76-0259a1080d1f",
    "https://aminoapps.com/explore/lfn/806ff09e-d6c0-4ea4-ab3b-7d5087cc6002",
]

en_url=[
"https://aminoapps.com/explore/bubbling-communities/19cb8f8b-0e1a-48a6-8647-2d49d36a894d",
"https://aminoapps.com/explore/music/bcc70197-c646-4056-9bc2-1df9a6c924eb",
"https://aminoapps.com/explore/official-amino-partners/5b28ea8c-4da4-47d9-98ea-c9b89a513bc5",
"https://aminoapps.com/explore/k-pop/06b7ce84-06f9-4363-9205-dc75bf89015b",
"https://aminoapps.com/explore/animal-lovers/f13b526b-f0f0-4fdc-ae28-baaaa61b9b5d",
"https://aminoapps.com/explore/indie-hits/6080b8ab-f922-45e7-ac4a-91e386ba98a6",
"https://aminoapps.com/explore/comics-and-cartoons/0223eb33-f7d2-4c0d-a5e0-4e262f371cba",
"https://aminoapps.com/explore/aesthetic/8dc2e9f1-5718-4344-b892-578a107dc28f",
"https://aminoapps.com/explore/trending-rp/e29fce8a-2f7a-4e50-b383-34881efa505b",
"https://aminoapps.com/explore/musical-fans/ecc2a2c6-2c3e-4528-a5a1-600f837ab22c",
"https://aminoapps.com/explore/fashion-beauty/51705005-fd51-4c9f-96d2-eff3ccd6f6c7",
"https://aminoapps.com/explore/hobbies/85e232cb-341c-492a-a5f5-aaf9961b98ad",
"https://aminoapps.com/explore/anime-and-manga/c5379a3b-145d-41b1-bb0c-ae2c066117ab",
"https://aminoapps.com/explore/just-friends/ba9cfb7e-1168-4f1c-8693-32505c531c6a",
"https://aminoapps.com/explore/darkness/dca4f7b1-479b-4ef9-886c-53e0bf3aa99c",
"https://aminoapps.com/explore/lifestyle/38f32c98-1085-49a1-9b02-6cd1fce5b3b5",
"https://aminoapps.com/explore/handheld-games/c6568a05-2535-4091-9775-df5a57fd9624",
"https://aminoapps.com/explore/lgbt-center/13d128bd-e022-4ddd-a96c-aa4d66a97f58",
"https://aminoapps.com/explore/yt-friends/c61da5d2-653e-4196-85aa-06223c008cbe",
"https://aminoapps.com/explore/writers-corner/097202c4-5403-4ad3-9c64-43d437050da3",
"https://aminoapps.com/explore/sports/2c032260-3bae-4dfe-bec9-c48ec2f08121",
"https://aminoapps.com/explore/gaming-season/be8cdc71-c65b-4330-b9c7-c4d826786321",
"https://aminoapps.com/explore/artists-alley/081c5fc4-0e76-49e0-a7ea-d6ed1f31b25e",

]

ar_url_akhr=[
"https://aminoapps.com/explore/akhr/f30116d1-7d1f-43d9-bd80-0b03ebf60b21"
]



def funco(url,driver):
    checker_url=False
    while checker_url==False:
        try:
            driver.get(url)
            time.sleep(3)
            driver.find_element(by=By.CLASS_NAME,value="children")
            checker_url=True
        except:
            checker_url=False
    ph=driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight+1000)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight+1000)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight+1000)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight+1000)")
        time.sleep(1)
        
        newh=driver.execute_script("return document.body.scrollHeight")
        if ph==newh:
            break
        ph=newh

    children=driver.find_element(by=By.CLASS_NAME,value="children")
    cc=children.find_elements(by=By.TAG_NAME,value="a")
    listo=[]
    print("\nsize is : ",len(cc),"\n")
    for c in cc:
        listo.append(c.get_attribute("data-community"))
        print(c.get_attribute("data-community"))
    return listo

def safaya_atkrar(l):
    return  list(set(l)) 

def ar():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--disable-gpu')
    service = Service(executable_path=DRIVER_PATH)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    listos=[]
    for u in ar_url:
        listos.extend(funco(u,driver))
    listos=safaya_atkrar(listos)   

    www="\n".join(listos)
    fileo=open("result_ar.txt","w")
    fileo.write(www)
    fileo.close()
    print("all comIds saved in result_ar.txt")

def en():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--disable-gpu')
    service = Service(executable_path=DRIVER_PATH)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    listos=[]
    for u in en_url:
        listos.extend(funco(u,driver))
    listos=safaya_atkrar(listos)   

    www="\n".join(listos)
    fileo=open("result_en.txt","w")
    fileo.write(www)
    fileo.close()
    print("all comIds saved in result_en.txt")

def ar_akhr():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--disable-gpu')
    service = Service(executable_path=DRIVER_PATH)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    listos=[]
    for u in ar_url_akhr:
        listos.extend(funco(u,driver))
    listos=safaya_atkrar(listos)   

    www="\n".join(listos)
    fileo=open("result_ar_big.txt","w")
    fileo.write(www)
    fileo.close()
    print("all comIds saved in result_ar_big.txt")




