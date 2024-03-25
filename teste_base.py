

from time import sleep
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from teste_datas import Zonyas
from teste_print import *


z = Zonyas(0)
dia, dia_da_semana, dia_do_mes,ultimo_dia, mes, mes_extenso, ano, hora, min = z.week_days()



domain = r'http://demo.automationtesting.in/Register.html'


# Função para abrir o navegador com base no link
def web_incognito(url):
    pg.hotkey('win', 'd')

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    chrome = "C:\\Users\\rayan\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe"
    service = Service(chrome)
    nav = webdriver.Chrome(service=service, options=options)

    nav.maximize_window()

    nav.get(url)

    return nav
