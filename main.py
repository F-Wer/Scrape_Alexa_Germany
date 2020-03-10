import locale
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

options = Options()
options.add_argument('--headless')
# Ohne Ansicht des Browsers starten
options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
driver_path: str = r'D:\Programs\BrowserDriver\chromedriver.exe'
driver: WebDriver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get("https://www.alexa.com/topsites/countries/DE")
# Seite für die Top50 Webseiten in Deutschland
elem: object = driver.find_element_by_xpath(
    "//*[@id='alx-content']/div/section/div[1]/section[2]/span/span/div/div").text
# Elemente holen
alexa_rank = [elem]
str1 = ''.join(alexa_rank)
pattern = re.findall('[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}', str1)
# URL extrahieren; string da List kein regex unterstützt
driver.quit()
# Browser stoppen
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
timestamp = time.strftime("%d %B %Y %H:%M:%S %n", time.localtime())
# Aktuelle Uhrzeit im deutschen Format
str2: str = '\n'.join(pattern)
# String, da list nicht ausgeschrieben werden kann
with open('D:/Download/Seminararbeit/html_source_code.txt', 'w') as f:
    # Uhrzeit und Liste in Txt speichern
    f.write(timestamp)
    f.write(str2)
