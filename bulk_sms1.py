# from lxml.html import fromstring
import requests
import codecs

# from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from itertools import cycle
from random import randint
import datetime
import time

print('Loading-------')
currentDT = datetime.datetime.now()
print('current date:' + str(currentDT))

phones = []
r_phones = open('testphones.txt', 'r', encoding="utf-8")
# with codecs.open('testphones.txt', 'r', encoding='utf-8',errors='ignore') as r_phones:
for r_phone in r_phones:
    each_phone = r_phone[0:len(r_phone)]
    if each_phone[-1] == "\n":
    	each_phone = r_phone[0:len(r_phone)-1]
    else:
        each_phone = r_phone[0:len(r_phone)]
	# each_phone = each_phone.decode("utf-8-sig").encode("utf-8")
	# each_phone = unicode(each_phone, errors='ignore')
    phones.append(each_phone)
print(phones)

message = ""
r_message = open('Message_text.txt', 'r')
for mes in r_message:
    message = mes
    if message[-1] == "\n":
        message = message[:-1]
print(message)
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(1400, 1000)
time.sleep(1)
driver.get('https://sms.to/login/#/')
# driver.navigate.to('https://sms.to/login/#/')
# time.sleep(3)
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-empty auth-button']")))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button is-info is-fullwidth']")))
driver.find_element_by_name("email").send_keys("contact@isobel-loans.com") 
driver.find_element_by_name("password").send_keys("Damland420")
driver.find_element_by_xpath("//button[@class='button is-info is-fullwidth']").click()
time.sleep(1)
driver.get("https://sms.to/app#/sms/send")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='icon-pencil']")))
driver.find_element_by_xpath("//*[text()='Write Message']").click()
time.sleep(1)
driver.find_element_by_xpath("//i[@class='icon-user']").click()
# sender_id

time.sleep(1)
for phone in phones:
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='sender_id']")))
	driver.find_element_by_name("sender_id").clear() #sender id
	time.sleep(1)
	driver.find_element_by_name("sender_id").send_keys("smsEE") #sender id
	time.sleep(1)
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='single_contact']")))
	driver.find_element_by_xpath("//input[@name='single_contact']").clear()
	driver.find_element_by_xpath("//input[@name='single_contact']").send_keys("+")
	time.sleep(0.5)
	driver.find_element_by_xpath("//input[@name='single_contact']").send_keys(phone)
	time.sleep(0.5)
	# driver.find_element_by_xpath("//textarea[@name='contacts']").send_keys(Keys.ENTER)
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='message']")))
	driver.find_element_by_xpath("//textarea[@name='message']").clear()
	time.sleep(1)
	driver.find_element_by_xpath("//textarea[@name='message']").click()
	time.sleep(1)
	driver.find_element_by_xpath("//textarea[@name='message']").send_keys(message)
	time.sleep(1)
	try:
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form[data-vv-scope='sms-form-submit'] button[type='submit']")))
		send_button = driver.find_element_by_css_selector("form[data-vv-scope='sms-form-submit'] button[type='submit']")
		if send_button.is_enabled():
			send_button.click()
	except NoSuchElementException:
		print("Skip")
	
	try:
		send_button = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal.align-baseline.is-active button.is-primary")))			
		send_button.click()
	except NoSuchElementException:
		print("Skip")
print("END")
driver.close()

# for phone in phones:

# 	print ("----- " + phone + " -----")
# 	try:
		
# 		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']")))

# 		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").clear()

# 		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='message']")))

# 		driver.find_element_by_xpath("//textarea[@id='message']").clear()
# 		# time.sleep(1)
# 		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").send_keys(phone)

# 		driver.find_element_by_xpath("//select[@id='caller_id']/option[@value='4593755408']").click()

# 		driver.find_element_by_xpath("//textarea[@id='message']").send_keys(message)
		

# 		send_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='sendsms_btn']")))
# 		send_button.click()
# 		time.sleep(1)

# 		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']")))

# 		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").clear()

# 		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='message']")))

# 		driver.find_element_by_xpath("//textarea[@id='message']").clear()

# 		print('success')
# 	except Exception as e:
# 		print('next')
# 		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']")))

# 		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").clear()

# 		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='message']")))

# 		driver.find_element_by_xpath("//textarea[@id='message']").clear()
# 		pass


# print("END")

# driver.close()





