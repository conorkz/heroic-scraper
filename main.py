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
directory = r'your_directory'
driver = webdriver.Chrome(service=s)
roi = 'no info on the website'
driver.get('https://www.heroic.us/optimize/account/login')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '[type=email]').send_keys('your_email')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[type=password]').send_keys('your_password')
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
        rawdata = 'your_cookie'
        cookie = SimpleCookie()
        cookie.load(rawdata)
        cookies = {k: v.value for k, v in cookie.items()}
        session = requests.Session()
        session.cookies.update(cookies)
        response = session.get(link, headers={'User-Agent': 'Mozilla/5.0'})
        sorpa = BeautifulSoup(response.content, "html.parser")
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
                folder_path = os.path.join(directory, adas)
                suffix = 1
                while os.path.exists(folder_path):
                    folder_path = os.path.join(directory, f'{adas}({suffix})')
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
