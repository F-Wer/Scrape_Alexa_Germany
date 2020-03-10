import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

options = Options()
options.add_argument('--headless')
options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
driver_path: str = r'D:\Programs\BrowserDriver\chromedriver.exe'
driver: WebDriver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get("https://www.alexa.com/topsites/countries/DE")
print('working')
# element = driver.find_element_by_class_name('listings table').text
elem = driver.find_element_by_xpath("//*[@id='alx-content']/div/section/div[1]/section[2]/span/span/div/div").text
# source_code = elem.get_attribute("tableContainer")
alexa_rank = []
alexa_rank.append(elem)
str1 = ''.join(alexa_rank)
pattern = re.findall('[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}',str1)
print(pattern)
driver.quit()
str2 = '\n'.join(pattern)
print(str2)
with open('D:/Download/Seminararbeit/html_source_code.txt', 'w') as f:
    f.write(str2)
