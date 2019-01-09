#!/usr/bin/env python3

# Scriot to send define numbers of messages to a WhatsApp web users or group, using selenium and chrome

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))
wait = WebDriverWait(driver = driver, timeout = 900)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()

wait = WebDriverWait(driver = driver, timeout = 600)
driver.close()
