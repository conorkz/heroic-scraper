from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pytz
from bs4 import BeautifulSoup
import re
import os
import requests
from http.cookies import SimpleCookie
s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)
roi = 'no info on the website'
driver.get('https://www.heroic.us/optimize/account/login')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '[type=email]').send_keys('vigomi1882@aicogz.com')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[type=password]').send_keys('zeta123456')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
time.sleep(5)
x = 1
while True:
    if x == 67:
        break
    driver.get(f'https://www.heroic.us/optimize/pn?page={x}')
    x+=1
    WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.image')))
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for a in soup.select('a.image'):
        link ='https://www.heroic.us' + a['href']
        print(link)
        rawdata = "OptanonAlertBoxClosed=2023-05-12T07:11:35.869Z; OptanonConsent=isGpcEnabled=1&datestamp=Sat+May+13+2023+11%3A58%3A37+GMT%2B0600+(East+Kazakhstan+Time)&version=6.31.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&geolocation=KZ%3B33&AwaitingReconsent=false; auth.strategy=local; __stripe_mid=433c07c8-925e-49ee-9ae7-bc22f8b174e7062695; intercom-id-j93o9ejx=78996592-d453-43e8-83ee-6c3e5d45a42f; intercom-device-id-j93o9ejx=e94c56b1-f9bf-4ad7-acda-a331b5eefd48; auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lm9wdGltaXplLm1lXC8iLCJpYXQiOjE2ODM4NzU1NjksIm5iZiI6MTY4Mzg3NTU2OSwic2Vzc2lvbl9pZCI6IjNfZFEzTUlkSjYxbkRwQndBQUctRXN4bUZzaTlzNjFSczVPSXE2UmFzN3dFTkdGM09VWmVHYktxOTRlWEsxeGF4S2REbm9sdzFDUEJmNjVMT0lybWVIOWtzVndjZEtMa1pMV08iLCJoZXJvaWNUb2tlbiI6ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJakZpWWpJMk16WTRZVE5rTVdFeE5EZzFZbU5oTlRKaU5HWTRNMkprWWpRNVlqWTBaV00yTW1ZaUxDSjBlWEFpT2lKS1YxUWlmUS5leUpwYzNNaU9pSm9kSFJ3Y3pvdkwzTmxZM1Z5WlhSdmEyVnVMbWR2YjJkc1pTNWpiMjB2YUdWeWIybGpMV0Z3Y0Mxd2NtOWtJaXdpWVhWa0lqb2lhR1Z5YjJsakxXRndjQzF3Y205a0lpd2lZWFYwYUY5MGFXMWxJam94Tmpnek9EYzFOVFk0TENKMWMyVnlYMmxrSWpvaWRITjJVSGRGYWtScldtZHZhSFptVURKWFowbG5iVlZLUzBReE15SXNJbk4xWWlJNkluUnpkbEIzUldwRWExcG5iMmgyWmxBeVYyZEpaMjFWU2t0RU1UTWlMQ0pwWVhRaU9qRTJPRE00TnpVMU5qZ3NJbVY0Y0NJNk1UWTRNemczT1RFMk9Dd2laVzFoYVd3aU9pSjJhV2R2YldreE9EZ3lRR0ZwWTI5bmVpNWpiMjBpTENKbGJXRnBiRjkyWlhKcFptbGxaQ0k2Wm1Gc2MyVXNJbVpwY21WaVlYTmxJanA3SW1sa1pXNTBhWFJwWlhNaU9uc2laVzFoYVd3aU9sc2lkbWxuYjIxcE1UZzRNa0JoYVdOdlozb3VZMjl0SWwxOUxDSnphV2R1WDJsdVgzQnliM1pwWkdWeUlqb2ljR0Z6YzNkdmNtUWlmWDAud3NlbU9wQlE1cE9tOG41TTYya0ViOTlXeTVKcnVSY1FWNWEySXJKTGg3NkdSY0x1cXFWWE9xbEozeVBlenA0VGk3YkN0M0hHcUtTdk1sYVdUdmFrRjU3akc5U0N1X2taTm9SVFp4WTdmdU0yUWZZTlVxSV82b3lwTEJ4SENXRHZkSm5jYlpOU2pISHh6Nk0zSmF2RldkT25zTl9ieXJlYWE4elBfQVVSbUlsaXhiTUNBRFhSTGQtNGlsRWpRaHVUNE9GSEJULWw4dlhXaS1uLVdfUVFFdnh0WGxLX0xQcEUtR1VmVWtXdmxveXBuT0JENC1ZUUxTd2t2U3g4VEVfUkVpOTNzb1pIRlBNb2FjX0UzaV82WWthancxU2lEeHVuaGV3eHc4UmxxT1VTWDl2ekRJMnZyUG9tWC1JMm1fQ0M3bE0tQ0hJYkFVT0dveVJxZnNtTW9BIiwiaGVyb2ljUmVmcmVzaFRva2VuIjoiQVBaVW8wUXYtLTFrQXFpMzg5TVdNME15Skx0Wm1UMlhkU1U5LV9FR2ZSc05aOVRuNVRhYVQyMGhqdkNhZy1hT1RtVHB6MWgzVVhuQW9JelpqZVFrMUJuMG8xYmZabkQ1T1B3bjJFOGJZaGZ4d1pDM2UwWjZRWEJHLVBELWFaYnozQl83Y1V1M0N1eV9xY3h4RXFiNGNFMkpVMlFIZFRGUFRwckVTZDZ6S21vSE82Q19oOEFoSkhmanl4YUNvN2lDSzBZVTI3X19qWVV1TGNmeE5sWU4waHY3QmRYOGphRXpmQSIsImV4cCI6MTc0NzAzMzk2OX0.szEcbhRRf8eWDkGtrxFVJ51Ws7u6kuyxFXNuxGawmaQ; auth._token_expiration.local=1747033969000; optimize_heroBannerShown=3702929; intercom-session-j93o9ejx=b0lKWlVsc0czM3Rrd0Zwd0dZQ1lIdTZuWGNyKzVidERpaXdsclhEUzhSU2ZUVDlzWHdwZEpHL0hJMnduTGhLLy0tS0t1amZZMUJYUjNKZFEzSGY0bEJ4dz09--c182f01919c9d37295e008fe8412eb4d6694fe62"
        cookie = SimpleCookie()
        cookie.load(rawdata)
        cookies = {k: v.value for k, v in cookie.items()}
        session = requests.Session()
        session.cookies.update(cookies)
        respons = session.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        sorpa = BeautifulSoup(respons.content, "html.parser")
        if sorpa.find(class_='-spacing-top-xxs'):
            description = sorpa.find(class_='-spacing-top-xxs').text
        else:
            description = roi
        title = sorpa.find('h1', class_='set-h4').text.strip()
        if sorpa.find('div', class_='set-h6'):
            subtitle = sorpa.find('div', class_='set-h6').text.strip()
        else:
            subtitle = roi
        if sorpa.find('span', class_='formatted-type'):
            ss = []
            for g in sorpa.find('span', class_='formatted-type').find_all('a'):
                ss.append(g.text)
            author = " and ".join(ss)
        else:
            author = roi
        f = sorpa.find('div', class_='details').text.strip()
        match = re.search(r'\|\s*\n\s*(.*)\n', f)
        if match:
            publisher = match.group(1)
        else:
            publisher = roi
        matcha = re.search(r'(\d+)\s*pages', f)
        if matcha:
            pages = matcha.group(1)
        else:
            pages = roi
        if sorpa.select_one('header img'):
            cover = sorpa.select_one('header img')['src']
            match = re.search(r'\/([\w-]+)-cover\.jpg', cover)
            if match:
                ada = match.group(1)
                pdf = f'https://assets.heroic.us/philosophers-notes/downloads/pdfs/files/member/{ada}.pdf'
                mp3 = f'https://assets.heroic.us/philosophers-notes/downloads/mp3s/files/{ada}.mp3'
                current_time = datetime.now(pytz.timezone('Europe/Berlin'))
                berlin = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
                adas = re.sub(r"[^\w\s]", "", ada)
                folder_path = os.path.join(r'D:\codes\heroic\files', adas)
                suffix = 1
                while os.path.exists(folder_path):
                    folder_path = os.path.join(r'D:\codes\heroic\files', f'{adas}({suffix})')
                    suffix += 1
                os.makedirs(folder_path)
                respon = requests.get(pdf)
                with open(os.path.join(folder_path, f'{adas}.pdf'), 'wb') as f:
                    f.write(respon.content)
                respo = requests.get(mp3)
                with open(os.path.join(folder_path, f'{adas}.mp3'), "wb") as fil:
                    fil.write(respo.content)
                with open(os.path.join(folder_path, f'{adas}.txt'), "w", encoding="utf-8") as file:
                    file.write(f"Link: {link}\n")
                    file.write(f"Book cover: {cover}\n")
                    file.write(f"Title: {title}\n")
                    file.write(f"Subtitle: {subtitle}\n")
                    file.write(f"Author: {author}\n")
                    file.write(f"Publisher: {publisher}\n")
                    file.write(f"Number of pages: {pages}\n")
                    file.write(f"Pdf link: {pdf}\n")
                    file.write(f"mp3 link: {mp3}\n")
                    file.write(f"Berlin time: {berlin}\n")
                    file.write(f"Description: {description}\n\n")
                    for g in sorpa.find('div', class_='-post-content').find_all_next(['p', 'li', 'h2']):
                        if g.text.strip() == 'About the author':
                            break
                        if g.text.strip() == 'About the authors':
                            break
                        file.write(g.text.strip() + "\n\n")