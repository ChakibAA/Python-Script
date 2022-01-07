import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

content = """
Message
"""


chrome_options = Options()
# chrome_options.add_argument("headless")
chrome_options.add_argument(
    "--user-data-dir=/PROFILE PATH")
chrome_options.add_argument('--profile-directory=Profile 1')

browser = webdriver.Chrome(
    executable_path=r"/PATH-Chrome-Driver", options=chrome_options)

with open('tel.csv', 'r') as csvFile:
    read = csv.reader(csvFile)
    for line in read:
        num = line

        print(num)
        browser.get(
            'https://web.whatsapp.com/send?phone='+str(num)+'&text='+content)

        try:
            browser.switch_to.alert.accept()
        except:
            print('Error alert')

        try:
            element = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='_4sWnG']")
                )).click()
        except:
            print('Error button ')

        time.sleep(5)

        print('-------')
