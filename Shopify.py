###########################################################--------------------------------------------#############################################################
import os
import requests
import responses
import aiohttp
from aiohttp import request
import time
import asyncio
import json
from datetime import date
import requests
from bs4 import BeautifulSoup
import re
import pymongo
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.request
import requests
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

###########################################################--------------------------------------------#############################################################


Prozzesor = "https://www.mindfactory.de/product_info.php/Intel-Core-i3-10100F-4x-3-60GHz-So-1200-TRAY_1386308.html"
Mainboard = "https://www.mindfactory.de/product_info.php/MSI-MPG-Z490-GAMING-PLUS-ATX-Intel-S1200-retail_1361673.html"
Ram = "https://www.mindfactory.de/product_info.php/16GB-G-Skill-Aegis-DDR4-3000-DIMM-CL16-Dual-Kit_1111126.html"
hdd = "https://www.mindfactory.de/product_info.php/4TB-Seagate-IronWolf-ST4000VN008-64MB-3-5Zoll--8-9cm--SATA-6Gb-s_1120762.html"
Netzteil = "https://www.mindfactory.de/product_info.php/400-Watt-be-quiet--System-Power-9-Non-Modular-80--Bronze_1228435.html"
kühler = "https://www.mindfactory.de/product_info.php/be-quiet--Pure-Rock-2_1359906.html"
GPU = ""
Gehause = "https://www.mindfactory.de/product_info.php/be-quiet--Pure-Base-500-Midi-Tower-ohne-Netzteil-schwarz_1329555.html"
wasserkuhlung = "https://www.mindfactory.de/product_info.php/NZXT-Kraken-X63-RGB-280mm-All-In-One-Wasserkuehlung-schwarz_1384559.html"
ssd = ""


###########################################################--------------------------------------------#############################################################


gached = [Prozzesor, Mainboard, Ram, hdd, kühler, Netzteil, GPU, Gehause, wasserkuhlung, ssd]

for i in range(0, len(gached)):
    try:
        for i in range(0,10):
            if gached[i] == str(""):
                print("town")
                gached.remove(gached[i])
    except IndexError:
        print("pass")
print(gached)


###########################################################--------------------------------------------#############################################################


cost = int()
for i in range(0, len(gached)):
    len_response = requests.get(gached[i]).text
    len_soup = BeautifulSoup(len_response, 'lxml')
    len_block = len_soup.find('div', class_ = "pprice").text
    price_count = len(len_block)
    terl = len_block[7:10]
    last = terl.replace(",", "")
    print( last)
    cost = cost + int(last)
print(cost)


###########################################################--------------------------------------------#############################################################
email = os.environ.get('EMAIL')
passw = os.environ.get('PASS')

s=Service(ChromeDriverManager().install())

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


driver.get("https://calibarpc.myshopify.com/admin/products/6700822396985")
sleep(1)
inputElement = driver.find_element_by_id("account_email")
inputElement.send_keys(email)
sleep(2)
driver.find_element_by_name("commit").click()

sleep(2)
inputElements = driver.find_element_by_id("account_password")
inputElements.send_keys(passw)
driver.find_element_by_name("commit").click()
sleep(7)

inputElements = driver.find_element_by_name("price")
inputElements.send_keys(Keys.CONTROL + "a")
inputElements.send_keys(Keys.DELETE)
inputElements.send_keys(cost)
sleep(1)
driver.find_element_by_css_selector(".Polaris-Button--primary_7k9zs").click()

time.sleep(20)

