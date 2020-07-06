import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path = '/home/temp/chromedriver', options = options)
driver.get('https://www.google.com/')
time.sleep(2)

search_box = driver.find_element_by_name('q')
search_box.send_keys('엔씨')
search_box.submit()
time.sleep(2)

driver.quit()
