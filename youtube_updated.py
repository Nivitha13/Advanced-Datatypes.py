from selenium import webdriver

import time

driver = webdriver.Chrome(r'<path>chromedriver.exe')

driver.get("http://www.youtube.com")

driver.find_element_by_xpath("//input[contains(@id,'search')]").send_keys('Taare gin')

driver.find_element_by_xpath("//button[contains(@id,'search-icon-legacy')]").click()

time.sleep(5)

driver.find_element_by_xpath("//a[@id='video-title' and (contains(@title,'Dil Bechara- Taare Ginn |Official Video|Sushant, Sanjana|A.R.Rahman|Mohit, Shreya|Mukesh C|Amitabh B'))]").click()

time.sleep(10)

driver.quit()
